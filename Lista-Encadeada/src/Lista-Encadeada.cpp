//============================================================================
// Name        : Lista-Encadeada.cpp
// Author      : Thomas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

typedef struct TouristAttractionInformation{
	string description;
	float latitude;
	float longitude;

}TouristAttractionInformation;

typedef struct TouristAttractionListElement{
	TouristAttractionInformation touristAttractionInformation;
	struct TouristAttractionListElement * nextTouristAttractionListElement;
}TouristAttractionListElement;

typedef TouristAttractionListElement * TouristAttractionListElementPointer;


class TouristAttractionsListManager{

	public:
	TouristAttractionListElementPointer createNewList(){
			return NULL;
		}

		void setHeaderToExistingList(TouristAttractionListElementPointer existingListHeader){
			listHeader = existingListHeader;
		}

		void addNewAttractionInBegginingOfList(TouristAttractionInformation touristAttractionInformation){
			TouristAttractionListElementPointer newListMember = (TouristAttractionListElementPointer) malloc(sizeof(TouristAttractionInformation));

			newListMember->touristAttractionInformation = touristAttractionInformation;
			newListMember->nextTouristAttractionListElement = listHeader;

			listHeader = newListMember;
		}

	private:
		TouristAttractionListElementPointer listHeader;

};

class Application{
	public:

		Application(){
			touristAttractionsListManager.createNewList();
		}

		void execute(){
			while (defineListOperation() == '1'){
				touristAttractionsListManager.
					addNewAttractionInBegginingOfList(
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

		TouristAttractionsListManager touristAttractionsListManager;
};


int main() {

	Application application;

	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!

	application.execute();

	return 0;
}
