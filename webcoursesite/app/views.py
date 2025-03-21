from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class TeacherViewSet(PersonViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherSerializer


class MentorViewSet(PersonViewSet):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorSerializer


class UsefulPostViewSet(ModelViewSet):
    queryset = UsefulPost.objects.all()
    serializer_class = UsefulPostSerializer


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
