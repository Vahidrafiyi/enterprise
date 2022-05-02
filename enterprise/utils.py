import datetime

from information.models import Visit


def visit():
    today = datetime.date.today()
    query = Visit.objects.get_or_create(date=today)
    query[0].number += 1
    query[0].save()
