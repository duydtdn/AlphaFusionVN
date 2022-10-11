from AFWeb.models import Client

def get_clients():
    return Client.objects.all()