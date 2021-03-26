//============================================================================
// Name        : Lista-Encadeada.cpp
// Author      : Thomas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

struct TouristAttractionModel{
	string description;
	float latitude;
	float longitude;
	struct TouristAttractionModel * nextTouristAttraction;
};

typedef struct TouristAttractionModel TouristAttraction;
typedef TouristAttraction * TouristAttractionPointer;

class TouristAttractionsListManager{

	public:
		TouristAttractionPointer createNewList(){
			return NULL;
		}

		void setHeaderToExistingList(TouristAttractionPointer existingListHeader){
			listHeader = existingListHeader;
		}

		void addNewTouristAttraction(TouristAttraction touristAttraction){

		}

	private:
		TouristAttractionPointer listHeader;

};

class Application{
	public:

		Application(){
			touristAttractionsListManager.createNewList();
		}

		void execute(){
			while (defineListOperation() == '1'){
				touristAttractionsListManager.
					addNewTouristAttraction(
						readTouristAttraction());
			}
		}

	private:

		TouristAttraction readTouristAttraction(){
					TouristAttraction touristAttraction;

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
