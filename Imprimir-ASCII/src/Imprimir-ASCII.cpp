//============================================================================
// Name        : Imprimir-ASCII.cpp
// Author      : Thomas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>

using namespace std;

class IntIterator{

	public:

		int getNextValue(){
			return this->currentValue++;
		}

		bool hasNextValue(){
			if ((currentValue+1) > maximumValue)
				return false;
			else
				return true;
		}

	protected:
		virtual void configureIterator(){}

		void setMaximumValue(int maximumValue){
			this->maximumValue = maximumValue;
		}

		void setInitialValue(int initialValue){
			this->currentValue = initialValue;
		}

	private:
		int maximumValue;
		int currentValue;


};


class ASCIITableIterator: public IntIterator {
	public:
		ASCIITableIterator(){
			configureIterator();
		}

	protected:
		void configureIterator(){
			setMaximumValue(256);
			setInitialValue(0);
		}

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
