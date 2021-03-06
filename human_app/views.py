from rest_framework import viewsets
from rest_framework.parsers import JSONParser

import human_app.models as models
import human_app.serializers as serializers
from human_app.utils import MultipartJsonParser


class HumansViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HumanSerializer
    parser_classes = (MultipartJsonParser, JSONParser)
    queryset = models.Human.objects.all().order_by('id')
    lookup_field = 'id'

