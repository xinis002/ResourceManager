from rest_framework.serializers import ModelSerializer, SerializerMethodField
from materials.models import Lesson, Course


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"




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



