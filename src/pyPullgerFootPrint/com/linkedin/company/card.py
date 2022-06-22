def goToAbout(**kwargs):
    squirrel = None
    result = None

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        sectionNavigation = squirrel.find_XPATH('//ul[@class="org-page-navigation__items "]')
        if sectionNavigation != None:
            result = 'ok'
            # sectionNavigation = squirrel.finds_XPATH('.//a')
            # for curSection

    return result

def getOverview(inSquirrel = None, **kwargs):
    squirrel = inSquirrel
    result = None

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        overviewCard = squirrel.find_XPATH('//section[@class="artdeco-card p5 mb4"]')
        if overviewCard != None:
            overviewSection = overviewCard.find_XPATH('.//p')
            if overviewSection != None:
                result = overviewSection.text
    return result

def getID(**kwargs):
    squirrel = None
    result = None

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        res1 = squirrel.find_XPATH('//*[@data-entity-hovercard-id]')
        if res1 != None:
            entityList = res1.get_attribute('data-entity-hovercard-id').split(":")
            if len(entityList) == 4:
                try:
                    result = int(entityList[3])
                except:
                    pass

    return result

def getNick(**kwargs):
    squirrel = None
    result = None

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        navigateBlock = squirrel.find_XPATH('//ul[@class="org-page-navigation__items "]')
        if navigateBlock != None:
            navButton = navigateBlock.find_XPATH('.//a')
            if navButton != None:
                href = navButton.get_attribute('href')
                if href != None:
                    hrefSplited = list(filter(None, href.split("/")))
                    if len(hrefSplited) >= 2:
                        result = hrefSplited[3]

    return result

def getLocations(inSquirrel=None, **kwargs):
    squirrel = inSquirrel
    result = []

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        locationsList = squirrel.finds_XPATH('//p[@class="t-14 t-black--light t-normal break-words"]')
        for curLocation in locationsList:
            result.append(curLocation.text)

    return result



def getAboutData(**kwargs):
    squirrel = None
    result = None

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        structureAbout = {
            'NAME': None,
            'DISCRIPTION': None,
            'LOCATION_NAME': None,
            'FOLLOWERS': None,
            'OVERVIEW': None,
            'WEBSITE': None,
            'INDUSTRY': None,
            'COMPANY_SIZE': None,
            'EMPLOYEE_LINKEDIN': None,
            'HEADQUARTERS': None,
            'FOUNDED': None,
            'SPECIALITIES': None,
            'LOCATIONS': None
        }

        headSegment = squirrel.find_XPATH('//div[@class="block mt2"]')
        if headSegment != None:
            NameTag = headSegment.find_XPATH('.//h1')
            if NameTag != None:
                structureAbout['NAME'] = NameTag.text

            DiscriptionTag = headSegment.find_XPATH('.//p')
            if DiscriptionTag != None:
                structureAbout['DISCRIPTION'] = DiscriptionTag.text

            MainInfoSegment = headSegment.find_XPATH('.//div[@class="org-top-card-summary-info-list t-14 t-black--light"]/div[@class="inline-block"]')
            if MainInfoSegment != None:
                MainSegments = MainInfoSegment.finds_XPATH('./div')
                i = 1
                for curMainInformation in MainSegments:
                    if i == 1:
                        structureAbout['LOCATION_NAME'] = curMainInformation.text
                    elif i == 2:
                        followersText = curMainInformation.text
                        if type(followersText) == str:
                            followersSplited = followersText.split(' ')
                            try:
                                structureAbout['FOLLOWERS'] = int(followersSplited[0].replace(',',''))
                            except:
                                pass
                    else:
                        break
                    i += 1

        structureAbout['OVERVIEW'] = getOverview(squirrel = squirrel)

        overviewCard = squirrel.find_XPATH('//dl[@class="overflow-hidden"]')
        if overviewCard != None:

            aboutSections = overviewCard.finds_XPATH('./*')
            curentSection = None;

            for aboutElement in aboutSections:
                if aboutElement.tag_name == 'dt':
                    curentSection = aboutElement.text.upper();
                elif aboutElement.tag_name == 'dd':
                    if curentSection == 'WEBSITE':
                        linckElement = aboutElement.find_XPATH('.//a')
                        if linckElement != None:
                            structureAbout[curentSection] = linckElement.get_attribute('href')
                    elif curentSection == 'INDUSTRY':
                        structureAbout[curentSection] = aboutElement.text.upper()
                    elif curentSection == 'COMPANY SIZE':
                        if aboutElement.find_XPATH('.//span'):
                            structureAbout['EMPLOYEE_LINKEDIN'] = aboutElement.text[:aboutElement.text.find('\n')]
                        else:
                            structureAbout['COMPANY_SIZE'] = aboutElement.text
                    elif curentSection == 'HEADQUARTERS':
                        structureAbout[curentSection] = aboutElement.text
                    elif curentSection == 'FOUNDED':
                        structureAbout[curentSection] = aboutElement.text
                    elif curentSection == 'SPECIALITIES':
                        listOfSpecialties = aboutElement.text.split(',')
                        structureAbout[curentSection] = [name.upper() for name in listOfSpecialties]

        structureAbout['LOCATIONS'] = getLocations(squirrel = squirrel)

        result = structureAbout

    return result