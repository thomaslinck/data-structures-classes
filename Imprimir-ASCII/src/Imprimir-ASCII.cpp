//============================================================================
// Name        : Imprimir-ASCII.cpp
// Author      : Thomas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class IntIterator{ // @suppress("Class has a virtual method and non-virtual destructor")

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


class ASCIITableIterator: public IntIterator { // @suppress("Class has a virtual method and non-virtual destructor")
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

class Application{
	public:
		Application(IntIterator iterator){
			this->iterator = iterator;
		}

		void execute(){
			int value;

			while (iterator.hasNextValue()){
				value = iterator.getNextValue();
				printf("%d - %c\n", value, value);
			}
		}

	private:
		IntIterator iterator;
};

int main() {

	ASCIITableIterator ASCIITableIteratorObject;
	Application application(ASCIITableIteratorObject);

	application.execute();

	return 0;
}
