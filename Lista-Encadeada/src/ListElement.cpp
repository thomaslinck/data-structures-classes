class ListElementInformation{ // @suppress("Class has a virtual method and non-virtual destructor")
	public:
		virtual void doNothing(){}
};

class ListManager{

	public:
		void createNewList(){
			listHeader = NULL;
		}

		void addNewElementInTheBegginingOfList(ListElementInformation listElementInformation){
			ListElementPointer newListMember = (ListElementPointer) malloc(sizeof(TouristAttractionInformation));

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
