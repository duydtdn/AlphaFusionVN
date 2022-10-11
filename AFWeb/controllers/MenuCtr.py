from AFWeb.models import Menu

def get_menu():
    return Menu.objects.all()