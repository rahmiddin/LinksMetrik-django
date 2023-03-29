from rest_framework import serializers


class DomainSerializer(serializers.Serializer):
    domains = serializers.ListField()
    status = serializers.CharField()
