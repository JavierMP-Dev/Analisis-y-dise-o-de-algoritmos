def emparejamiento_estable(preferencias_hombres, preferencias_mujeres):
    # Diccionario para almacenar las parejas de mujeres con sus parejas hombres
    comprometidos_con = {}
    hombres_libres = list(preferencias_hombres.keys())  # Hombres que aún no están emparejados
    propuestas = {hombre: 0 for hombre in preferencias_hombres}  # Número de propuestas realizadas por cada hombre

    # Mientras haya hombres solteros
    while hombres_libres:
        hombre = hombres_libres[0]  # Elige al primer hombre libre
        lista_preferencias_hombre = preferencias_hombres[hombre]
        mujer = lista_preferencias_hombre[propuestas[hombre]]  # Elige la primera mujer a la que aún no ha propuesto
        propuestas[hombre] += 1  # se Incrementa el número de propuestas hechas por este hombre

        if mujer not in comprometidos_con:  # Si la mujer no está comprometida
            comprometidos_con[mujer] = hombre  # Se comprometen
            hombres_libres.pop(0)  # borra al hombre de la lista de libres

        else:  # Si la mujer ya está comprometida
            pareja_actual = comprometidos_con[mujer]
            # Verifica si prefiere al nuevo hombre en lugar de su pareja actual
            if preferencias_mujeres[mujer].index(hombre) < preferencias_mujeres[mujer].index(pareja_actual):
                comprometidos_con[mujer] = hombre  # Cambia de pareja
                hombres_libres.pop(0)  # El nuevo hombre ahora está comprometido
                hombres_libres.append(pareja_actual)  # El antiguo hombre vuelve a estar soltero

    return comprometidos_con

# Ejemplo de uso
preferencias_hombres = {
    'Hombre1': ['M1', 'M2', 'M3'],
    'Hombre2': ['M2', 'M3', 'M1'],
    'Hombre3': ['M3', 'M1', 'M2']
}
#lista de mujeres 
preferencias_mujeres = {
    'Mujer1': ['H1', 'H2', 'H3'],
    'Mujer2': ['H2', 'H1', 'H3'],
    'Mujer3': ['H3', 'H2', 'H1']
}

parejas = emparejamiento_estable(preferencias_hombres, preferencias_mujeres)

print("Parejas emparejadas:")
for mujer, hombre in parejas.items():
    print(f"{mujer} está emparejada con {hombre}")
