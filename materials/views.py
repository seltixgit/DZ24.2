from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import action
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson, Subscription
from materials.paginations import CustomPagination
from materials.serializers import (CourseDetailSerializer, CourseSerializer,
                                   LessonSerializer, SubscriptionSerializer)
from materials.tasks import course_update
from users.permissions import IsModer, IsOwner


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
        if self.action == "destroy":
            self.permission_classes = (~IsModer | IsOwner,)
        return super().get_permissions()

    def perform_update(self, serializer):
        instance = serializer.save()
        course_update.delay(instance.id)
        return instance


class LessonCreateAPIView(CreateAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModer, IsAuthenticated)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveAPIView(RetrieveAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModer | IsOwner, IsAuthenticated)


class LessonUpdateAPIView(UpdateAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModer | IsOwner, IsAuthenticated)


class LessonDestroyAPIView(DestroyAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModer | IsOwner, IsAuthenticated)


class SubscriptionCreateAPIView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)
        if subs_item.exists():
            subs_item.delete()  # Удаляем подписку
            message = "подписка удалена"
        else:
            Subscription.objects.create(
                user=user, course=course_item, sign_of_subscription=True
            )  # Создаем подписку
            message = "подписка добавлена"
        return Response({"message": message})
