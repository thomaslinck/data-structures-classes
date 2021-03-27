
#include <iostream>
#include "ListElement.cpp"

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
		definedListOperation = '1';
	}

		void execute(){

			while (defineListOperation() != '1'){

				switch(definedListOperation){
					case '2':
						listManager.
							addNewElementInTheBegginingOfList(
								readTouristAttraction());
						break;

					case '3':
						printAttractionsList();

				}

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
			cout << "As operações disponíveis para a lista são: "<< endl;
			cout << "1 - Sair" << endl;
			cout << "2 - Adicionar" << endl;
			cout << "3 - ImprimirAtrações" << endl;

			cin >> definedListOperation;

			return definedListOperation;
		}

		void printAttractionsList(){
			ListIterator listIterator = listManager.getNewListIterator();
			cout << "A lista de atrações é:" << endl;

			printAttractionElement(listIterator.getFirstElement());

			while(listIterator.hasNextElement()){

			}

			cout << "Fim da lista" <<endl;
		}

		void printAttractionElement(ListElementInformation touristAttraction){

		}

		ListManager listManager;
		char definedListOperation;
};



