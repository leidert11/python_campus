from diccionario import campus

def espacios_acceso_campers():
    for i in campus:
        if campus[i]["students access"] == True:
            print("------------------------------------")
            print(i)
    return i        
            