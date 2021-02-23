//============================================================================
// Name        : Imprimir-ASCII.cpp
// Author      : Thomas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>

using namespace std;

class ASCIITableIterator{
public:

	int getNextValue (){
		return currentValue++;
	}

	bool hasNextValue(){
		if ((currentValue+1) > maximumValue)
			return false;
		else
			return true;
	}

private:
	const int maximumValue = 256;
	const int initialValue = 0;
	int currentValue = initialValue;


};

int main() {

	ASCIITableIterator ASCIITableIteratorObject;
	int value;

	while (ASCIITableIteratorObject.hasNextValue()){
		value = ASCIITableIteratorObject.getNextValue();
		printf("%d - %c\n", value, value);
	}

	return 0;
}
