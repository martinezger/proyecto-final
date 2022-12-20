from ejemplo_dos.models import WebSiteSetup


def add_variable_to_context(request):
    web_site_setup = WebSiteSetup.objects.first()
    context = {}
    if web_site_setup:
        context = {
            "titulo_site": web_site_setup.titulo,
            "sub_titulo_site": web_site_setup.sub_titulo,
        }
    return context