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