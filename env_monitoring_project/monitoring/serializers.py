from django.contrib.gis.geos import Point
from rest_framework import serializers
from .models import MonitoringStation, Alert
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class MonitoringStationSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()

    class Meta:
        model = MonitoringStation
        fields = ['id', 'name', 'location', 'country', 'description']

    def get_location(self, obj):
        """
        Converts a Point object to GeoJSON format.
        """
        if obj.location and isinstance(obj.location, Point):
            return {
                "type": "Point",
                "coordinates": [obj.location.x, obj.location.y]  # Longitude, Latitude
            }
        return None

    def create(self, validated_data):
        # Convert GeoJSON to Point object
        location_data = self.initial_data.get('location')
        if location_data and 'coordinates' in location_data:
            point = Point(location_data['coordinates'][0], location_data['coordinates'][1])
            validated_data['location'] = point
        return super().create(validated_data)

    def update(self, instance, validated_data):
        location_data = self.initial_data.get('location')
        if location_data and 'coordinates' in location_data:
            instance.location = Point(location_data['coordinates'][0], location_data['coordinates'][1])
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)  # Update country
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'title', 'location', 'date', 'alert_type')