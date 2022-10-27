from django.shortcuts import render

# Create your views here.
def index(request):
    # first, second = get_voucher_by_hot_deal()
    return render(request, '../templates/index.html',
                  {'places': get_places(), 'banners': get_banner(), 'vouchers_first': first, 'voucher_second': second})