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

	private:
		TouristAttractionPointer listHeader;

};


int main() {

	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!

	return 0;
}
