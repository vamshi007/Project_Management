from rest_framework import viewsets
from .models import  ProjectStateModel
from .serializers import ProjectStateSerializers
# Create your views here.

class ProjectStateViewSets(viewsets.ModelViewSet):
    queryset=ProjectStateModel.objects.all()
    serializer_class=ProjectStateSerializers

