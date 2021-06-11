class Nodo:
    def __init__(self, data):
        self.data = data
        self.hijos = []
        self.padre = None
        self.costo_acumulado = 0
        self.distancia = None
        self.evaluacion = None

    def obtener_nivel(self):
        nivel = 0
        p = self.padre
        while p:
            nivel += 1
            p = p.padre

        return nivel

    def imprimir_arbol(self):
        espacios = ' ' * self.obtener_nivel() * 3
        prefijo = espacios + "|__" if self.padre else ""
        print(prefijo + str(self.data))
        if self.hijos:
            for hijo in self.hijos:
                hijo.imprimir_arbol()

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

def build_product_tree():
    root = Nodo("Electronics")

    laptop = Nodo("Laptop")
    laptop.agregar_hijo(Nodo("Mac"))
    laptop.agregar_hijo(Nodo("Surface"))
    laptop.agregar_hijo(Nodo("Thinkpad"))

    cellphone = Nodo("Cell Phone")
    cellphone.agregar_hijo(Nodo("iPhone"))
    cellphone.agregar_hijo(Nodo("Google Pixel"))
    cellphone.agregar_hijo(Nodo("Vivo"))

    tv = Nodo("TV")
    tv.agregar_hijo(Nodo("Samsung"))
    tv.agregar_hijo(Nodo("LG"))

    root.agregar_hijo(laptop)
    root.agregar_hijo(cellphone)
    root.agregar_hijo(tv)

    root.imprimir_arbol()

if __name__ == '__main__':
    build_product_tree()