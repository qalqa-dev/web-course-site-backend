"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from app.views import (
    PersonViewSet,
    TeacherViewSet,
    MentorViewSet,
    UsefulPostViewSet,
    LabViewSet,
    TestViewSet,
    ScheduleViewSet,
    LectureViewSet,
    CourseViewSet
)

router = DefaultRouter()

router.register(r"api/people", PersonViewSet, basename="people")
router.register(r"api/teachers", TeacherViewSet, basename="teachers")
router.register(r"api/mentors", MentorViewSet, basename="mentors")
router.register(r"api/useful", UsefulPostViewSet, basename="useful")
router.register(r"api/labs", LabViewSet, basename="labs")
router.register(r"api/tests", TestViewSet, basename="tests")
router.register(r"api/schedule", ScheduleViewSet, basename="schedule")
router.register(r"api/lectures", LectureViewSet, basename="lectures")
router.register(r"api/courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("admin/", admin.site.urls),
] + router.urls
