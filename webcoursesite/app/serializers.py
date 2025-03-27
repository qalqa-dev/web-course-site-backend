from rest_framework import serializers
from .models import (
    Person,
    TeacherProfile,
    MentorProfile,
    UsefulPost,
    Lab,
    Test,
    Schedule,
    Lecture,
    Course,
)


class PersonSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = [
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "contact",
            "role",
            "img_url",
            "is_teacher",
            "is_mentor",
        ]

    def get_img_url(self, obj):
        base_url = "http://localhost:9000/photos/"
        return f"{base_url}{obj.contact}.webp"


class TeacherSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="person.id")
    first_name = serializers.CharField(source="person.first_name")
    middle_name = serializers.CharField(source="person.middle_name")
    last_name = serializers.CharField(source="person.last_name")
    contact = serializers.CharField(source="person.contact")
    role = serializers.CharField(source="person.role")
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = TeacherProfile
        fields = [
            "id",
            "last_name",
            "first_name",
            "middle_name",
            "contact",
            "role",
            "img_url",
        ]

    def get_img_url(self, obj):
        base_url = "http://localhost:9000/photos/"
        return f"{base_url}{obj.person.contact}.webp"


class MentorSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="person.id")
    first_name = serializers.CharField(source="person.first_name")
    middle_name = serializers.CharField(source="person.middle_name")
    last_name = serializers.CharField(source="person.last_name")
    contact = serializers.CharField(source="person.contact")
    role = serializers.CharField(source="person.role")
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = MentorProfile
        fields = [
            "id",
            "last_name",
            "first_name",
            "middle_name",
            "contact",
            "role",
            "img_url",
        ]

    def get_img_url(self, obj):
        base_url = "http://localhost:9000/photos/"
        return f"{base_url}{obj.person.contact}.webp"


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ["id", "title", "content_url"]
        abstract = True


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = [
            "id",
            "name",
            "title",
            "number",
            "content_url",
        ]


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        exclude = ["course"]


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        exclude = ["course"]


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(many=True, read_only=True)
    labs = LabSerializer(many=True, read_only=True)
    tests = TestSerializer(many=True, read_only=True)
    schedule = ScheduleSerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "title",
            "type",
            "description",
            "statement",
            "year",
            "lectures",
            "schedule",
            "labs",
            "tests",
        ]


class CourseShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "name", "description"]


class UsefulPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsefulPost
        fields = "__all__"
