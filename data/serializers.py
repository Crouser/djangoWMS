from rest_framework_json_api import serializers
from data.models import Data

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('temperature', 'pressure','dateTime')

