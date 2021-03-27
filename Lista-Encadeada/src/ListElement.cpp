

#include <iostream>
using namespace std;

class ListElementInformation{ // @suppress("Class has a virtual method and non-virtual destructor")
	public:
		virtual void doNothing(){}
};


class ListIterator{ // @suppress("Class has a virtual method and non-virtual destructor")
	public:
		virtual bool hasNextElement(){} // @suppress("No return")
		virtual ListElementInformation getNextElement(){} // @suppress("No return")
};

class ListManager{

	public:
		void createNewList(){
			listHeader = NULL;
		}

		void addNewElementInTheBegginingOfList(ListElementInformation listElementInformation){
			ListElementPointer newListMember = (ListElementPointer) malloc(sizeof(listElementInformation)+sizeof(listHeader));

			newListMember->listElementInformation = listElementInformation;
			newListMember->nextListElement = listHeader;

			listHeader = newListMember;
		}

		ListIterator getNewListIterator(){
			ConcreteListIterator listIterator(listHeader);
			return listIterator;
		};

	private:

		typedef struct ListElement{
			ListElementInformation listElementInformation;
			ListElement * nextListElement;
		}ListElement;

		typedef ListElement * ListElementPointer;

		ListElementPointer listHeader;

		class ConcreteListIterator: public ListIterator{ // @suppress("Class has a virtual method and non-virtual destructor")
			public:
				ConcreteListIterator(ListElementPointer firstElement){
					this->firstElement = firstElement;
					this->currentElement = firstElement;

				}

				bool hasNextElement(){
					return true;
				};

				ListElementInformation getNextElement(){
					ListElementInformation listElementInformation;
					return listElementInformation;
				};

			private:
				ListElementPointer firstElement;
				ListElementPointer currentElement;

		};

};
