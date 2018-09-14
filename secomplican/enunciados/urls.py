from django.urls import path, register_converter

from enunciados.views import index, materias, conjuntos_de_enunciados, practicas
from enunciados.views.enunciados import ver as ver_enunciados
from enunciados.views.enunciados import crear as crear_enunciado
from enunciados.views.enunciados import editar as editar_enunciado
from enunciados.views.enunciados import versiones as versiones_enunciado
from enunciados.views.soluciones import crear as crear_solucion
from enunciados.views.soluciones import editar as editar_solucion
from enunciados.views.soluciones import versiones as versiones_solucion
from enunciados.url_converters.materiacarrera_converter import MateriaCarreraConverter


register_converter(MateriaCarreraConverter, 'materiacarrera')


urlpatterns = [
    path('', index.index, name='index'),
    path('materias/', materias.MateriasView.as_view(), name='materias'),

    path(
        'nuevo-ejercicio/',
        crear_enunciado.nuevo_enunciado,
        name='agregar_enunciado'
    ),

    path('<materiacarrera:materia_carrera>/', materias.materia, name='materia'),
    path('<slug:materia>/practicas/', practicas.practicas, name='practicas'),
    path('<slug:materia>/practicas/<int:anio>/<cuatrimestre>/<int:numero>/',
         conjuntos_de_enunciados.practica, name='practica'),
    path('<slug:materia>/parciales/<int:anio>/<cuatrimestre>/<int:numero>/',
         conjuntos_de_enunciados.parcial, name='parcial'),
    path('<slug:materia>/recuperatorios/<int:anio>/<cuatrimestre>/<int:numero>/',
         conjuntos_de_enunciados.parcial, {'recuperatorio': True},
         name='recuperatorio'),
    path('<slug:materia>/finales/<int:anio>/<int:mes>/<int:dia>/',
         conjuntos_de_enunciados.final, name='final'),

    # Enunciados
    path(
        '<slug:materia>/practicas/<int:anio>/<cuatrimestre>/<int:numero_practica>/<int:numero>/',
        ver_enunciados.enunciado_practica,
        name='enunciado_practica'
    ),
    path(
        '<slug:materia>/parciales/<int:anio>/<cuatrimestre>/<int:numero_parcial>/<int:numero>/',
        ver_enunciados.enunciado_parcial,
        {'es_recuperatorio': False},
        name='enunciado_parcial'
    ),
    path(
        '<slug:materia>/recuperatorios/<int:anio>/<cuatrimestre>/<int:numero_parcial>/<int:numero>/',
        ver_enunciados.enunciado_parcial,
        {'es_recuperatorio': True},
        name='enunciado_recuperatorio'
    ),
    path(
        '<slug:materia>/finales/<int:anio>/<int:mes>/<int:dia>/<int:numero>/',
        ver_enunciados.enunciado_final,
        name='enunciado_final'
    ),

    # Editar
    path(
        '<slug:materia>/practicas/<int:anio>/<cuatrimestre>/'
        '<int:numero_practica>/<int:numero>/editar/',
        editar_enunciado.enunciado_practica,
        name='editar_enunciado_practica'
    ),
    path(
        '<slug:materia>/parciales/<int:anio>/<cuatrimestre>/'
        '<int:numero_parcial>/<int:numero>/editar/',
        editar_enunciado.enunciado_parcial,
        {'es_recuperatorio': False},
        name='editar_enunciado_parcial'
    ),
    path(
        '<slug:materia>/recuperatorios/<int:anio>/<cuatrimestre>/'
        '<int:numero_parcial>/<int:numero>/editar/',
        editar_enunciado.enunciado_parcial,
        {'es_recuperatorio': True},
        name='editar_enunciado_recuperatorio'
    ),
    path(
        '<slug:materia>/finales/<int:anio>/<int:mes>/<int:dia>/'
        '<int:numero>/editar',
        editar_enunciado.enunciado_final,
        name='editar_enunciado_final'
    ),

    # Versiones
    path(
        '<slug:materia>/practicas/<int:anio>/<cuatrimestre>/'
        '<int:numero_practica>/<int:numero>/versiones/',
        versiones_enunciado.VersionesEnunciadoView.as_view(),
        {'conjunto': 'practica'},
        name='versiones_enunciado_practica'
    ),
    path(
        '<slug:materia>/parciales/<int:anio>/<cuatrimestre>/'
        '<int:numero_parcial>/<int:numero>/versiones/',
        versiones_enunciado.VersionesEnunciadoView.as_view(),
        {
            'conjunto': 'parcial',
            'es_recuperatorio': False,
        },
        name='versiones_enunciado_parcial'
    ),
    path(
        '<slug:materia>/recuperatorios/<int:anio>/<cuatrimestre>/'
        '<int:numero_parcial>/<int:numero>/versiones/',
        versiones_enunciado.VersionesEnunciadoView.as_view(),
        {
            'conjunto': 'parcial',
            'es_recuperatorio': True,
        },
        name='versiones_enunciado_recuperatorio'
    ),
    path(
        '<slug:materia>/finales/<int:anio>/<int:mes>/<int:dia>/'
        '<int:numero>/versiones',
        versiones_enunciado.VersionesEnunciadoView.as_view(),
        {'conjunto': 'final'},
        name='versiones_enunciado_final'
    ),

    # Soluciones
    path(
        '<slug:materia>/practicas/<int:anio>/<cuatrimestre>/<int:numero_practica>/<int:numero>/nueva-solucion/',
        crear_solucion.CrearSolucion.as_view(),
        name='solucion_practica'
    ),
    path(
        '<slug:materia>/parciales/<int:anio>/<cuatrimestre>/<int:numero_parcial>/<int:numero>/nueva-solucion/',
        crear_solucion.CrearSolucion.as_view(),
        {'es_recuperatorio': False},
        name='solucion_parcial'
    ),
    path(
        '<slug:materia>/recuperatorios/<int:anio>/<cuatrimestre>/<int:numero_parcial>/<int:numero>/nueva-solucion/',
        crear_solucion.CrearSolucion.as_view(),
        {'es_recuperatorio': True},
        name='solucion_recuperatorio'
    ),
    path(
        '<slug:materia>/finales/<int:anio>/<int:mes>/<int:dia>/<int:numero>/nueva-solucion/',
        crear_solucion.CrearSolucion.as_view(),
        name='solucion_final'
    ),

    path(
        'soluciones/<int:pk>/editar/',
        editar_solucion.editar_solucion,
        name='editar_solucion'
    ),

    path(
        'soluciones/<int:pk>/versiones/',
        versiones_solucion.VersionesSolucionView.as_view(),
        name='versiones_solucion'
    ),
]
