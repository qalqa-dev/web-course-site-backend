from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        from rest_framework.response import Response

        response = super().list(request, *args, **kwargs)
        if response.data and "results" in response.data:
            return Response(response.data["results"])
        return response


class TeacherViewSet(PersonViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        from rest_framework.response import Response

        response = super().list(request, *args, **kwargs)
        if response.data and "results" in response.data:
            return Response(response.data["results"])
        return response


class MentorViewSet(PersonViewSet):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorSerializer

    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        from rest_framework.response import Response

        response = super().list(request, *args, **kwargs)
        if response.data and "results" in response.data:
            return Response(response.data["results"])
        return response


class UsefulPostViewSet(ModelViewSet):
    queryset = UsefulPost.objects.all()
    serializer_class = UsefulPostSerializer

    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        from rest_framework.response import Response

        response = super().list(request, *args, **kwargs)
        if response.data and "results" in response.data:
            return Response(response.data["results"])
        return response


class LabViewSet(ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class LectureViewSet(ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "name"

    @action(detail=False, methods=["get"])
    def short(self, request):
        courses = self.get_queryset()
        serializer = CourseShortSerializer(courses, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        from rest_framework.response import Response

        response = super().list(request, *args, **kwargs)
        if response.data and "results" in response.data:
            return Response(response.data["results"])
        return response
