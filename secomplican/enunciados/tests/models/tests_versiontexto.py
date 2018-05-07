from django.test import TestCase
from enunciados.models import Materia, Cuatrimestre, ConjuntoDeEnunciados, Enunciado, VersionTextoEnunciado


def agregar_enunciado(conjunto, numero):
    enunciado = Enunciado(conjunto=conjunto, numero=numero, texto='')
    enunciado.save()
    return enunciado


class VersionTextoEnunciadoTests(TestCase):
    def setUp(self):
        materia = Materia(nombre='Materia')
        materia.save()
        cuatrimestre = Cuatrimestre(anio=2018, numero=1)
        cuatrimestre.save()
        conjunto = ConjuntoDeEnunciados(materia=materia, cuatrimestre=cuatrimestre)
        conjunto.save()
        self.enunciado = Enunciado(conjunto=conjunto, numero=1)
        self.enunciado.save()

    def test_ordenamiento(self):
        """Deberían estar ordenados por tiempo de más reciente a menos reciente."""
        self.enunciado.versiones.create(texto='hola')
        self.enunciado.versiones.create(texto='chau')
        self.enunciado.versiones.create(texto='que tal')
        self.enunciado.versiones.create(texto='foobar')

        versiones = self.enunciado.versiones.all()
        for index, version in enumerate(versiones):
            if index < len(versiones) - 1:
                self.assertGreaterEqual(version.tiempo, versiones[index + 1].tiempo)
