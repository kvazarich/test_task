from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

import match_app.models as models
import match_app.serializers as serializers


from rest_framework.response import Response


class MatchViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = models.Match.objects.all()
        serializer = serializers.MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.Match.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.MatchSerializer(user)
        return Response(serializer.data)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context