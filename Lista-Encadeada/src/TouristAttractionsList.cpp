//============================================================================
// Name        : Lista-Encadeada.cpp
// Author      : Thomas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <ListElement.cpp>

using namespace std;


class TouristAttractionInformation: public ListElementInformation{ // @suppress("Class has a virtual method and non-virtual destructor")
	public:
		void doNothing(){}

	    string description;
		float latitude;
		float longitude;
};



class TouristAttractionApplication{
	public:

	TouristAttractionApplication(){
		listManager.createNewList();
		}

		void execute(){
			while (defineListOperation() == '1'){
				listManager.
					addNewElementInTheBegginingOfList(
						readTouristAttraction());
			}
		}

	private:

		TouristAttractionInformation readTouristAttraction(){
			TouristAttractionInformation touristAttraction;

			cout << "Digite a descrição do ponto turístico" << endl;
			cin >> touristAttraction.description;

			cout << "Digite a latitude do ponto turístico" << endl;
			cin >> touristAttraction.latitude;

			cout << "Digite a longitude do ponto turístico" << endl;
			cin >> touristAttraction.longitude;

			return touristAttraction;
		}

		char defineListOperation(){
			char operation;

			cout << "As operações disponíveis para a lista são: "<< endl;
			cout << "1 - Adicionar" << endl;
			cout << "2 - Sair" << endl;

			cin >> operation;

			return operation;
		}

		ListManager listManager;
};


int main() {

	TouristAttractionApplication application;

	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!

	application.execute();

	return 0;
}
