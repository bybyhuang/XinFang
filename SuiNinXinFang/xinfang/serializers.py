from rest_framework import serializers
from .models import Case

class CaseList(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = ('reportName','address')
