
campus = {

"Sputnik": {"activity": "classes",
            "students access": True,
            "schedule": "6 am to 10 pm",
            "capacity": 35},

"Artemis": {"activity": "classes",
            "students access": True,
            "schedule": "6 am to 10 pm",
            "capacity": 30},

"Apollo": {"activity": "classes",
            "students access": True,
            "schedule": "6 am to 10 pm",
            "capacity": 30},

"Houston": {"activity": "teachers room",
            "students access": False,
            "schedule": "when teachers need",
            "capacity": 6},

"Review": {"activity": "skills review",
            "students access": True,
            "schedule": "24/7",
            "capacity": 100}

}

from paquete.espacio_acceso import  espacios_acceso_campers 
from paquete.menu import menu
from paquete.no_clase import no_hay_horario_clases
from paquete.promedio_clases import promedio_espacios_clase
from paquete.no_entrar import no_estudiar_nunca

menu_de_opciones = menu()
espacio_acceso = espacios_acceso_campers()
tiempo_libre = no_hay_horario_clases()
promedio = promedio_espacios_clase()
no_estudiar = no_estudiar_nunca()