"""
Dado un laberinto en forma de matriz rectangular, encuentre un camino desde
una fuente dada hasta un destino dado. El camino solo se puede construir a 
partir de celdas que representen un muro y sin salirse de los límites; 
en cualquier momento, solo podemos movernos un paso en una de las cuatro direcciones: Arriba, Derecha, Abajo e Izquierda, es decir, usando una topología de cuatro vecinos y en sentido contrario a las agujas del reloj.
intentando hacer el programa del laberinto
"""
def find_path(lab, x, y, xf, yf, visit, path_f,steps_f, columns, rows):
    if x < 0 or y < 0 or x >= columns or y >= rows: #actual posicion
        return False
    if lab[x][y] == '#' or visit[x][y] == 1: #muro o ya visitada
        return False
    if (x, y) == (xf, yf):      #si es encontrada
        path_f.append((x, y))    
        return True
    
    visit[x][y] = 1          
    path_f.append((x, y))     

    #arriba
    if find_path(lab, x - 1, y, xf, yf, visit,path_f,steps_f,columns,rows): 
        steps_f.append('U')
        return True
    #derecha
    if find_path(lab, x, y + 1, xf, yf, visit,path_f,steps_f,columns,rows): 
        steps_f.append('R')
        return True
    #abajo
    if find_path(lab, x + 1, y, xf, yf, visit,path_f,steps_f,columns,rows): 
        steps_f.append('D')
        return True
    #izquierda
    if find_path(lab, x, y - 1, xf, yf, visit,path_f,steps_f,columns,rows): 
        steps_f.append('L')
        return True
#campos eliminados
    path_f.pop()                  
    if steps_f:
        #pasos eliminados
        steps_f.pop()            
    return False


def OFunction(P, S,arrmov):    
    if S == False:
        if P == 1:
            print(S)
    else:
        if P == 1:
            print(S)                            
        if P == 2:
            print(len(arrmov))
        if P == 3:
            mov = ''.join(arrmov)
            print(mov)

#leyendo las entradas
readinfo = input()
inp = readinfo.split()
info = list(map(int, inp))
R, C = info[0], info[1]         
Sr, Sc = info[2], info[3]      
Tr, Tc = info[4], info[5]       
O = info[6]                 
labyrinth = []             
for a in range(R):
    aux = input()
    labyrinth.append(aux)

#cuerpo de la funcion
visited = [[0 for a in range(C)] for a in range(R)]             
path = []                                                       
steps = []                                                       
if find_path(labyrinth, Sr, Sc, Tr, Tc,visited, path,steps,C,R):   
    Sol = True
    steps.reverse()
    OFunction(O, Sol,steps)
else:                                                            
    Sol = False
    OFunction(O, Sol,steps)