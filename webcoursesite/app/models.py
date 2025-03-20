import uuid
from django.db import models


class ModelWithId(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class Person(ModelWithId):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    img = models.ImageField()

    def __str__(self):
        return self.title


class Teacher(Person):
    def __str__(self):
        return self.title


class Mentor(Person):
    def __str__(self):
        return self.title


class Post(ModelWithId):
    title = models.CharField(max_length=50)
    content_url = models.URLField()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class Lab(Post):
    number = models.IntegerField()
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="labs")


class Test(Post):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="tests")


class Schedule(Post):
    course = models.ForeignKey(
        "Course", on_delete=models.CASCADE, related_name="schedules"
    )


class Lectures(ModelWithId):
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
    description = models.TextField()
    statement = models.URLField()
    year = models.IntegerField()

    class Type(models.TextChoices):
        DISTANCE = "distance", "Дистанционный"
        FULLTIME = "full-time", "Очный"

    def __str__(self):
        return self.title


class UsefulPost(Post):
    semester = models.IntegerField()
    description = models.TextField()
    lastUpdate = models.DateField()
    date = models.DateField()
