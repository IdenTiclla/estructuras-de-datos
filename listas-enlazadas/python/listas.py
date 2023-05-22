class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    

class Lista:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def insertar_al_principio(self, valor):
        nodo = Nodo(valor=valor)
        nodo.siguiente = self.cabeza
        self.cabeza = nodo
        self.longitud += 1

    def insertar_al_final(self, valor):
        nodo = Nodo(valor=valor)
        if (self.cabeza):
            puntero = self.cabeza
            while puntero.siguiente:
                puntero = puntero.siguiente
            nodo.siguiente = puntero.siguiente
            puntero.siguiente = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        self.longitud += 1

    def insertar_posicion_n(self, n, valor):
        nodo = Nodo(valor=valor)
        if n == 0:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        else:
            puntero = self.cabeza
            posicion = 0
            while posicion < (n - 1) and puntero.siguiente:
                puntero = puntero.siguiente
                posicion += 1

            if puntero == None:
                print("La posicion especificada esta fuera de rango")
                return 
            
            nodo.siguiente = puntero.siguiente
            puntero.siguiente = nodo
        self.longitud += 1
        

    def eliminarPrincipio(self):
        if self.cabeza:
            eliminado = self.cabeza
            self.cabeza = eliminado.siguiente
            self.longitud -= 1

    def eliminarFinal(self):
        if self.cabeza:
            if self.cabeza.siguiente:
                puntero = self.cabeza
                while puntero.siguiente.siguiente:
                    puntero = puntero.siguiente
                eliminado = puntero.siguiente
                puntero.siguiente = eliminado.siguiente
                self.longitud -= 1
            else:
                eliminado = self.cabeza
                self.cabeza = eliminado.siguiente

                self.longitud -= 1


    def eliminar_en_posicion_n(self, n):
        if n == 0:
            eliminado = self.cabeza
            self.cabeza = eliminado.siguiente
        else:
            posicion = 0
            puntero = self.cabeza
            while posicion < n - 1 and puntero.siguiente:
                puntero = puntero.siguiente
                posicion += 1
            
            if puntero.siguiente == None:
                print("La posicion especificada esta fuera de rango")
                return
            eliminado = puntero.siguiente
            puntero.siguiente = eliminado.siguiente
        
        self.longitud -= 1

    def mostrar_lista(self):
        puntero = self.cabeza
        while puntero:
            print(f"{puntero.valor} ->", end="")
            puntero = puntero.siguiente
        print(f" NULL   | La cantidad de elementos: {self.longitud}")
        


lista_enlazada = Lista()

lista_enlazada.insertar_al_final(1)
lista_enlazada.mostrar_lista()

lista_enlazada.insertar_al_final(2)
lista_enlazada.mostrar_lista()

lista_enlazada.insertar_al_final(3)
lista_enlazada.mostrar_lista()

lista_enlazada.insertar_posicion_n(0, 5)
lista_enlazada.mostrar_lista()

lista_enlazada.insertar_posicion_n(1, 6)
lista_enlazada.mostrar_lista()

lista_enlazada.insertar_posicion_n(2, 7)
lista_enlazada.mostrar_lista()

lista_enlazada.insertar_posicion_n(3, 8)
lista_enlazada.mostrar_lista()

lista_enlazada.eliminarPrincipio()
lista_enlazada.mostrar_lista()

lista_enlazada.eliminarFinal()
lista_enlazada.mostrar_lista()


lista_enlazada.eliminarFinal()
lista_enlazada.mostrar_lista()



lista_enlazada.eliminarFinal()
lista_enlazada.mostrar_lista()

lista_enlazada.eliminarFinal()
lista_enlazada.mostrar_lista()

lista_enlazada.eliminarFinal()
lista_enlazada.mostrar_lista()

lista_enlazada.eliminarFinal()
lista_enlazada.mostrar_lista()


lista_enlazada.insertar_al_final(1)
lista_enlazada.mostrar_lista()

lista_enlazada.insertar_al_final(2)
lista_enlazada.mostrar_lista()

lista_enlazada.insertar_al_final(3)
lista_enlazada.mostrar_lista()

lista_enlazada.eliminar_en_posicion_n(3)
lista_enlazada.mostrar_lista()
