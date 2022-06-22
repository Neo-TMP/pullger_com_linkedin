def getCountOfElements(squirrel):
    resultReviewsElements = None;

    try:
        elFind = squirrel.find_XPATH('// *[ @ id = "paginatedList"] / div[3] / span[3]')
    except:
        elFind = None;

    if elFind != None:
        resultReviewsElements = int(elFind.text.replace(".",""))

    return resultReviewsElements


def getList(squirrel):

    PersonCardList = [];

    ListOfPersons = squirrel.finds_XPATH('// *[ @ id = "coleccion"] / tbody / tr')

    for elListOfPersons in ListOfPersons:
        PersonCardEl = {}
        PersonCardEl["id"] = None
        PersonCardEl["Surname"] = None
        PersonCardEl["FirstName"] = None
        PersonCardEl["YearOfBirth"] = None
        PersonCardEl["PlaceOfBirth"] = None
        PersonCardEl["PlaceOfDeparture"] = None
        PersonCardEl["PlaceOfArrival"] = None

        RowsOfPersonsList = elListOfPersons.finds_XPATH('.//td')

        irow = 1;
        for elRowsOfPersonsList in RowsOfPersonsList:
            information = elRowsOfPersonsList.text;
            if irow == 1:
                PersonCardEl["Surname"] = information;
            elif irow == 2:
                PersonCardEl["FirstName"] = information;
            elif irow == 3:
                PersonCardEl["YearOfBirth"] = information;
            elif irow == 4:
                PersonCardEl["PlaceOfBirth"] = information;
            elif irow == 5:
                PersonCardEl["PlaceOfDeparture"] = information;
            elif irow == 6:
                PersonCardEl["PlaceOfArrival"] = information;
            elif irow == 7:
                fElement = elListOfPersons.find_XPATH('.//a');

                id = None;
                if fElement != None:
                    link = fElement.get_attribute("href");

                    splited = link.split('=')
                    if len(splited) == 2:
                        try:
                            id = int(splited[1]);
                        except:
                            id = None;
                    else:
                        id = None;
                else:
                    id = None;

                PersonCardEl["id"] = id;

            irow += 1
        PersonCardList.append(PersonCardEl)
    return PersonCardList;

def 