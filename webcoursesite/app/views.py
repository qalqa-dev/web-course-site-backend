from rest_framework.viewsets import ModelViewSet
from .models import Person, UsefulPost
from .serializers import PersonSerializer, UsefulPostSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class UsefulPostViewSet(ModelViewSet):
    queryset = UsefulPost.objects.all()
    serializer_class = UsefulPostSerializer
