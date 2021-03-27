/*
 * TypesDefinition.hpp
 *
 *  Created on: Mar 27, 2021
 *      Author: i532371
 */

#ifndef TYPESDEFINITION_HPP_
#define TYPESDEFINITION_HPP_

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



#endif /* TYPESDEFINITION_HPP_ */
