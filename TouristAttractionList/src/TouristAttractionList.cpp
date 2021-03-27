//============================================================================
// Name        : TouristAttractionList.cpp
// Author      : Thomas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string.h>
#include "TouristAttractionListManager.cpp"

using namespace std;

class Application{
public:

	Application(){
		touristAttractionsListManager.createNewList();
		definedListOperation = '1';
	}

	void execute(){
		while (defineListOperation() != '1'){
			switch(definedListOperation){
				case '2':
					touristAttractionsListManager.
					addNewAttractionInBegginingOfList(
							readTouristAttraction());
					break;

				case '3':
					printAttractionsList();
					break;

				case '4':
					searchInAttractionsList();
					break;
			}
		}
	}

private:

	TouristAttractionInformation readTouristAttraction(){
		TouristAttractionInformation touristAttraction;

		cout << "\nDigite a descrição do ponto turístico" << endl;
		cin >> touristAttraction.description;

		cout << "Digite a latitude do ponto turístico" << endl;
		cin >> touristAttraction.latitude;

		cout << "Digite a longitude do ponto turístico" << endl;
		cin >> touristAttraction.longitude;

		return touristAttraction;
	}

	char defineListOperation(){
		cout << "\n\nAs operações disponíveis para a lista são: "<< endl;
		cout << "1 - Sair" << endl;
		cout << "2 - Adicionar" << endl;
		cout << "3 - Imprimir Atrações" << endl;
		cout << "4 - Procurar Atração\n" << endl;
		cin >> definedListOperation;
		return definedListOperation;
	}

	void printAttractionsList(){
		touristAttractionsListManager.resetCurrentElement();

		do { printAttraction(touristAttractionsListManager.getCurrentElement()->touristAttractionInformation); }
		while(touristAttractionsListManager.positionInNextElementIfExists());
	}

	void printAttraction(TouristAttractionInformation touristAttraction){
		cout << touristAttraction.description << " - "
		     << touristAttraction.latitude << " - "
			 << touristAttraction.longitude << endl;
	}

	void searchInAttractionsList(){
		string attractionToSearch;

		cout << "\nDigite o nome da atração que deseja procurar" << endl;
		cin >> attractionToSearch;

		try{
			printAttraction(touristAttractionsListManager.getElementWhere(attractionToSearch)->touristAttractionInformation);
		}
		catch(const char * error){
			cout << error <<endl;
		}
	}

	TouristAttractionsListManager touristAttractionsListManager;
	char definedListOperation;
};


int main() {

	Application application;

	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!

	application.execute();

	return 0;
}
