
using namespace std;

class ListElementInformation{ // @suppress("Class has a virtual method and non-virtual destructor")
	public:
		virtual void doNothing(){}
};


class ListIterator{ // @suppress("Class has a virtual method and non-virtual destructor")
	public:
		virtual bool hasNextElement(){return false;};
		virtual ListElementInformation getNextElement(){return NULL;};

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

	private:

		typedef struct ListElement{
			ListElementInformation listElementInformation;
			ListElement * nextListElement;
		}ListElement;

		typedef ListElement * ListElementPointer;

		ListElementPointer listHeader;

};
