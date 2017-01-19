from django.conf import settings
from datetime import datetime
from django.utils import timezone

def chunks(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
from datetime import datetime


def get_now():
    if settings.USE_TZ:
        return datetime.utcnow().replace(tzinfo=timezone.utc)
    else:
        return datetime.now()

def user_is_group_member(user, group_name):
    return user.groups.filter(name=group_name).exists()