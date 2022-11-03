import random
from django.db.models import Max
from bookingWeb.controller import ModelCtr
from bookingWeb.models import Voucher


def get_voucher():
    return ModelCtr.get_all_models(Voucher)

def get_voucher_by_hot_deal():
    try:
        max_id = Voucher.objects.all().aggregate(max_id=Max("id"))['max_id']
        first = Voucher.objects.get(pk=max_id)
        second = Voucher.objects.order_by("?").first()
        return first, second
    except Exception as e:
        print(e)

    return None