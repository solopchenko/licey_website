from app.utils import chunks
from core.models import Organisation, Menu

def organisation(request):
    organisation = Organisation.objects.all().first()
    return {'organisation': organisation}

def menu(request):
    footer_menu_qs = Menu.objects.footer()
    footer_menu = chunks(footer_menu_qs, 3)

    main_menu = Menu.objects.main()

    return {'footer_menu': footer_menu, 'main_menu': main_menu}