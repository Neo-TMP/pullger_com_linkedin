from djPullgerReflection.com_linkedin import metods

def test1():
    import sys

    sys.path.insert(0, '/home/vector/PromoteProjects/SoftIndustri/src/')

    from pyPullgerDomain.com.linkedin import port as linkedinPORT
    import time


    new = linkedinPORT.Domain();

    time.sleep(2)
    #AuthorizationResult = new.authorization('k.kovalenko@bukovel.com', '137a8f2e37')
    AuthorizationResult = new.authorization('kkovalenko.sphere@outlook.com', 'bebb90cbf2')
    if AuthorizationResult == True:
        #101728296 #Russia
        #104994045 #Moscow City, Russia
        #106686604 #StPetersburg City, Russia
        #104359155 #Moscow, Russia
        #103752778 #Yaroslavl’, Russia
        #103574901 #Sverdlovsk, Russia
        #105303715 #Krasnodar, Russia
        #100020981 #Rostov, Russia
        #102917175 #Tatarstan, Russia
        #101777369 #Novosibirsk, Russia
        #103249458 #Samara, Russia
        #104523009 #Chelyabinsk, Russia
        #100827052 #Nizhniy Novgorod, Russia
        #102734387 #Bashkortostan, Russia
        #107992632 #Novosibirsk, Novosibirsk, Russia
        #107062619 #Perm, Russia
        #100367933 #Yekaterinburg, Sverdlovsk, Russia
        #100674497 #Krasnoyarsk, Russia
        #102450862 #Rostov, Rostov, Russia
        #101631519 #Kazan, Tatarstan, Russia

        locations = [100020981]
        resGetData = new.search('people', locations, ".NET")

        if resGetData == True:
            countResults = new.getCountOfResults();

            EndOfSearch = False;

            while EndOfSearch == False:
                time.sleep(4)
                listOfPersons = new.getListOfPeoples();
                print('List get: ' + str(len(listOfPersons)));

                for elOfList in listOfPersons:
                    metods.addPeople(**elOfList);

                if new.listOfPeopleNext() != True:
                    EndOfSearch = True;
                # EndOfSearch = True;

    #new.close();

'''
from djPullgerReflection.com_linkedin import tests
dl = tests.test1()

import importlib
from pyPullgerFootPrint.com.linkedin.search import people
importlib.reload(people)

people.getNumberCurentPaginationPage(dl.squirrel)
'''


def test2():
    import sys

    sys.path.insert(0, '/home/vector/PromoteProjects/SoftIndustri/src/')

    from pyPullgerDomain.com.linkedin import port as linkedinPORT
    import time

    new = linkedinPORT.Domain();

    AuthorizationResult = new.authorization('kkovalenko.sphere@outlook.com', 'bebb90cbf2')

    CardsArray = metods.getAllPersons(date_loaded=None)

    for CurCardPeople in CardsArray:
        new.getPerson(CurCardPeople.url)
        experieneceList = new.getListOfExperience()

        metods.delExperiences(uuid=CurCardPeople.uuid)
        errorsInLoop = False

        for curExperienece in experieneceList:
            newCompanyDict = {
                "id" : curExperienece['companyID'],
                "name": curExperienece['companyName'],
                "url": curExperienece['companyURL']
            }
            newCompany = metods.addCompany(**newCompanyDict)

            newPeopleExperienceDict = {
                "job_discription": curExperienece['job_discription'],
                "job_timing_type": curExperienece['job_timing_type']
            }
            resAddExperience = metods.addPeopleExperience(CurCardPeople, newCompany, **newPeopleExperienceDict)
            if resAddExperience == None:
                errorsInLoop = True;

        if errorsInLoop == False:
            metods.updateFullLoadDatePeople(people = CurCardPeople)


    new.close();

'''
from djPullgerReflection.com_linkedin import tests
tests.test2()
'''

def test3():
    from djPullgerReflection.com_linkedin import metods

    print(metods.getAllCompanies());

    metods.delCompanyByUUID("872b3e52-ef3e-11ec-8ee2-d5c4034c4de5")

    # ddt = { "id": 234 };
    # metods.addCompany(**ddt)

'''
from djPullgerReflection.com_linkedin import tests
tests.test3()
'''

def bc():
    from pyPullgerDomain.com.linkedin.port import port as linkedinPORT

    new = linkedinPORT.Domain();

    new.authorization('kkovalenko.sphere@outlook.com', 'bebb90cbf2')

    return new

#from pyPullgerDomain.com.linkedin import port


def colectCompanies():
    from djPullgerReflection.com_linkedin.models import companies

    # authorization = {
    #     'user' : 'kkovalenko.sphere@outlook.com',
    #     'password' : 'bebb90cbf2'
    # }

    i = 1
    limit = 10

    from pyPullgerDomain.com.linkedin import port as linkedinPORT
    rootDomain = linkedinPORT.Domain();
    rootDomain.authorization('kkovalenko.sphere@outlook.com', 'bebb90cbf2')

    listCompanies = companies.objects.getList(date_full_loaded__lte = None)
    for curCompny in listCompanies:
        curCompny.domainConnection(root = rootDomain)
        curCompny.updateDATA()
        if i >= limit:
            break
        i += 1

'''
from djPullgerReflection.com_linkedin import tests
tests.colectCompanies()
'''

'''
from djPullgerReflection.com_linkedin.models import companies
ob = companies.objects.all()
cob = ob[3]
cob.domainConnection(user='kkovalenko.sphere@outlook.com', password='bebb90cbf2')

cob.reloadFunctions()
cob.updateDATA()

from pyPullgerFootPrint.com.linkedin.company import card
import importlib

importlib.reload(card)
card.getAboutData(squirrel=cob.domain.squirrel)

'''


'''
from djPullgerReflection.com_linkedin import tests
tests.colectCompanies()
'''


'''
from djPullgerReflection.com_linkedin.models import companies
companies().aa()


import importlib
importlib.reload(models_companies_functions)
'''

'''
from djPullgerReflection.com_linkedin.models import models_companies_functions

import importlib
importlib.reload(models_companies_functions)
models_companies_functions.aa()
'''

'''
from djPullgerReflection.com_linkedin import tests
rd = tests.bc()
import importlib
from pyPullgerDomain.com.linkedin.port import port_companies
CD = port_companies.CompanyDomain(root=rd)
CD.setCompany(id=2980493)
CD.goToAbout()


importlib.reload(port_companies)
CD = port_companies.CompanyDomain(root=rd)
CD.setCompany(id=27152955)
CD.goToAbout()

CD.goToAbout()

from pyPullgerFootPrint.com.linkedin.company import card
card.getID(squirrel=CD.squirrel)
card.getNick(squirrel=CD.squirrel)
card.getAbout(squirrel=CD.squirrel)


from pyPullgerFootPrint.com.linkedin.company import card
card.getAboutData(squirrel=CD.squirrel)
importlib.reload(card)
card.getLocations(squirrel=CD.squirrel)
'''
