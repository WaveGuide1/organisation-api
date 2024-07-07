from rest_framework import serializers
from .models import Organisation


class OrganisationSerializer(serializers.ModelSerializer):
    """
    Serializer for the organisation model
    """

    class Meta:
        model = Organisation
        fields = ['orgId', 'name', 'description']
        read_only_fields = ['orgId', 'users']
