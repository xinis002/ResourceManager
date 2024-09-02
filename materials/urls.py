from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import (
    LessonViewSet,
    CourseViewSet,
    LessonCreateApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView,
    LessonDestroyApiView,
)
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name


router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lesson_list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_detail"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path(
        "lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"
    ),
    path(
        "lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson_delete"
    ),
]

urlpatterns += router.urls
