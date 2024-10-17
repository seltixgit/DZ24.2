from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateAPIView,
                             LessonDestroyAPIView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateAPIView,
                             SubscriptionCreateAPIView)

app_name = MaterialsConfig.name


router = SimpleRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path("lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("course_subscription/", SubscriptionCreateAPIView.as_view(), name="course_subscription"),
] + router.urls
