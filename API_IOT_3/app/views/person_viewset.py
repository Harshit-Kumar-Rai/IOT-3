from rest_framework import viewsets
from app.models.person_model import Person
from app.serializers.person_serializer import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer