import numpy as np

def crear_matriz(probabilidades, forma): #Crea una matriz de numeros aleatorios
    matriz = np.random.choice(7,forma,probabilidades)
    return matriz

def guardar_matriz(fname,matriz): #guarda una matriz :V
    a = open(fname, "w")
    np.savetxt(a, matriz, fmt='%d', delimiter=',')
    a.close()
    
def cargar_matriz(fname): #carga una matriz :VVVVV
    matriz = np.loadtxt(fname, dtype=int,delimiter =  ',')
    return matriz
    
def generar_probabilidades(n_probabilidades): ##genera las probabilidades de 
    probabilidades = []                       ##parecer de cada numero de  
    probabilidad_restante = 1                 ##la matriz
    for i in range(n_probabilidades):
        if (i < n_probabilidades-1):
            probabilidad = probabilidad_restante * np.random.sample()
            probabilidad_restante -= probabilidad
            probabilidades.append(probabilidad)
    probabilidad = probabilidad_restante 
    probabilidad_restante = 0
    probabilidades.append(probabilidad)
    return probabilidades

if __name__ == '__main__':
    probabilidades = generar_probabilidades(7) 
    fname = "matriz_aleatoria.txt"
    forma = (15,15)
    matriz = crear_matriz(probabilidades,forma)
    guardar_matriz(fname,matriz)
    