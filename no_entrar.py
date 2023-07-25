from diccionario import campus


def no_estudiar_nunca():
    for i in campus:
        if campus[i]["activity"] == "teachers room" and campus[i]["students access"] == False:
            print("------------------------------------")
            print(i)