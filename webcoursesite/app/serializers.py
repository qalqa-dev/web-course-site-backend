from rest_framework import serializers
from .models import (
    Person,
    Teacher,
    Mentor,
    UsefulPost,
    Lab,
    Test,
    Schedule,
    Lecture,
    Course,
)


class PersonSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = [
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "contact",
            "role",
            "imgUrl",
        ]

    def get_imgUrl(self, obj):
        base_url = "http://localhost:9000/photos/"
        return f"{base_url}{obj.contact}.webp"


class TeacherSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        model = Teacher


class MentorSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        model = Mentor


class PostSerializer(serializers.ModelSerializer):
    contentFile = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        abstract = True

    def get_contentFile(self, obj):
        base_url = "http://localhost:9000/files/"
        return f"{base_url}{obj.content_url}"


class LabSerializer(PostSerializer):
    class Meta:
        model = Lab
        fields = "__all__"


class TestSerializer(PostSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class ScheduleSerializer(PostSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(many=True, read_only=True)
    labs = LabSerializer(many=True, read_only=True)
    tests = TestSerializer(many=True, read_only=True)
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class UsefulPostSerializer(serializers.ModelSerializer):
    contentFile = serializers.SerializerMethodField()

    class Meta:
        model = UsefulPost
        fields = "__all__"

    def get_contentFile(self, obj):
        base_url = "http://localhost:9000/useful/"
        return f"{base_url}{obj.content_url}"
