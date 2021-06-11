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
        self.lista = [] 
        
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
                        self.lista.append(self.root)
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
                        self.lista.append(self.root)
                        self.nodo_act.costo_acumulado=0
                if (paramsd[(i, j)]['F']):
                    if (self.ente[matriz[i][j]]):
    
                        paramsd[(i, j)]['S'] = True
                    else:
                        paramsd[(i, j)]['F'] = False
                        paramsd[(i, j)]['S'] = False
                        paramsd[(i - 1, j)]['F'] = True
                        paramsd[(i - 1, j)]['S'] = True

    def sense(self,paramsd, matriz):
        col= matriz.shape[0]
        fil = matriz.shape[1]
        aux=0;
        caminos_bloqueados = 0 
        for i in range(0, fil):
            for j in range(0, col):
                if (paramsd[(i, j)]['X']):
                    paramsd[(i, j)]['S'] = True
    
                    if(i>0):
                        paramsd[(i-1, j)]['S']= True
                        if (self.ente[matriz[i -1][j]]and not paramsd[(i-1, j)]['V']):
                            aux = aux + 1
                        if not self.ente[matriz[i-1][j]] or paramsd[(i-1, j)]['V']:
                            caminos_bloqueados += 1    
                    else: 
                        caminos_bloqueados += 1
    
                    if(i<fil-1):
                        paramsd[(i+1,j)]['S'] = True
                        if (self.ente[matriz[i+1][j]]and not paramsd[(i+1, j)]['V']):
                            aux = aux + 1
                        if not self.ente[matriz[i+1][j]] or paramsd[(i+1, j)]['V']:
                            caminos_bloqueados += 1
                    else:
                        caminos_bloqueados += 1
    
                    if (j>0):
                        paramsd[(i, j-1)]['S']= True
                        if (self.ente[matriz[i][j -1]] and not paramsd[(i, j-1)]['V']):
                            aux = aux + 1
                        if not self.ente[matriz[i][j-1]] or paramsd[(i, j-1)]['V']:
                            caminos_bloqueados += 1
                    else:
                        caminos_bloqueados += 1
    
                    if (j < col-1):
                        paramsd[(i, j+1)]['S'] = True
                        if (self.ente[matriz[i][j+1]]and not paramsd[(i, j+1)]['V']):
                            aux = aux+1
                        if not self.ente[matriz[i][j+1]] or paramsd[(i, j+1)]['V']:
                            caminos_bloqueados += 1
                    else:
                        caminos_bloqueados += 1
    
                    if aux>1:
                        paramsd[(i, j )]['O'] = True
                        
                    elif caminos_bloqueados > 3:
                        paramsd[(i, j )]['k'] = True

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
                        else:# self.ente[matriz[i][j + 1]] or paramsd[(i, j + 1)]['V']:
                            caminos_bloqueados += 1
                    else:

                        caminos_bloqueados += 1

                    if caminos_bloqueados > 3:
                        paramsd[(i, j)]['k'] = True
                    print(caminos_bloqueados)


    def step_profundidad(self, paramsd, matriz):
        aux = 0
        col= matriz.shape[0]
        fil = matriz.shape[1]
    
        for i in range(0, fil):
            for j in range(0, col):
    
                    if paramsd[(i, j)]['X']:
    
    
                        if not paramsd[(i, j)]['F']:
                        
                            if paramsd[(i, j)]['X'] and paramsd[(i, j)]['V']:
                                if  paramsd[(i, j)]['k']:
                                    if not paramsd[(i, j)]['n']:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.nodo_act.agregar_hijo(nuevo_nodo)
                                        coordenadas = nuevo_nodo.padre.data
                                        paramsd[(i,j)]['n'] = True
                                        print(coordenadas)
                                        paramsd[(i,j)]['X'] = False
                                        paramsd[coordenadas]['X'] = True
                                        return False
                                    else:
                                        coordenadas = self.nodo_act.padre.data
                                        print(coordenadas)
                                        paramsd[(i,j)]['X'] = False
                                        paramsd[coordenadas]['X'] = True
                                        self.nodo_act = self.nodo_act.padre
                                        return False
                                                                        
                                    
    
    
                            paramsd[(i, j)]['V'] = True
    
                            if i-1 >= 0 and self.ente[matriz[i-1][j]] and not paramsd[(i-1, j)]['V']:
                                paramsd[(i, j)]['X']=False
                                paramsd[(i-1, j)]['X']=True
                                costo=self.ente[matriz[i-1][j]]
                                if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']:
                                    if not self.nodo_act.padre:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.root.agregar_hijo(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        self.nodo_act = nuevo_nodo
                                    else:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.nodo_act.agregar_hijo(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        self.nodo_act = nuevo_nodo
                                return costo
    
                            if j -1 >= 0 and self.ente[matriz[i][j-1]] and not paramsd[(i, j-1)]['V']:
                                paramsd[(i, j)]['X'] = False
                                paramsd[(i, j - 1)]['X'] = True
                                costo=self.ente[matriz[i][j-1]]
                                if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']:
                                    if not self.nodo_act.padre:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.root.agregar_hijo(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        nodo_act = nuevo_nodo
                                    else:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.nodo_act.agregar_hijo(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        self.nodo_act = nuevo_nodo
                                return costo                            

                            if i+1 < fil and self.ente[matriz[i+1][j]] and not paramsd[(i+1, j)]['V'] :
                                paramsd[(i, j)]['X'] = False
                                paramsd[(i +1, j)]['X'] = True
                                costo=self.ente[matriz[i+1][j]]
                                if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']:
                                    if not self.nodo_act.padre:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.root.agregar_hijo(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        self.nodo_act = nuevo_nodo
                                    else:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.nodo_act.agregar_hijo(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        self.nodo_act = nuevo_nodo
                                return costo
                            
                            if j+1 < col and self.ente[matriz[i][j+1]] and not paramsd[(i, j+1)]['V']:
                                paramsd[(i, j)]['X'] = False
                                paramsd[(i, j+1)]['X'] = True
                                costo=self.ente[matriz[i][j+1]]
                                if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']:
                                    if not self.nodo_act.padre:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.root.agregar_hijo(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        nodo_act = nuevo_nodo
                                    else:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.nodo_act.agregar_hijo(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        nodo_act = nuevo_nodo
                                return costo
                            return False
                        else:
                            if not paramsd[(i, j)]['n']:
                                nuevo_nodo = Nodo.Nodo((i,j))
                                self.nodo_act.agregar_hijo(nuevo_nodo)
                                paramsd[(i,j)]['n'] = True
                                return False
                            else:
                                return False
                        
    
    def step_anchura(self, paramsd, matriz):
        aux = 0
        col= matriz.shape[0]
        fil = matriz.shape[1]
    
        for i in range(0, fil):
            for j in range(0, col):
    
                    if paramsd[(i, j)]['X']:
    
    
                        if not paramsd[(i, j)]['F']:
                        
                            if paramsd[(i, j)]['X'] and paramsd[(i, j)]['V']:
                                if  paramsd[(i, j)]['k']:
                                    if not paramsd[(i, j)]['n']:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.nodo_act.agregar_hijo(nuevo_nodo)
                                        #coordenadas = nuevo_nodo.padre.data
                                        paramsd[(i,j)]['n'] = True
                                        paramsd[(i,j)]['X'] = False
                                        #lista.pop(0)
                                        self.nodo_act=self.lista[0]
                                        
                                        paramsd[self.nodo_act.data]['X'] = True
                                        return False
                                    else:
                                        #coordenadas = self.nodo_act.padre.data
                                        paramsd[(i,j)]['X'] = False
                                        #paramsd[coordenadas]['X'] = True
                                        self.lista.pop(0)
                                        self.nodo_act=self.lista[0]
                                        paramsd[self.nodo_act.data]['X'] = True
                                        return False
                                                                        
                                    
    
    
                            paramsd[(i, j)]['V'] = True
    
                            if i-1 >= 0 and self.ente[matriz[i-1][j]] and not paramsd[(i-1, j)]['V']:
                                paramsd[(i, j)]['X']=False
                                paramsd[(i-1, j)]['X']=True
                                costo=self.ente[matriz[i-1][j]]
                                if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']:
                                    if not self.nodo_act.padre:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.root.agregar_hijo(nuevo_nodo)
                                        self.lista.append(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        paramsd[(i-1, j)]['X'] = False
                                        paramsd[self.nodo_act.data]['X']=True
                                        #self.nodo_act = nuevo_nodo
                                    else:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.nodo_act.agregar_hijo(nuevo_nodo)
                                        self.lista.append(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        paramsd[(i-1, j)]['X'] = False
                                        paramsd[self.nodo_act.data]['X']=True
                                        #self.nodo_act = nuevo_nodo
                                return costo
    
                            if j -1 >= 0 and self.ente[matriz[i][j-1]] and not paramsd[(i, j-1)]['V']:
                                paramsd[(i, j)]['X'] = False
                                paramsd[(i, j - 1)]['X'] = True
                                costo=self.ente[matriz[i][j-1]]
                                if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']:
                                    if not self.nodo_act.padre:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.root.agregar_hijo(nuevo_nodo)
                                        self.lista.append(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        paramsd[(i, j-1)]['X'] = False
                                        paramsd[self.nodo_act.data]['X']=True
                                        #self.nodo_act = nuevo_nodo
                                    else:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.nodo_act.agregar_hijo(nuevo_nodo)
                                        self.lista.append(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        paramsd[(i, j - 1)]['X'] = False
                                        paramsd[self.nodo_act.data]['X']=True
                                        #self.nodo_act = nuevo_nodo
                                return costo
                            
                            if i+1 < fil and self.ente[matriz[i+1][j]] and not paramsd[(i+1, j)]['V'] :
                                paramsd[(i, j)]['X'] = False
                                paramsd[(i +1, j)]['X'] = True
                                costo=self.ente[matriz[i+1][j]]
                                if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']:
                                    if not self.nodo_act.padre:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.root.agregar_hijo(nuevo_nodo)
                                        self.lista.append(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        paramsd[(i+1, j)]['X'] = False
                                        paramsd[self.nodo_act.data]['X']=True
                                        #self.nodo_act = nuevo_nodo
                                    else:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.nodo_act.agregar_hijo(nuevo_nodo)
                                        self.lista.append(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        paramsd[(i+1, j)]['X'] = False
                                        paramsd[self.nodo_act.data]['X']=True
                                        #self.nodo_act = nuevo_nodo
                                return costo
                            
                            if j+1 < col and self.ente[matriz[i][j+1]] and not paramsd[(i, j+1)]['V']:
                                paramsd[(i, j)]['X'] = False
                                paramsd[(i, j+1)]['X'] = True
                                costo=self.ente[matriz[i][j+1]]
                                if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']: 
                                    if not self.nodo_act.padre:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.root.agregar_hijo(nuevo_nodo)
                                        self.lista.append(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        paramsd[(i, j+1)]['X'] = False
                                        paramsd[self.nodo_act.data]['X']=True
                                        #self.nodo_act = nuevo_nodo
                                    else:
                                        nuevo_nodo = Nodo.Nodo((i,j))
                                        self.nodo_act.agregar_hijo(nuevo_nodo)
                                        self.lista.append(nuevo_nodo)
                                        paramsd[(i,j)]['n'] = True
                                        paramsd[(i, j + 1)]['X'] = False
                                        paramsd[self.nodo_act.data]['X']=True
                                        #self.nodo_act = nuevo_nodo
                                return costo
                            return False
                        else:
                            if not paramsd[(i, j)]['n']:
                                nuevo_nodo = Nodo.Nodo((i,j))
                                self.nodo_act.agregar_hijo(nuevo_nodo)
                                paramsd[(i,j)]['n'] = True
                                return False
                            else:
                                return False



    def step_estrella(self, paramsd,lista_obj):
        nodoaux = None
        evaluacion_auxiliar=0
        paramsd[self.nodo_act.data]['V'] = True
        if not paramsd[self.nodo_act.data]['F']:
            print(paramsd[self.nodo_act.data],self.nodo_act.data)
            if not paramsd[self.nodo_act.data]['k']:
                for nodo in self.nodo_act.hijos:
                    if not evaluacion_auxiliar and not paramsd[nodo.data]['V']:
                        evaluacion_auxiliar=nodo.evaluacion
                        nodoaux=nodo
                    elif nodo.evaluacion<evaluacion_auxiliar and not paramsd[nodo.data]['V']:
                        evaluacion_auxiliar = nodo.evaluacion
                        nodoaux = nodo

                paramsd[self.nodo_act.data]['X'] = False
                paramsd[nodoaux.data]['X'] = True
                self.nodo_act=nodoaux
            else:
                paramsd[self.nodo_act.data]['X']=False
                self.nodo_act = self.nodo_act.padre
                paramsd[self.nodo_act.data]['X']=True
                print("holo")
            print(paramsd[self.nodo_act.data],self.nodo_act.data)

        

    def step_down(self, paramsd, matriz):
    
        col= matriz.shape[0]
        fil = matriz.shape[1]
    
        for i in range(0, fil):
            for j in range(0, col):
    
                    if paramsd[(i, j)]['X']:
    
    
    
                        if not paramsd[(i, j)]['F']:
                            paramsd[(i, j)]['V'] = True
    
                            if i+1 < fil and self.ente[matriz[i+1][j]]:
                                paramsd[(i, j)]['X'] = False
                                paramsd[(i +1, j)]['X'] = True
    
                                costo = self.ente[matriz[i+1][j]]
                                return costo
    
    def step_up(self,paramsd, matriz):
    
        col= matriz.shape[0]
        fil = matriz.shape[1]
    
        for i in range(0, fil):
            for j in range(0, col):
    
                    if paramsd[(i, j)]['X']:
    
    
    
                        if not paramsd[(i, j)]['F']:
                            paramsd[(i, j)]['V'] = True
    
                            if i-1 >= 0 and self.ente[matriz[i-1][j]]:
                                paramsd[(i, j)]['X']=False
                                paramsd[(i-1, j)]['X']=True
    
                                costo = self.ente[matriz[i-1][j]]
                                return costo
    
    def step_right(self,paramsd, matriz):
    
        col= matriz.shape[0]
        fil = matriz.shape[1]
    
        for i in range(0, fil):
            for j in range(0, col):
    
                    if paramsd[(i, j)]['X']:
    
    
    
                        if not paramsd[(i, j)]['F']:
                            paramsd[(i, j)]['V'] = True
    
                            if j+1 < col and self.ente[matriz[i][j+1]]:
                                paramsd[(i, j)]['X'] = False
                                paramsd[(i, j+1)]['X'] = True
    
                                costo = self.ente[matriz[i][j+1]]
                                return costo
    
    def step_left(self, paramsd, matriz):
    
        col= matriz.shape[0]
        fil = matriz.shape[1]
    
        for i in range(0, fil):
            for j in range(0, col):
    
                    if paramsd[(i, j)]['X']:
    
    
    
                        if not paramsd[(i, j)]['F']:
                            paramsd[(i, j)]['V'] = True
    
                            if j -1 >= 0 and self.ente[matriz[i][j-1]]:
                                paramsd[(i, j)]['X'] = False
                                paramsd[(i, j - 1)]['X'] = True
    
                                costo = self.ente[matriz[i][j-1]]
    
                                return costo
                        
    def costo_acumulado(self,i,j,matriz):
        costo_acumulado=self.nodo_act.costo_acumulado+ self.ente[matriz[i][j]]
        return costo_acumulado

    def calcular_distancia(self,i,j,xfinal,yfinal):
        distancia=abs(i-xfinal)+abs(j-yfinal)
        return distancia