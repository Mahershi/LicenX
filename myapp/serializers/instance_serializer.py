from rest_framework.serializers import ModelSerializer
from ..models import Instance


class InstanceSerializer(ModelSerializer):
    class Meta:
        model = Instance
        fields = '__all__'
