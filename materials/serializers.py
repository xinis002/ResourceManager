from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import YouTubeURLValidator


class LessonSerializer(ModelSerializer):
    video = serializers.CharField(validators=[YouTubeURLValidator()])

    class Meta:
        model = Lesson
        fields = ["id", "name", "course", "owner", "video"]
        read_only_fields = ["owner"]


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lesson_with_same_course = SerializerMethodField()

    def get_count_lesson_with_same_course(self, lesson):
        return Lesson.objects.filter(course=lesson.course).count()

    class Meta:
        model = Course
        fields = ("name", "description", "count_lesson_with_same_course")


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["user", "course", "subscribed_at"]
        read_only_fields = ["subscribed_at"]
