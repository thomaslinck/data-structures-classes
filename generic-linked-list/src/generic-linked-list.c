/*
 ============================================================================
 Name        : generic-linked-list.c
 Author      : Thomas
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define EXIT '1'

typedef struct ListNode{
	char nodeValue;
	int id;
	struct ListNode * nextNode;
} ListNode;
typedef ListNode * ListNodePointer;


int getRandomId(void){
	srand(time(0));
	return (int) rand();
}

char getValue(void){
	char value[2] = "0";
	printf("\nDigite o valor:");
	gets(value);
	return value[0];
}

ListNodePointer createList(void){
	return NULL;
}

ListNodePointer insertInBeggining(ListNodePointer header, char value){
	ListNodePointer newElement = (ListNodePointer) malloc(sizeof(ListNode));
	newElement->id = getRandomId();
	newElement->nodeValue = value;
	newElement->nextNode = header;
	return newElement;
}
void printElement(ListNodePointer node){
	if(node == NULL) printf("Element does not exist");
	else printf("\n%d - %c", node->id, node->nodeValue);
}

void printList(ListNodePointer header){
	printf("\n\nList:");
	for(ListNodePointer p = header; p != NULL; p = p->nextNode)
		printElement(p);
}

ListNodePointer getNodeWhere(ListNodePointer header, char value){
	for(ListNodePointer p = header; p != NULL; p = p->nextNode)
		if(p->nodeValue == value) return p;
	return NULL;
}

ListNodePointer deleteNextNode(ListNodePointer currentNode){
	ListNodePointer aux = currentNode->nextNode;
	currentNode->nextNode = aux->nextNode;
	free(aux);
	return currentNode;
}

ListNodePointer deleteNodeWhere(ListNodePointer header, char value){
	ListNodePointer aux = header;

		if(header->nodeValue == value){
			header = header->nextNode;
			free(aux);
			return header;
		}

		for(ListNodePointer p = header; p != NULL; p = p->nextNode){
			if(p->nextNode->nodeValue == value) {
				header = deleteNextNode(p);
				return header;
			}
		}

		return NULL;
}

ListNodePointer deleteList(ListNodePointer header){
	for(header; header != NULL; header = header->nextNode)
		header = deleteNextNode(header);
	free(header);
	return NULL;
}

int main(void) {
	ListNodePointer header;
	char selection[2] = "0";

	header = createList();

	while(selection[0] != EXIT){
		printf("\n---------------------------------------------------");
		printf("\nEscolha uma das opções:");
		printf("\n1 - Sair");
		printf("\n2 - Adicionar elemento na lista");
		printf("\n3 - Imprimir lista");
		printf("\n4 - Buscar nodo");
		printf("\n5 - Deletar nodo");
		printf("\n6 - Deletar lista");

		gets(selection);

		switch(selection[0]){
			case '2':
				header = insertInBeggining(header, getValue());
				break;
			case '3':
				printList(header);
				break;
			case '4':
				printElement(getNodeWhere(header, getValue()));
				break;
			case '5':
				header = deleteNodeWhere(header, getValue());
				break;
			case '6':
				header = deleteList(header);
				break;
		}
	}

	return 0;
}
