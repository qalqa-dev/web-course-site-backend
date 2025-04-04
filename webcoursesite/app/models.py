import uuid
from django.db import models


class ModelWithId(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class Person(ModelWithId):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    contact = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    @property
    def is_teacher(self):
        return self.teachers.count() > 0

    @property
    def is_mentor(self):
        return self.mentors.count() > 0

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class TeacherProfile(ModelWithId):
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, related_name="teacher_profile"
    )

    def __str__(self):
        if not self.person:
            return
        return f"{self.person.first_name} {self.person.last_name} {self.person.middle_name}"


class MentorProfile(ModelWithId):
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, related_name="mentor_profile"
    )

    def __str__(self):
        return (
            self.person.first_name
            + " "
            + self.person.last_name
            + " "
            + self.person.middle_name
        )


class Post(ModelWithId):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content_url = models.URLField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class Lab(Post):
    number = models.IntegerField()
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="labs")

    def __str__(self):
        return f"({self.course}) - {self.title}"


class Test(Post):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="tests")

    def __str__(self):
        return self.title


class Schedule(Post):
    course = models.OneToOneField(
        "Course", on_delete=models.CASCADE, related_name="schedule"
    )

    def __str__(self):
        return f"План - {self.course} "


class Lecture(ModelWithId):
    title = models.CharField(max_length=50)
    description = models.JSONField()
    href = models.URLField()
    course = models.ForeignKey(
        "Course", on_delete=models.CASCADE, related_name="lectures"
    )

    def __str__(self):
        return self.title


class Course(ModelWithId):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    statement = models.URLField(blank=True)
    year = models.IntegerField()

    class Type(models.TextChoices):
        DISTANCE = "distance", "Дистанционный"
        FULLTIME = "full-time", "Очный"

    type = models.CharField(max_length=10, choices=Type.choices, default=Type.FULLTIME)

    def __str__(self):
        return f"{self.title}{' - ' + self.get_type_display() if self.type == self.Type.DISTANCE else ''}"


class UsefulPost(Post):
    semester = models.IntegerField()
    description = models.TextField()
    lastUpdate = models.DateField()
    date = models.DateField()

    def __str__(self):
        return str(self.title)
