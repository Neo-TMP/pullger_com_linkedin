'''
    dataList = List.find_elements(By.XPATH, ".//td");

    for elReviewRow in dataList:
        print(elReviewRow.text)

    return List
'''


'''
summary
Data from the Selected Registers

//*[@id="fichaSinPest"]/table[1]
/html/body/div/div/div[6]/div/div/div[1]/div[2]/blockquote/div[2]/div/table[1]
'''


    #test = 9;
    #return test;
from selenium.webdriver.common.by import By

def getPersonCard(squirrel):

    PersonData = {};

    PersonData["fullname"] = None;
    PersonData["DateOfBirth"] = None;
    PersonData["PlaceOfBirth"] = None;
    PersonData["Nationality"] = None;
    PersonData["Sex"] = None;
    PersonData["Age"] = None;
    PersonData["Occupations"] = None;
    PersonData["Exiled"] = None;
    PersonData["LastResidence"] = None;

    PersonData["PlaceOfArrival"] = None;
    PersonData["DateOfArrival"] = None;

    PersonData["RepositoryCode"] = None;
    PersonData["SignatureOfTheDigitalObject"] = None;
    PersonData["ArchiveGroup"] = None;
    PersonData["Title"] = None;
    PersonData["Creator"] = None;
    PersonData["StartDate"] = None;
    PersonData["EndDate"] = None;
    PersonData["ExistenceAndLocation"] = None;

    List = squirrel.finds_XPATH("//*[@id='fichaSinPest']/table");
    #List = squirrel.driver.find_elements(By.XPATH, "//*[@id='fichaSinPest']/table");
    #print(List);

    for elReviewRow in List:
        #dataList = elReviewRow.find_elements(By.XPATH, ".//tr");
        dataList = elReviewRow.finds_XPATH(".//tr");

        for elDataList in dataList:
            try:
                #fEL = elDataList.find_element(By.XPATH, ".//th")
                fEL = elDataList.find_XPATH(".//th")

                if fEL != None:
                    #print(fEL)
                    nameOfRowEl =  fEL.text;
                    value = elDataList.find_XPATH(".//td")

                    if value != None:
                        #print(value.text);
                        if nameOfRowEl == 'Surname(s) and first name':
                            PersonData["fullname"] = value.text
                            #print("+1: " + value.text)
                        elif nameOfRowEl == 'Date of birth':
                            PersonData["DateOfBirth"] = value.text
                            #print("+2: " + value.text)
                        elif nameOfRowEl == 'Place of birth':
                            PersonData["PlaceOfBirth"] = value.text
                            #print("+3: " + value.text)
                        elif nameOfRowEl == 'Nationality':
                            PersonData["Nationality"] = value.text
                            #print("+4: " + value.text)
                        elif nameOfRowEl == 'Sex':
                            PersonData["Sex"] = value.text
                            #print("+5: " + value.text)
                        elif nameOfRowEl == 'Age':
                            PersonData["Age"] = value.text
                            #print("+6: " + value.text)
                        elif nameOfRowEl == 'Occupations':
                            PersonData["Occupations"] = value.text
                            #print("+7: " + value.text)
                        elif nameOfRowEl == 'Exiled':
                            PersonData["Exiled"] = value.text
                            #print("+8: " + value.text)
                        elif nameOfRowEl == 'Last residence':
                            PersonData["LastResidence"] = value.text
                            #print("+9: " + value.text)
                        elif nameOfRowEl == 'Place of arrival':
                            PersonData["PlaceOfArrival"] = value.text
                            #print("+10: " + value.text)
                        elif nameOfRowEl == 'Date of arrival':
                            PersonData["DateOfArrival"] = value.text
                            #print("+11: " + value.text)
                        elif nameOfRowEl == 'Repository code':
                            PersonData["RepositoryCode"] = value.text
                            #print("+12: " + value.text)
                        elif nameOfRowEl == 'Signature of the digital object':
                            PersonData["SignatureOfTheDigitalObject"] = value.text
                            #print("+13: " + value.text)
                        elif nameOfRowEl == 'Archive group':
                            PersonData["ArchiveGroup"] = value.text
                            #print("+14: " + value.text)
                        elif nameOfRowEl == 'Series':
                            test = 1
                        elif nameOfRowEl == 'Title':
                            PersonData["Title"] = value.text
                            #print("+15: " + value.text)
                        elif nameOfRowEl == 'Creator':
                            PersonData["Creator"] = value.text
                            #print("+16: " + value.text)
                        elif nameOfRowEl == 'Start date':
                            PersonData["StartDate"] = value.text
                            #print("+17: " + value.text)
                        elif nameOfRowEl == 'End date':
                            PersonData["EndDate"] = value.text
                            #print("+18: " + value.text)
                        elif nameOfRowEl == 'Volume':
                            test = 1
                        elif nameOfRowEl == 'Existence and location of originals':
                            PersonData["ExistenceAndLocation"] = value.text
                            #print("+19: " + value.text)
                        else:
                            #print('Error, no element:')
                            #print(nameOfRowEl)

                    #print(nameOfRowEl);
            except:
                print('error')

    #print(PersonData)

    return PersonData