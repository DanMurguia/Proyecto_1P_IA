import pygame
import random
import genera_matriz as gm
import agente as ag
import time
import Nodo

BLACK = (0, 0, 0)
water = (0, 0, 255)
forest = (6, 71, 12)
redP = (230, 0, 20)
pinkP = (255, 77, 195)
mountains = (160, 160, 160)
aquaP = (90, 139, 185)
sand = (194, 178, 128)
pantano = (102, 0, 102)
nieve = (255, 255, 255)
land = (181, 101, 29)



# tamañoCasilla es el tamaño que tendrá cada lado de las casillas
tamañoCasilla = 40

# tamañoCuadricula es el numero de casillas que tendrá la cuadricula por lado
tamañoCuadricula = 15
columna = 0

'''def dibujar(agente,algoritmo,modo,xinicial,yinicial,xfinal,yfinal):
    if algoritmo == 3:
        dibujar_estrella(agente,xinicial,yinicial,xfinal,yfinal)'''

def dibujar():
    pygame.init()
    costo=0
    costoAcumulado=0
    objetivos_humano =[]
    objetivos_mono =[]
    objetivos_pulpo =[]
    contf = 0

    # tamañoPantalla es el una tupla con los valores del tamaño de la pantalla
    tamañoPantalla = (tamañoCasilla*tamañoCuadricula,
                      tamañoCasilla*tamañoCuadricula)

    # pantall es la pantalla a desplegar
    pantalla = pygame.display.set_mode(tamañoPantalla)

    # se le da un titulo a la ventana a desplegar
    pygame.display.set_caption("Grid on PYGAME")

    # reloj es un timer que indica la velocidad de actualización de la pantalla
    reloj = pygame.time.Clock()

    # gameOver el el indicador de querer cerrar la pantalla
    gameOver = False

    # Fuente es un estilo de imagen inicializada dentro de pygame. Pygame solo muestra imagenes o dibujos, no texto.
    Fuente = pygame.font.SysFont('fontname', 16)
    matriz = gm.cargar_matriz('mapa_proyecto.txt')
    fil = matriz.shape[0]
    col = matriz.shape[1]
    params_humano = {}           #Se crea el diccionario de parametros
    params_mono = {}
    params_pulpo = {}


    for i in range(0, fil):
        for j in range(0, col):
            params_humano[(i, j)] = {'V': False, 'O': False, 'I': False, 'X': False,
                               'S':False, 'F':False, 'k':False, 'n':False, 'h':0,'Obj':False}
            
            params_mono[(i, j)] = {'V': False, 'O': False, 'I': False, 'X': False,
                               'S':False, 'F':False, 'k':False, 'n':False, 'h':0,'Obj':False}
            
            params_pulpo[(i, j)] = {'V': False, 'O': False, 'I': False, 'X': False,
                               'S':False, 'F':False, 'k':False, 'n':False, 'h':0,'Obj':False}
            
            
            
    params_humano[(13, 2)] = {'V': False, 'O': False, 'I': True, 'X': False,
                         'S':False,'F':False, 'k':False, 'n':False,'h':0,'Obj':False}
    params_humano[(12, 3)] = {'V': False, 'O': False, 'I': False, 'X': False, 
                      'S':False,'F':True, 'k':False, 'n':False,'h':0,'Obj':False}
    params_humano[(14, 13)]['Obj'] = True
    
    params_mono[(13, 4)] = {'V': False, 'O': False, 'I': True, 'X': False,
                         'S':False,'F':False, 'k':False, 'n':False,'h':0,'Obj':False}
    params_mono[(12, 3)] = {'V': False, 'O': False, 'I': False, 'X': False, 
                      'S':False,'F':True, 'k':False, 'n':False,'h':0,'Obj':False}
    params_mono[(6, 7)]['Obj'] = True
    
    params_pulpo[(9, 1)] = {'V': False, 'O': False, 'I': True, 'X': False,
                         'S':False,'F':False, 'k':False, 'n':False,'h':0,'Obj':False}
    params_pulpo[(12, 3)] = {'V': False, 'O': False, 'I': False, 'X': False, 
                      'S':False,'F':True, 'k':False, 'n':False,'h':0,'Obj':False}
    params_pulpo[(2, 14)]['Obj'] = True
    
    objetivos_humano.append((14,13))
    objetivos_humano.append((12,3))
    objetivos_mono.append((6,7))
    objetivos_mono.append((12,3))    
    objetivos_pulpo.append((2,14))
    objetivos_pulpo.append((12,3))
    


    humano=ag.Agente(1)
    mono = ag.Agente(3)
    pulpo = ag.Agente(2)
    
    humano.spawn(params_humano, matriz)
    mono.spawn(params_mono, matriz)
    pulpo.spawn(params_pulpo, matriz)
    
       
    while not gameOver:
            
        pantalla.fill(BLACK)  # La pantalla se llena de un fondo negro.
        # T es un contador para pintar las coordenadas
        T = 0
        #fila es la fila que se va a recorrer de la matriz :V 
        fila = 0

        humano.sense_estrella(params_humano,matriz,objetivos_humano[0][0],objetivos_humano[0][1])
        mono.sense_estrella(params_mono,matriz,objetivos_mono[0][0],objetivos_mono[0][1])
        pulpo.sense_estrella(params_pulpo,matriz,objetivos_pulpo[0][0],objetivos_pulpo[0][1])
        
        # este for recorre el ancho de la pantalla
        for i in range(1, tamañoPantalla[0], 40):
            linea = matriz[fila] #se obtiene una fila de la matriz
            fila = fila+1
            if linea != '':
                columna = 0
                # este for recorre el alto de la pantalla
                for j in range(1, tamañoPantalla[1], 40):

                    lista_params_h = params_humano[(fila-1, columna)]
                    lista_params_m = params_mono[(fila-1, columna)]
                    lista_params_p = params_pulpo[(fila-1, columna)]

                    if linea[columna] == 0:
                           # Los cuadros son ligeramente más pequeños para dar el efecto de la cuadricula.
                           pygame.draw.rect(pantalla, mountains, [j, i, 38, 38], 0)
                    elif linea[columna] == 1:
                            pygame.draw.rect(pantalla, land, [j, i, 38, 38], 0)
                    elif linea[columna] == 2:
                            pygame.draw.rect(pantalla, water, [j, i, 38, 38], 0)
                    elif linea[columna] == 3:
                            pygame.draw.rect(pantalla, sand, [j, i, 38, 38], 0)
                    elif linea[columna] == 4:
                            pygame.draw.rect(pantalla, forest, [j, i, 38, 38], 0)
                    elif linea[columna] == 5:
                            pygame.draw.rect(pantalla, pantano, [j, i, 38, 38], 0)
                    elif linea[columna] == 6:
                            pygame.draw.rect(pantalla, nieve, [j, i, 38, 38], 0)
                    elif linea[columna] == 7:
                            pygame.draw.rect(pantalla, aquaP, [j, i, 38, 38], 0)
                    elif linea[columna] == 8:
                            pygame.draw.rect(pantalla, redP, [j, i, 38, 38], 0)
                    elif linea[columna] == 9:
                            pygame.draw.rect(pantalla, pinkP, [j, i, 38, 38], 0)


                    ## Se obtiene la lista de parametros para esta coordenada
            
                    
                    
                    if(lista_params_h['X']):
                        H = Fuente.render('H', lista_params_h['X'], BLACK)
                        pantalla.blit(H, [j+3, i+3])
                    if(lista_params_m['X']):
                        M = Fuente.render('M', lista_params_m['X'], BLACK)
                        pantalla.blit(M, [j+3, i+15])
                    if(lista_params_p['X']):
                        O = Fuente.render('O', lista_params_p['X'], BLACK)
                        pantalla.blit(O, [j+3, i+27])
                    if(lista_params_h['Obj']):
                        X = Fuente.render('K', lista_params_h['Obj'], BLACK)
                        pantalla.blit(X, [j+15, i+15])
                    if(lista_params_m['Obj']):
                        X = Fuente.render('T', lista_params_m['Obj'], BLACK)
                        pantalla.blit(X, [j+15, i+15])
                    if(lista_params_p['Obj']):
                        X = Fuente.render('S', lista_params_p['Obj'], BLACK)
                        pantalla.blit(X, [j+15, i+15])
                    if (lista_params_h['F']):
                        X = Fuente.render('P', lista_params_h['F'], BLACK)
                        pantalla.blit(X, [j+15, i+15])
                    if (lista_params_h['X'] and lista_params_m['X'] and 
                        lista_params_p['X'] and lista_params_h['F'] and contf == 2):
                        gameOver=True
                        print("Ha llegado a su objetivo!!!")
                        time.sleep(10)
                    elif (lista_params_h['X'] and lista_params_m['X'] and 
                        lista_params_p['X'] and lista_params_h['F']):
                        contf += 1
                    if lista_params_h['X'] and lista_params_h['Obj']:
                        objetivos_humano.pop(0)
                        lista_params_h['Obj']=False
                    if lista_params_m['X'] and lista_params_m['Obj']:
                        objetivos_mono.pop(0)
                        lista_params_m['Obj']=False
                    if lista_params_p['X'] and lista_params_p['Obj']:
                        objetivos_pulpo.pop(0)
                        lista_params_p['Obj']=False
                    columna = columna+1


        
            # Texto es la imagen con la que se pintarán las coordenadas
            Texto = Fuente.render(str(T), True, BLACK)
            pantalla.blit(Texto, [i, 2])  # Coordenadas en el eje X
            if T != 0:
                pantalla.blit(Texto, [2, i])  # Coordenadas en el eje Y
            T += 1

        pygame.display.flip()

        humano.step_estrella(params_humano,objetivos_humano)
        mono.step_estrella(params_mono,objetivos_mono)
        pulpo.step_estrella(params_pulpo,objetivos_pulpo)
        humano.root.imprimir_arbol()
        mono.root.imprimir_arbol()
        pulpo.root.imprimir_arbol()
        
        
        reloj.tick(1)
    pygame.quit()
    print("Costo acumulado: "+str(costoAcumulado))