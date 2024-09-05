from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson, Subscription
from materials.paginations import CustomPagination
from materials.serializers import (
    CourseDetailSerializer,
    CourseSerializer,
    LessonSerializer,
)
from users.permissions import IsModer, IsOwner


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer




@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="description from swagger_auto_schema via method_decorator"))
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner | ~IsModer,)

        return super().get_permissions()


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        ~IsModer,
        IsAuthenticated,
    )

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsModer | IsOwner,
    )


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsModer | IsOwner,
    )


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner | ~IsModer,
    )


class SubscriptionView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get("course_id")
        course = get_object_or_404(Course, id=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course)

        if subs_item.exists():

            subs_item.delete()
            message = "Subscription removed"
        else:

            Subscription.objects.create(user=user, course=course)
            message = "Subscription added"

        return Response({"message": message}, status=status.HTTP_200_OK)
