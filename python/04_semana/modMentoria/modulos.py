# calcular la edad de una persona
import datetime


def fechaEnLista():
    anio_actual = datetime.datetime.now().year
    mes_actual = datetime.datetime.now().month
    dia_actual = datetime.datetime.now().day
    return [anio_actual, mes_actual, dia_actual]
