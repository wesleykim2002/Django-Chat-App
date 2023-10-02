from rest_framework import serializers

class StatusSerializer(serializers.Serializer):
    type = serializers.CharField()
    status_colour = serializers.CharField()
    status = serializers.CharField()
    action_text = serializers.CharField()


class KeepAliveSerializer(serializers.Serializer):
    type = serializers.CharField()
    keep_alive = serializers.CharField()
