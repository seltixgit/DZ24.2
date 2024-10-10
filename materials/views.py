from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import (CourseDetailSerializer, CourseSerializer,
                                   LessonSerializer)

from users.permissions import IsModer, IsOwner


class CourseViewSet(ModelViewSet):

    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner,)
        if self.action == 'destroy':
            self.permission_classes = (~IsModer | IsOwner,)
        return super().get_permissions()


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
