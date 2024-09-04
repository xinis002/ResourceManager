from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.course = Course.objects.create(name="Course", owner=self.user)
        self.lesson = Lesson.objects.create(name="Test Lesson", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)
        self.video_url = "https://www.youtube.com/watch?v=123"

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name
        )

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            'name': 'Updated Lesson',
            'course': self.course.pk,
            'video': self.video_url
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'Updated Lesson')

    def test_lesson_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertGreaterEqual(len(data['results']), 1)
        self.assertEqual(data['results'][0]['name'], self.lesson.name)

    def test_lesson_destroy(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


        with self.assertRaises(Lesson.DoesNotExist):
            Lesson.objects.get(pk=self.lesson.pk)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="user@example.com", password="password")
        self.course = Course.objects.create(name="Test Course", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_creation(self):
        url = reverse("materials:subscription")
        data = {
            'course_id': self.course.id,
        }
        response = self.client.post(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Subscription added')


        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_subscription_removal(self):

        Subscription.objects.create(user=self.user, course=self.course)

        url = reverse("materials:subscription")
        data = {
            'course_id': self.course.id,
        }
        response = self.client.post(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Subscription removed')


        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_invalid_course_id(self):
        url = reverse("materials:subscription")
        data = {
            'course_id': 999,
        }
        response = self.client.post(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)