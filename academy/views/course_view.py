from rest_framework.generics import ListAPIView
from academy.serializers import CourseSerializer
from academy.serializers import CourseSimpleSerializer
from academy.pagination import CourseListPagination
from academy.models import Course
from django.db.models import Q


class CourseListView(ListAPIView):

    serializer_class = CourseSerializer
    pagination_class = CourseListPagination
    queryset = Course.objects.all()


class PublishedCourseView(ListAPIView):

    serializer_class = CourseSerializer
    pagination_class = CourseListPagination

    def get_queryset(self):
        return Course.objects.filter(is_published = True).order_by('created_at')


class TeacherCoursesView(ListAPIView):

    serializer_class = CourseSerializer

    def get_queryset(self):
        
        teacher_id = self.kwargs['teacher_id']
        
        return Course.objects.filter(teacher__id = teacher_id)
    

class SearchCoursesView(ListAPIView):

    serializer_class = CourseSerializer
    pagination_class = CourseListPagination

    def get_queryset(self):
        query = self.request.query_params.get('c')

        if not query:
            return Course.objects.none()
        
        return Course.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        ).order_by('id')
    

class CoursePriceView(ListAPIView):

    serializer_class = CourseSerializer
    pagination_class = CourseListPagination

    def get_queryset(self):

        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        queryset = Course.objects.all()

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset.order_by('price')
    

class StudentCoursesView(ListAPIView):

    serializer_class = CourseSimpleSerializer
    pagination_class = CourseListPagination

    def get_queryset(self):

        student_id = self.kwargs['student_id']

        queryset = Course.objects.filter(enrollments__student_id=student_id)

        return queryset

    
class CompletedCoursesView(ListAPIView):

    serializer_class = CourseSerializer
    pagination_class = CourseListPagination


    def get_queryset(self):
        
        student_id = self.kwargs["student_id"]

        queryset = Course.objects.filter(
            enrollments__student_id = student_id, 
            enrollments__completed=True
        )
        print(queryset.query)
        return queryset
    

#VIEW LISTA PRACTICANDO Q()
class PublishedView(ListAPIView):

    serializer_class = CourseSimpleSerializer
    pagination_class = CourseListPagination

    def get_queryset(self):

        queryset = Course.objects.filter(
            Q(price__lt=120) | 
            Q(is_published=True, teacher__specialty__icontains='python'))
        
        print(queryset.query)

        return queryset


class NotPublishedView(ListAPIView):

    serializer_class = CourseSerializer
    pagination_class = CourseListPagination
    queryset = Course.objects.exclude(is_published=True)


class NotTeacherView(ListAPIView):

    serializer_class = CourseSerializer
    pagination_class = CourseListPagination

    def get_queryset(self):
        return Course.objects.filter(teacher_id__isnull=True)


class GetTeacherView(ListAPIView):

    serializer_class = CourseSerializer
    pagination_class = CourseListPagination

    def get_queryset(self):
        return Course.objects.filter(teacher_id__in=[1,3,5])
    
from django.db.models import Count

class TotalStudentView(ListAPIView):

    serializer_class = CourseSimpleSerializer
    pagination_class = CourseListPagination

    def get_queryset(self):

        queryset = Course.objects.annotate(student_count=Count('enrollments')).order_by('id')

        print(queryset.query)
        return queryset


from django.db.models import Avg
from django.db.models.functions import Round

class AverageRatingView(ListAPIView):

    serializer_class = CourseSimpleSerializer
    pagination_class = CourseListPagination

    def get_queryset(self):
        queryset = Course.objects.annotate(
            average_rating=Round(Avg('reviews__rating'),precision=2)
        ).order_by('id')

        print(queryset.query)
        return queryset