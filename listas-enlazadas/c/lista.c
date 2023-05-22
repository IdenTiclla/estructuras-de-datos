#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

int main(void) {
    Lista* lista = malloc(sizeof(Lista));
    lista->cabeza = NULL;

    mostrarLista(lista);

    insertarFinal(lista, 1);
    mostrarLista(lista);


    insertarFinal(lista, 2);
    mostrarLista(lista);


    insertarFinal(lista, 3);
    mostrarLista(lista);

    eliminarPosicionN(lista, 3);
    mostrarLista(lista);


    free(lista);

    return 0;
}

