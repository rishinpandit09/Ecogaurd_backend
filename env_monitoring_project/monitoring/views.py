from rest_framework import viewsets
from rest_framework.decorators import action

from .models import MonitoringStation, Alert
from .serializers import MonitoringStationSerializer, AlertSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ai_models.model_inference import make_prediction



class MonitoringStationViewSet(viewsets.ModelViewSet):
    queryset = MonitoringStation.objects.all()
    serializer_class = MonitoringStationSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AIModelViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def predict(self, request):
        """
        Custom action to handle predictions from the AI model.
        """
        input_data = request.data.get("input_data")
        if not input_data:
            return Response({"error": "No input data provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            predictions = make_prediction(input_data)
            return Response({"predictions": predictions}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
