#Matriz original
#almacen = [
#[0, 0, 0, 1, 0], # 0 = espacio vacío, 1 = obstáculo
#[0, 2, 0, 1, 3], # 2 = posición del robot, 3 = paquete
#[0, 0, 0, 0, 0],
#[1, 1, 0, 1, 0],
#[0, 0, 0, 0, 4] # 4 = zona de entrega
#]

#Matriz de mafer
almacen = [
    [0, 2, 0, 0, 1], # 0 = espacio vacío
    [0, 1, 0, 1, 0], # 1 = obstáculo
    [0, 0, 3, 1, 0], # 2 = posición del robot
    [1, 0, 0, 0, 0], # 3 = paquete
    [0, 1, 0, 1, 4]  # 4 = zona de entrega
]

inicio = [0,1] #Esta es la posicion inicial del robot [fila, columna]
zona_entrega = [4,4] #Esta es la posicion de la zona de entrega [fila, columna]

#Funciones para mover al robot

#Esta funcion es para q el robot busque el camino, recibe destino pq sirve para paquete y zona_entrega
def buscar_camino(inicio, destino, almacen):

    #Inicializamos la cola
    #Guardamos una lista q contiene: [posicion actual, [camino recorrido]]
    cola = [[inicio, [inicio]]]

    #las casillas visitadas seran una lista, otra vez
    visitado = [inicio]

    #MIENTRAS la cola este ocupada / NO este vacia
    while len(cola) > 0:

        #DESENCOLAMOS, sacamos el primer elemento de la lista
        actual, camino = cola.pop(0) #Aca le decimos a cola q saque el primer elemento (acuerdate q aca se empieza desde 0)

        #SI llegamos al destino (zona_entrega) entonces retornamos el camino
        if actual == destino:
            return camino

        #Desarmamos la posicion actual [fila, columna]
        fila, columna = actual

        #Definimos los 4 movimientos posibles: arriba, abajo, izquierda, derecha
        #(cambios en la fila, cambios en la columna)
        movimientos = [(-1,0), (1,0), (0,-1), (0,1)]
        for df, dc in movimientos:
            nueva_fila = fila + df
            nueva_columna = columna + dc

            #Validamos q el robot NO se salga de los limites de la matriz
            if 0 <= nueva_fila < 5 and 0 <= nueva_columna < 5:

                #Validamos q NO sea un obstaculo (1) y q NO hayamos visitado esa casilla antes
                if almacen[nueva_fila][nueva_columna] != 1 and [nueva_fila, nueva_columna] not in visitado:
                    #Si la casilla esta limpia, la marcamos como visitada
                    visitado.append([nueva_fila, nueva_columna])

                    #La metemos a la cola para despues validarla y sumandola al camino del robot
                    cola.append([[nueva_fila, nueva_columna], camino + [[nueva_fila, nueva_columna]]])

    #Si el bucle no encontro nada, retornamos nulo / 0
    return None

#Esta funcion es para q el robot busque el paquete
def buscar_paquete(almacen):
    #Recorremos cada fila usando el indice [0 a 4]
    for fila in range(len(almacen)):

        #Ahora recorremos cada columna usando el mismo indice [0 a 4]
        for columna in range (len(almacen[fila])):

            #Si el elemento q encuentra el robot es = 3, entonces....
            if almacen[fila][columna] == 3:

                #Retornamos la posicion como una lista
                return [fila, columna] #posicion de donde se encuentra el paquete

    #Si no encuentra el paquete, devolvemos None (Valor vacio o nulo)
    return None

#Esta funcion es para q se mueva el robot
def mover_robot(almacen, camino):
    #Validamos q haya camino
    if camino is None:
        print("No hay camino valido para q el robot se mueva")
        return
    
    print("\n--- ¡INICIANDO MOVIMIENTO DEL ROBOT! ---")
    #Recorremos cada coordenada [fila, columna] dentro de la lista "camino"
    for paso in camino:

        #1- Buscamos donde estaba el robot antes para marcar su posicion ACTUAL como 0
        for fila in range(len(almacen)):
            for columna in range(len(almacen[fila])):
                if almacen[fila][columna] == 2:
                    #Aqui reiniciamos la posicion del robot
                    almacen[fila][columna] = 0
        
        #2- Ahora le pasamos la nueva coordenada al robot
        nueva_fila = paso[0]
        nueva_columna = paso[1]
        #Nueva coordenada:
        almacen[nueva_fila][nueva_columna] = 2

        # 3. Imprimimos el mapa para ver cómo se movió en este paso
        print(f"\nPosicion actual del robot: {paso}")
        for fila in almacen:
            print(fila)

#Esta funcion es para q el robot recoja el paquete, reemplazaremos el 3 por un 0
def recoger_paquete(almacen, posicion_paquete):
    fila = posicion_paquete[0]
    columna = posicion_paquete[1]
    #El paquete pasa a 0 pq el robot se lo llevo
    almacen[fila][columna] = 0

#Funcion Principal
def funcion_principal(almacen, inicio):
    # Buscamos si hay un paquete en el almacén para empezar
    pos_paquete = buscar_paquete(almacen)
    
    # MIENTRAS encontremos un paquete (es decir, pos_paquete NO sea None)
    while pos_paquete is not None:
        
        #Calculamos ruta desde el inicio hasta el paquete
        camino_a_paquete = buscar_camino(inicio, pos_paquete, almacen)
        
        if camino_a_paquete is not None:
            # Movemos al robot por el camino al paquete
            mover_robot(almacen, camino_a_paquete)
            
            # El robot recoge el paquete en esa posición
            recoger_paquete(almacen, pos_paquete)
            
            # Actualizamos la posicion inicial del robot
            inicio = pos_paquete
        else:
            print("No se encontró un camino seguro hacia el paquete.")
            return

        # Calculamos ruta desde la posicion actual hasta la zona de entrega
        camino_a_entrega = buscar_camino(inicio, zona_entrega, almacen)
        
        if camino_a_entrega is not None:
            # Movemos al robot a dejar el paquete
            mover_robot(almacen, camino_a_entrega)
            
            # Ahora el robot está en la zona de entrega, actualizamos su inicio ahí
            inicio = zona_entrega
        else:
            print("No se encontró un camino seguro hacia la zona de entrega.")
            return
        
        # 3. ESCANEO DE REPETICIÓN: Volvemos a buscar si queda otro paquete (punto 5 de la pauta)
        pos_paquete = buscar_paquete(almacen)
        
    print("\n¡Proceso terminado! Todos los paquetes fueron entregados con éxito.")

#Prints
funcion_principal(almacen, inicio)