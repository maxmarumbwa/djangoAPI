# Serializers are used to convert complex data types, like querysets and model instances, into native Python datatypes.
# They also handle deserialization, converting parsed data back into complex types.
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "url", "name", "language", "price"]
