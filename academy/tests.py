from django.test import TestCase
from academy.models import Teacher

# Create your tests here.
class CanCreateTeacher(TestCase):

    def setUp(self):
        self.teacher = Teacher.objects.create(
            name='Benjamin',
            email='ebenja@gmail.com',
            specialty='compute science',
        )

    def test_create_teacher(self):

        response = self.client.post(
            '/api/academy/create/teacher/',
            data={
                "name": "Carlos",
                "email": "carlos@gamil.com",
                "specialty": "Backend",
            },
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)


# CAN'T CREATE WITH AN EMAIL ALREADY REGISTERED
class CanRegisterSameEmail(TestCase):

    def setUp(self):

        self.teacher = Teacher.objects.create(
            name='Benjamin',
            email='ebenja@gmail.com',
            specialty='compute science',
        )

    def test_cant_register_with_same_email(self):

        teacher_before = Teacher.objects.count()

        response = self.client.post(
            '/api/academy/create/teacher/',
            data={
                "name": "Benja",
                "email": self.teacher.email,
                "specialty": "Backend",
            },
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            Teacher.objects.count(),
            teacher_before
        )


#CURSOS DE UN PROFESOR
from academy.models import Course

class BelongsCourseToTeacher(TestCase):

    def setUp(self):

        self.teacher = Teacher.objects.create(
            name='Benjamin',
            email='ebenja@gmail.com',
            specialty='compute science',
        )

        self.teacher_2 = Teacher.objects.create(
            name='Rodrigo',
            email='rodrigo@gmail.com',
            specialty='pyschology',
        )

        self.course_1 = Course.objects.create(
            title='backend',
            description='backend with python',
            price=129.90,
            teacher=self.teacher
        )
        self.course_2 = Course.objects.create(
            title='devops',
            description='aws for beginner',
            price=209.90,
            teacher=self.teacher
        )
        self.course_3 = Course.objects.create(
            title='cloud computing',
            description='google cloud from scratch',
            price=169.90,
            teacher=self.teacher
        )

        self.course_4 = Course.objects.create(
            title='sesgos cognitivos',
            description='know your limitations',
            price=19.90,
            teacher=self.teacher_2
        )

        
    def test_related_name_courses(self):

        courses_teacher_one = self.teacher.courses.all() 
        courses_teacher_two = self.teacher_2.courses.all()

        self.assertEqual(courses_teacher_one.count(), 3)
        self.assertEqual(courses_teacher_two.count(), 1)

        self.assertIn(self.course_1, courses_teacher_one)
        self.assertIn(self.course_2, courses_teacher_one)
        self.assertIn(self.course_3, courses_teacher_one)
        self.assertIn(self.course_4, courses_teacher_two)


#CASCADE DELETE
from academy.models import Lesson

class DeleteCascadeCourseLesson(TestCase):

    def setUp(self):

        self.teacher = Teacher.objects.create(
            name='Benjamin',
            email='ebenja@gmail.com',
            specialty='compute science',
        )

        self.course_1 = Course.objects.create(
            title='backend',
            description='backend with python',
            price=129.90,
            teacher=self.teacher
        )

        self.lesson_1 = Lesson.objects.create(
            title= 'Python basics',
            duration= 60,
            order= 1,
            course= self.course_1
        )

    def test_delete_teacher(self):

        self.assertTrue(
            Teacher.objects.filter(id=self.teacher.id).exists()
        )
        self.assertTrue(
            Course.objects.filter(id=self.course_1.id).exists()
        )
        self.assertTrue(
            Lesson.objects.filter(id=self.lesson_1.id).exists()
        )

        self.teacher.delete()

        self.assertFalse(
            Teacher.objects.filter(id=self.teacher.id).exists()
        )
        self.assertFalse(
            Course.objects.filter(id=self.course_1.id).exists()
        )
        self.assertFalse(
            Lesson.objects.filter(id=self.lesson_1.id).exists()
        )


# RELATED NAME + FILTER
class TeacherCourseBelongsQuantity(TestCase):

    def setUp(self):
        
        self.teacher = Teacher.objects.create(
            name='Benjamin',
            email='ebenja@gmail.com',
            specialty='computer science',
        )

        self.teacher_2 = Teacher.objects.create(
            name='Rodrigo',
            email='rodrigo@gmail.com',
            specialty='pyschology',
        )

        self.course_1 = Course.objects.create(
            title='backend',
            description='backend with python',
            price=129.90,
            teacher=self.teacher
        )
        self.course_2 = Course.objects.create(
            title='devops',
            description='aws for beginner',
            price=209.90,
            teacher=self.teacher
        )
        self.course_3 = Course.objects.create(
            title='cloud computing',
            description='google cloud from scratch',
            price=169.90,
            teacher=self.teacher
        )

        self.course_4 = Course.objects.create(
            title='sesgos cognitivos',
            description='know your limitations',
            price=19.90,
            teacher=self.teacher_2
        )

    def test_course_has_quantity_created(self):

        teacher_courses = self.teacher.courses.all()

        self.assertEqual(teacher_courses.count(), 3)
        self.assertIn(self.course_1, teacher_courses)
        self.assertIn(self.course_2, teacher_courses)
        self.assertIn(self.course_3, teacher_courses)
        self.assertNotIn(self.course_4, teacher_courses)


# AGREGATE 
from django.db.models import Min, Max, Avg

class CoursePriceAggregationTest(TestCase):

    def setUp(self):

        self.teacher = Teacher.objects.create(
            name='Benjamin',
            email='ebenja@gmail.com',
            specialty='computer science',
        )

        self.course_1 = Course.objects.create(
            title='backend',
            description='backend with python',
            price=100,
            teacher=self.teacher
        )
        self.course_2 = Course.objects.create(
            title='devops',
            description='aws for beginner',
            price=200,
            teacher=self.teacher
        )
        self.course_3 = Course.objects.create(
            title='cloud computing',
            description='google cloud from scratch',
            price=300,
            teacher=self.teacher
        )
        self.course_4 = Course.objects.create(
            title='django',
            description='django for beginners',
            price=400,
            teacher=self.teacher
        )

    def test_calculate_min_max_mean(self):

        result = self.teacher.courses.aggregate(
            lowest_price=Min('price'),
            max_price= Max('price'),
            average= Avg('price')
        )

        self.assertEqual(result['lowest_price'], 100)
        self.assertEqual(result['max_price'], 400)
        self.assertEqual(result['average'], 250)