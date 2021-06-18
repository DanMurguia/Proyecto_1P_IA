import Nodo
 
humano = {0: False, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5} #definicion humano
pulpo = {0: False, 1: 2, 2: 1, 3: False, 4: 3, 5: 2, 6: False} #definicion humano
mono = {0: False, 1: 2, 2: 4, 3: 3, 4: 1, 5: 5, 6: False}
chupacabras = {0: 15, 1: 4, 2: False, 3: False, 4: 4, 5: 5, 6: 3}

              
class Agente:
    def __init__(self, agente):
        self.nodo_act = None
        self.ente = self.definir_agente(agente)
        self.root = None
        self.lista_nodos = [] 
        self.costoTotal=0
        self.ordenados=[]
        self.camino=[]
        
    def definir_agente(self, agente):
        if agente==1:
            ente=humano
        elif agente==2:
            ente=pulpo
        elif agente==3:
            ente = mono
        elif agente==4:
            ente =chupacabras
        elif agente<1 and agente>4:
            print("ente no definido")
        return ente       

    def spawn(self, paramsd,matriz):
        col= matriz.shape[0]
        fil = matriz.shape[1]
        for i in range(0, fil):
            for j in range(0, col):
                if(paramsd[(i,j)]['I']):
                    if (self.ente[matriz[i][j]]):#generalizar
                        paramsd[(i,j)]['S'] = True
                        paramsd[(i,j)]['X'] = True
                        paramsd[(i,j)]['n'] = True
                        self.root = Nodo.Nodo((i,j))
                        self.nodo_act = self.root
                        self.nodo_act.costo_acumulado=0
                    else:
                        paramsd[(i,j)]['I'] = False
                        paramsd[(i,j)]['S'] = False
                        paramsd[(i,j)]['X'] = False
                        paramsd[(i-1,j)]['I'] = True
                        paramsd[(i-1,j)]['S'] = True
                        paramsd[(i-1,j)]['X'] = True
                        paramsd[(i,j)]['n'] = True
                        self.root = Nodo.Nodo((i-1,j))
                        self.nodo_act = self.root
                        self.nodo_act.costo_acumulado=0
                if (paramsd[(i, j)]['F']):
                    if (self.ente[matriz[i][j]]):
    
                        paramsd[(i, j)]['S'] = True
                    else:
                        paramsd[(i, j)]['F'] = False
                        paramsd[(i, j)]['S'] = False
                        paramsd[(i - 1, j)]['F'] = True
                        paramsd[(i - 1, j)]['S'] = True


    def sense_estrella(self, paramsd, matriz,xfinal,yfinal):
        col = matriz.shape[0]
        fil = matriz.shape[1]
        aux = 0;
        caminos_bloqueados = 0
        for i in range(0, fil):
            for j in range(0, col):
                if (paramsd[(i, j)]['X']):
                    paramsd[(i, j)]['S'] = True

                    if (i > 0):
                        paramsd[(i - 1, j)]['S'] = True
                        if (self.ente[matriz[i - 1][j]] and not paramsd[(i - 1, j)]['V']):
                            if not paramsd[(i - 1, j)]['n']:
                                paramsd[(i - 1, j)]['O'] = True
                                nuevo_nodo = Nodo.Nodo((i-1, j))
                                self.nodo_act.agregar_hijo(nuevo_nodo)
                                paramsd[(i-1, j)]['n'] = True
                                nuevo_nodo.costo_acumulado= self.costo_acumulado(i - 1, j, matriz)
                                nuevo_nodo.distancia= self.calcular_distancia(i - 1, j,xfinal,yfinal)
                                nuevo_nodo.evaluacion=nuevo_nodo.costo_acumulado+nuevo_nodo.distancia
                                paramsd[(i-1, j)]['h'] = nuevo_nodo.evaluacion
                                print(nuevo_nodo.distancia)
                                print(nuevo_nodo.costo_acumulado)
                                print(nuevo_nodo.evaluacion)
                                self.lista_nodos.append(nuevo_nodo)

                        else:# self.ente[matriz[i - 1][j]] or paramsd[(i - 1, j)]['V']:
                            caminos_bloqueados += 1
                    else:
                        caminos_bloqueados += 1

                    if (i < fil - 1):
                        paramsd[(i + 1, j)]['S'] = True
                        if (self.ente[matriz[i + 1][j]] and not paramsd[(i + 1, j)]['V']):
                            if not paramsd[(i + 1, j)]['n']:
                                paramsd[(i + 1, j)]['O'] = True
                                nuevo_nodo = Nodo.Nodo((i + 1, j))
                                self.nodo_act.agregar_hijo(nuevo_nodo)
                                paramsd[(i +1, j)]['n'] = True
                                nuevo_nodo.costo_acumulado = self.costo_acumulado(i +1, j, matriz)
                                nuevo_nodo.distancia = self.calcular_distancia(i + 1, j,xfinal, yfinal)
                                nuevo_nodo.evaluacion = nuevo_nodo.costo_acumulado + nuevo_nodo.distancia
                                paramsd[(i +1, j)]['h'] = nuevo_nodo.evaluacion
                                print(nuevo_nodo.distancia)
                                print(nuevo_nodo.costo_acumulado)
                                print(nuevo_nodo.evaluacion)
                                self.lista_nodos.append(nuevo_nodo)
                        else:# self.ente[matriz[i + 1][j]] or paramsd[(i + 1, j)]['V']:
                            caminos_bloqueados += 1
                    else:
                        caminos_bloqueados += 1

                    if (j > 0):
                        paramsd[(i, j - 1)]['S'] = True
                        if (self.ente[matriz[i][j - 1]] and not paramsd[(i, j - 1)]['V']):
                            if not paramsd[(i , j-1)]['n']:
                                paramsd[(i , j-1)]['O'] = True
                                nuevo_nodo = Nodo.Nodo((i , j-1))
                                self.nodo_act.agregar_hijo(nuevo_nodo)
                                paramsd[(i , j-1)]['n'] = True
                                nuevo_nodo.costo_acumulado = self.costo_acumulado(i , j-1, matriz)
                                nuevo_nodo.distancia = self.calcular_distancia(i, j - 1,xfinal, yfinal)
                                nuevo_nodo.evaluacion = nuevo_nodo.costo_acumulado + nuevo_nodo.distancia
                                paramsd[(i , j-1)]['h'] = nuevo_nodo.evaluacion
                                print(nuevo_nodo.distancia)
                                print(nuevo_nodo.costo_acumulado)
                                print(nuevo_nodo.evaluacion)
                                self.lista_nodos.append(nuevo_nodo)
                        else:# self.ente[matriz[i][j - 1]] or paramsd[(i, j - 1)]['V']:
                            caminos_bloqueados += 1
                    else:
                        caminos_bloqueados += 1

                    if (j < col - 1):
                        paramsd[(i, j + 1)]['S'] = True
                        if (self.ente[matriz[i][j + 1]] and not paramsd[(i, j + 1)]['V']):
                            if not paramsd[(i , j+1)]['n']:
                                paramsd[(i , j+1)]['O'] = True
                                nuevo_nodo = Nodo.Nodo((i , j+1))
                                self.nodo_act.agregar_hijo(nuevo_nodo)
                                paramsd[(i , j+1)]['n'] = True
                                nuevo_nodo.costo_acumulado = self.costo_acumulado(i , j+1, matriz)
                                nuevo_nodo.distancia = self.calcular_distancia(i, j + 1,xfinal, yfinal)
                                nuevo_nodo.evaluacion = nuevo_nodo.costo_acumulado + nuevo_nodo.distancia
                                paramsd[(i , j+1)]['h'] = nuevo_nodo.evaluacion

                                print(nuevo_nodo.distancia)
                                print(nuevo_nodo.costo_acumulado)
                                print(nuevo_nodo.evaluacion)
                                self.lista_nodos.append(nuevo_nodo)
                        else:# self.ente[matriz[i][j + 1]] or paramsd[(i, j + 1)]['V']:
                            caminos_bloqueados += 1
                    else:

                        caminos_bloqueados += 1

                    if caminos_bloqueados > 3:
                        paramsd[(i, j)]['k'] = True
                    print(caminos_bloqueados)

    def step_estrella(self, paramsd,lista_obj):
        nodoaux = None
        evaluacion_auxiliar=0
        paramsd[self.nodo_act.data]['V'] = True
        if not paramsd[self.nodo_act.data]['F'] or len(lista_obj)>1:
            print(paramsd[self.nodo_act.data],self.nodo_act.data)
            nodoaux=self.lista_nodos[0]
            self.lista_nodos.pop(0)
            paramsd[self.nodo_act.data]['X'] = False
            paramsd[nodoaux.data]['X'] = True
            self.nodo_act=nodoaux
            print(paramsd[self.nodo_act.data],self.nodo_act.data)
                        
    def costo_acumulado(self,i,j,matriz):
        costo_acumulado=self.nodo_act.costo_acumulado+ self.ente[matriz[i][j]]
        return costo_acumulado

    def calcular_distancia(self,i,j,xfinal,yfinal):
        distancia=abs(i-xfinal)+abs(j-yfinal)
        return distancia

    def ordenar_nodos(self):
    	self.ordenados=sorted(self.lista_nodos,key=lambda x: x.evaluacion)
    	self.lista_nodos=self.ordenados
    	'''for nodo in self.lista_nodos:
    		print(nodo.data,nodo.evaluacion)'''

    def reiniciar_lista(self):
    	self.lista_nodos.clear()

    def recorrido_optimo(self):
    	nodoaux = self.nodo_act
    	while(nodoaux != None):
    		self.camino.append(nodoaux)
    		nodoaux=nodoaux.padre
    	self.camino.reverse()
    	for nodo in self.camino:
    		print(nodo.data)