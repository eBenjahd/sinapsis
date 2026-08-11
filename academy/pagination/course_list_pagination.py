from rest_framework.pagination import PageNumberPagination

class CourseListPagination(PageNumberPagination):

    page_size = 5