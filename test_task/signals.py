import django.dispatch
human_post_save = django.dispatch.Signal(providing_args=['pk'])
human_pre_delete = django.dispatch.Signal(providing_args=['pk'])
