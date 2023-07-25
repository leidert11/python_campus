from diccionario import campus

def promedio_espacios_clase():
    
    acumulador_sputnik=0
    
    contador_sputnik=0
    
    for i in campus:
        if campus[i]["activity"] == 'classes':
            acumulador_sputnik += campus[i]["capacity"]
            contador_sputnik += 1
            
    print("------------------------------------")
    print(f"El promedio es: {acumulador_sputnik/contador_sputnik}") 