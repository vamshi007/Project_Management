from django.http import HttpResponse
from rest_framework import serializers
from .models import ProjectStateModel

class ProjectStateSerializers(serializers.ModelSerializer):


    class Meta:
        model = ProjectStateModel
        fields = "__all__"

    def validate_project_name(self, value):
        if len(value) > 3:
            return value
        else:
            raise serializers.ValidationError('at-least 3 characters')