from diccionario import campus


def no_hay_horario_clases():
    for i in campus:
        if campus[i]["schedule"] != "6 am to 10 pm" and campus[i]["students access"] != False:
            print("------------------------------------")
            print(i)