from ejemplo.models import Familiar

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()


from ejemplo_dos.models import Post

Post(titulo="Un post", sub_titulo="un sub post", texto="Un comentario", publicado_el="12/12/2022")


print("Se cargo con éxito los usuarios de pruebas")