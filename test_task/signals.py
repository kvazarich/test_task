import django.dispatch
human_created = django.dispatch.Signal(providing_args=['pk'])
human_deleted = django.dispatch.Signal(providing_args=['pk'])
