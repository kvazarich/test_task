from rest_framework import viewsets

import match_app.models as models
import match_app.serializers as serializers


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Match.objects.all().order_by('human')
    serializer_class = serializers.MatchSerializer

