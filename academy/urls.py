from django.urls import path
from academy.views import (
    CourseListView,
    PublishedCourseView, 
    TeacherCoursesView, 
    SearchCoursesView, 
    CoursePriceView, 
    StudentCoursesView, 
    CompletedCoursesView,
    PublishedView,
    NotPublishedView,
    TotalStudentView,
    AverageRatingView,
    CreateTeacherView
)

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='courses'),
    path('published/courses/', PublishedCourseView.as_view(), name='published_courses'),
    path("courses/teacher/<int:teacher_id>/", TeacherCoursesView.as_view()),
    path("search/", SearchCoursesView.as_view(), name="search_course"),
    path("price/", CoursePriceView.as_view(), name="price"),
    path("courses/student/<int:student_id>/", StudentCoursesView.as_view()),
    path("courses/student/<int:student_id>/completed/", CompletedCoursesView.as_view()),
    path("published/", PublishedView.as_view(), name="published"),
    path("not_published/", NotPublishedView.as_view(), name="not_published"),
    path("total_student/", TotalStudentView.as_view(), name="total_student"),
    path("avg_rating/", AverageRatingView.as_view(), name="avg_rating"),
    path('create/teacher/' ,CreateTeacherView.as_view(), name='create_teacher'),
]