typedef struct Nodo {
    int valor;
    struct Nodo* siguiente;
} Nodo;

typedef struct Lista {
    Nodo* cabeza;
} Lista;


Nodo* crearNodo(int valor) {
    Nodo* nodo = (Nodo*) malloc(sizeof(Nodo));
    nodo->valor = valor;
    nodo->siguiente = NULL;
    return nodo;
}

void destruirNodo(Nodo* nodo) {
    free(nodo);
}

void insertarPrincipio(Lista* lista, int valor) {
    Nodo* nodo = crearNodo(valor);
    nodo->siguiente = lista->cabeza;
    lista->cabeza = nodo;
}

void insertarFinal(Lista* lista, int valor) {
    Nodo* nodo = crearNodo(valor);
    if (lista->cabeza) {
        Nodo* puntero = lista->cabeza;
        while (puntero->siguiente) {
            puntero = puntero->siguiente;
        }
        nodo->siguiente = puntero->siguiente;
        puntero->siguiente = nodo;
    } else {
        nodo->siguiente = lista->cabeza;
        lista->cabeza = nodo;
    }
}

void insertarEnPosicionN(Lista* lista, int n, int valor) {
    Nodo* nodo = crearNodo(valor);
    if (n == 0) {
        nodo->siguiente = lista->cabeza;
        lista->cabeza = nodo;
    } else {
        Nodo* puntero = lista->cabeza;
        int posicion = 0;
        while(posicion < (n - 1) && puntero->siguiente) {
            puntero = puntero->siguiente;
            posicion++;
        }
        nodo->siguiente = puntero->siguiente;
        puntero->siguiente = nodo;
    }
}

void eliminarPrincipio(Lista* lista) {
    if (lista->cabeza) {
        Nodo* eliminado = lista->cabeza;
        lista->cabeza = eliminado->siguiente;
        destruirNodo(eliminado);
    }
}

void eliminarFinal(Lista* lista) {
    if (lista->cabeza) {
        if (lista->cabeza->siguiente) {
            Nodo* puntero = lista->cabeza;
            while (puntero->siguiente->siguiente) {
                puntero = puntero->siguiente;
            }
            Nodo* eliminado = puntero->siguiente;
            puntero->siguiente = eliminado->siguiente;
            destruirNodo(eliminado);
        } else {
            Nodo* eliminado = lista->cabeza;
            lista->cabeza = eliminado->siguiente;
            destruirNodo(eliminado);
        }

    }
}

void eliminarPosicionN(Lista* lista, int n) {
    if (n == 0) {
        Nodo* eliminado = lista->cabeza;
        lista->cabeza = eliminado->siguiente;
        destruirNodo(eliminado);
    } else {
        Nodo* puntero = lista->cabeza;
        int posicion = 0;
        while (posicion < (n - 1) && puntero->siguiente) {
            puntero = puntero->siguiente;
            posicion++;
        }
        if (puntero->siguiente == NULL) {
            printf("Posicion fuera de rango\n");
            return;
        }
        Nodo* eliminado = puntero->siguiente;
        puntero->siguiente = eliminado->siguiente;
    }
}


void mostrarLista(Lista* lista) {
    if (lista->cabeza) {
        Nodo* puntero = lista->cabeza;
        while (puntero) {
            printf("%d -> ", puntero->valor);
            puntero = puntero->siguiente;
        }
        printf("NULL \n");
    } else {
        printf("La lista esta vacia\n");
    }
}