import sys
sys.path.insert(0, '/home/vector/PromoteProjects/SoftIndustri/src/')

# from pyPullgerFootPrint.com.linkedin import authorization as linkedinAuthorizationFootPrint
from squirrel import SquairrelCore
from pyPullgerFootPrint.com.linkedin import authorization as linkedinAuthorizationFootPrint
from pyPullgerFootPrint.com.linkedin.search import people as linkedinSearchPeopleFootPrint
from pyPullgerFootPrint.com.linkedin.people import card as linkedinPeopleCardFootPrint
import time

class Domain:
    #languageWeb = None;
    #driver = None;
    authorizated = None
    squirrel = None
    RootLoaded = None
    
    def __init__(self):
        self.squirrel = SquairrelCore.Squirrel('selenium')
        self.squirrel.initialize()

    def connect(self):
        self.squirrel.get('https://www.linkedin.com/')
        self.RootLoaded = True

    def authorization(self, inUserName, inPassword):
        if self.RootLoaded != True:
            self.connect()

        if self.RootLoaded == True:
            AuthorizationResult = linkedinAuthorizationFootPrint.setUserName(self.squirrel, inUserName);

            if AuthorizationResult == True:
                AuthorizationResult = linkedinAuthorizationFootPrint.setPassword(self.squirrel, inPassword);

                if AuthorizationResult == True:
                    AuthorizationResult = linkedinAuthorizationFootPrint.singIn(self.squirrel);

            self.authorizated = AuthorizationResult

        return self.authorizated;

    def isPageCorrect(self):
        isError = True

        errorSection = self.squirrel.find_XPATH('//section[@class="global-error artdeco-empty-state ember-view"]')
        if errorSection != None:
            isError = False;

        return isError


    def search(self, searchScope, locationsArray, keywords):
        geoUrn = '';
        prefixRequest = '&'

        if len(locationsArray) != 0:
            geoUrn = 'geoUrn=%5B'

        prefix = '';
        for curLocation in locationsArray:
            geoUrn = geoUrn + prefix + '"' + str(curLocation) + '"'
            prefix = '%2C'

        if geoUrn != "":
            geoUrn = geoUrn + '%5D'

        url = "https://www.linkedin.com/search/results/" + searchScope + "/?origin=FACETED_SEARCH"
        if geoUrn != '':
            url = url + prefixRequest + geoUrn

        url = url + prefixRequest + 'keywords=' + keywords

        self.squirrel.get(url)

        return True;

    def getCountOfResults(self):
        return linkedinSearchPeopleFootPrint.getCountOfResults(self.squirrel);

    def getListOfPeoples(self):
        return linkedinSearchPeopleFootPrint.getListOfPeoples(self.squirrel);

    def listOfPeopleNext(self):
        result = None;

        self.squirrel.send_PAGE_DOWN()
        time.sleep(1)
        self.squirrel.send_PAGE_DOWN()
        time.sleep(1)

        CurPagination = linkedinSearchPeopleFootPrint.getNumberCurentPaginationPage(self.squirrel)
        LastPagination = linkedinSearchPeopleFootPrint.getNumberLastPaginationPage(self.squirrel)
        if CurPagination != None and LastPagination != None:
            if CurPagination < LastPagination:
                result = linkedinSearchPeopleFootPrint.pushNextPaginationButton(self.squirrel)
            else:
                result = False;
        return result

    #     pass
        #linkedinSearchPeopleFootPrint
        #return linkedinSearchPeopleFootPrint.pushNextPaginationButton(self.squirrel);

    def getPerson(self, url):
        self.squirrel.get(url)

    def getListOfExperience(self):
        time.sleep(1)
        self.squirrel.send_PAGE_DOWN()
        time.sleep(1)
        self.squirrel.send_PAGE_DOWN()
        time.sleep(1)
        return linkedinPeopleCardFootPrint.getListOfExperience(self.squirrel);

    def close(self):
        self.squirrel.close();



class _Hotel:
    id = None;
    country = None;
    languageWeb = None;
    reviewCount = None;
    squirrel = None;
    
    def __init__(self, squirrel, country, languageWeb, idHotelName):
        self.country = country;
        self.languageWeb = languageWeb;
        self.id = idHotelName;
        self.squirrel = squirrel;
        
        url = 'https://www.booking.com/hotel/' + country.id + '/' + idHotelName + '.' + languageWeb.id + '.html';
        #self.driver.execute_script('window.location.href = "' + url + '"');
        #driver.get('https://www.booking.com/hotel/' + country.id + '/' + idHotelName + '.' + languageWeb.id + '.html');
        self.squirrel.get(url)
        self.reviewCount = bookingHotelsFootPrint.getReviewCount(self.squirrel);

    def fetchReviews(self):
        return FetchReview(self.squirrel, self);

