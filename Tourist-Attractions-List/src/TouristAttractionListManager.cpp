/*
 * TouristAttractionListManager.cpp
 *
 *  Created on: Mar 27, 2021
 *      Author: i532371
 */

#include <iostream>
#include <string.h>
#include "TypesDefinition.hpp""

using namespace std;

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

	bool positionInNextElementIfExists(){
		if(currentElement->nextTouristAttractionListElement != NULL){
			currentElement = currentElement->nextTouristAttractionListElement;
			return true;
		}
		else return false;
	}

	TouristAttractionListElementPointer getCurrentElement(){
		return currentElement;
	}

	void resetCurrentElement(){
		currentElement = listHeader;
	}

	TouristAttractionListElementPointer getElementWhere(string description){
		resetCurrentElement();
		do {
			if(strcmp(currentElement->touristAttractionInformation.description.c_str(), description.c_str()) == 0)
				return currentElement;
		}
		while(positionInNextElementIfExists());

		throw "Atração não cadastrada";
	};

private:
	TouristAttractionListElementPointer listHeader;
	TouristAttractionListElementPointer currentElement;

};

