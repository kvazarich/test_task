from django.http import JsonResponse

import match_app.models as models
import match_app.serializers as serializers


def match_list(request):
    if request.method == 'GET':
        matches = models.Match.objects.all()
        serializer = serializers.MatchSerializer(matches, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse(status=404)


def match_detail(request, pk):
    try:
        human = models.Human.objects.get(pk=pk)
    except models.Human.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        match = models.Match.objects.get(human=human)
        serializer = serializers.MatchSerializer(match)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse(status=404)