class Review:
    hotel = None
    userName = None;
    uuid_reviews = None;
    post_date = None;
    rate = None;
    review_good = None;
    review_good_lang = None;
    review_bad = None;
    review_bad_lang = None;
    
    _squirrel = None;
    _url = None;
    _listOfReviews = None;
    
    def __init__(self, squirrel, hotel):
        self._squirrel = squirrel;
        self._url = self._squirrel.current_url;
        self.hotel = hotel;
    
    def getReviewByCountOnPage(self, countOnPage):
        if self._listOfReviews == None or self._url != self._squirrel.current_url:
            self._listOfReviews = bookingReviewsFootPrint.getListOfReviews(self._squirrel)
            self._url = self._squirrel.current_url
        
        if self._listOfReviews == None:
            return None;
        elif len(self._listOfReviews) == 0:
            return None;
        else:
            elReviews = self._listOfReviews[countOnPage];
            self.userName = elReviews["name"];
            self.uuid_reviews = elReviews["uuid_reviews"];
            self.post_date = elReviews["post_date"];
            self.rate = elReviews["rate"];
            self.review_good = elReviews["review_good"];
            self.review_good_lang = Language(elReviews["review_good_lang"]);
            self.review_bad = elReviews["review_bad"];
            self.review_bad_lang = Language(elReviews["review_bad_lang"]);

            return True;  

class FetchReview:
    squirrel = None;
    curentNum = None;
    el = None;
    _curentNumOnPagination = None;
    _countReviewOnCurentPagination = None;
    
    def __new__(cls, squirrel, hotel):
        cls.squirrel = squirrel;
        
        url = 'https://www.booking.com/reviewlist.' + hotel.languageWeb.id + '.html?cc1=' + hotel.country.id + '&pagename=' + hotel.id + ';sort=f_recent_desc';
        #cls.driver.execute_script('window.location.href = "' + url + '"');
        #cls.driver.get('https://www.booking.com/reviewlist.' + hotel.languageWeb.id + '.html?cc1=' + hotel.country.id + '&pagename=' + hotel.id + ';sort=f_recent_desc');
        cls.squirrel.get(url);

        cls._countReviewOnCurentPagination = bookingReviewsFootPrint.getCountOfReviewsElements(cls.squirrel);
        
        if cls._countReviewOnCurentPagination != 0:
            cls.el = Review(cls.squirrel, hotel);
        
        if cls.el == None:
            return None;
        else:
            return super().__new__(cls)
    '''  
    def __init__(self, driver, hotel):
        test = 1;
    '''
        
    def next(self):
        if self.curentNum == None:
            self.curentNum = 0;
            self._curentNumOnPagination = 0;
        else:
            self.curentNum += 1;
            self._curentNumOnPagination += 1;
            if (self._curentNumOnPagination + 1) > self._countReviewOnCurentPagination:
                self._curentNumOnPagination = 0;
                if bookingReviewsFootPrint.goToNextPaginationPage(self.squirrel) == True:
                    self._countReviewOnCurentPagination = bookingReviewsFootPrint.getCountOfReviewsElements(self.squirrel);
                else:
                    self.curentNum -= 1
                    return False;
         
        resultStatus = self.el.getReviewByCountOnPage(self._curentNumOnPagination);
        
        if resultStatus != True:
            raise Exception('Error in Fetch-Next');
        
        return True;

class Country:
    id = None;
    idCountryISO = None;
    
    def __init__(self, idCountryISO):
        self.id = idCountryISO;
        self.idCountryISO = idCountryISO;

class LanguageWeb:
    id = None;
    link = None;
    
    def __init__(self, idLanguageWebName):
        self.id = idLanguageWebName;
        self.link = self;
        
class Language:
    idLanguageISO = None;
    
    def __init__(self, idLanguageISO):
        self.idLanguageISO = idLanguageISO;
        
    def __str__(self):
        if self.idLanguageISO == None:
            return "";
        else: 
            return self.idLanguageISO

def bb(a,b):
    return a + b;

#test = Hotel("df");
