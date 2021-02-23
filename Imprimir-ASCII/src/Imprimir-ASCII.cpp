//============================================================================
// Name        : Imprimir-ASCII.cpp
// Author      : Thomas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>

using namespace std;

int main() {

	int i;

	for (i=0; i<256; i++)
		printf("%d - %c\n", i, i);

	return 0;
	system("Pause");
}
