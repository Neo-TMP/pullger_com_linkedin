class Squirrel:
    genus = None
    type = None
    driver = None
    Keys = None
    By = None
    current_url = None

    def __init__(self, inGenus, inType=None):
        self.genus = inGenus
        self.type = inType

    def initialize(self):
        if self.genus == 'selenium':
            import undetected_chromedriver.v2 as uc
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.common.by import By

            chrome_options = uc.ChromeOptions()

            # chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--profile-directory=Default")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--user_agent=DN")
            chrome_options.add_argument('--no-first-run')
            chrome_options.add_argument('--no-service-autorun')
            chrome_options.add_argument('--password-store=basic')

            try:
                self.driver = uc.Chrome(options=chrome_options)
                self.Keys = Keys
                self.By = By
            except Exception as Err:
                print("ERROR ERROR ERROR")
                #raise CriticalErrorInitialization(Err)

    def get(self, inURL = None, **kwargs):
        result = None

        url = inURL
        #Used for whait for render
        timeout = None
        xpath = None
        readyState = None

        if 'url' in kwargs:
            url = kwargs['url']
        if 'timeout' in kwargs:
            timeout = kwargs['timeout']
        if 'xpath' in kwargs:
            xpath = kwargs['xpath']
        if 'readyState' in kwargs:
            readyState = kwargs['readyState']


        if url != None:
            if self.genus == 'selenium':
                self.driver.execute_script("window.location.href='" + url + "'");
                self.current_url = self.driver.current_url
                #Whait for render page with timing out
                import time
                if timeout == None:
                    timeout = 5;
                isRendered = False
                circleCalc = 0

                if readyState != None:
                    curState = self.driver.execute_script('return document.readyState');

                    while isRendered == False and (circleCalc < timeout or isRendered == True):
                        if readyState == curState:
                            isRendered = True

                        if isRendered == False:
                            time.sleep(1)
                        circleCalc += 1

                    result = isRendered

                elif xpath != None:
                    while isRendered == False and (circleCalc < timeout or isRendered == True):
                        CheckBlock = self.find_XPATH(xpath)
                        if CheckBlock != None:
                            isRendered = True
                        if isRendered == False:
                            time.sleep(1)
                        circleCalc += 1

                    result = isRendered
                else:
                    result = True

        return result

    def close(self):
        if self.genus == 'selenium':
            self.driver.close();

    def finds_XPATH(self, inXPATH):
        if self.genus == 'selenium':
            returnLst = [];

            for el in self.driver.find_elements(self.By.XPATH, inXPATH):
                returnLst.append(WebElements(self.genus, self.driver, el));

            return  returnLst

    def find_XPATH(self, inXPATH):
        if self.genus == 'selenium':
            try:
                fEl = self.driver.find_element(self.By.XPATH, inXPATH);
                returnEL = WebElements(self.genus, self.driver, fEl)
            except:
                returnEL = None;

            return returnEL

    def send_PAGE_DOWN(self):
        result = None

        try:
            self.driver.find_element(self.By.XPATH, "//body").send_keys(self.Keys.PAGE_DOWN)
            result = True;
        except:
            pass

        return result;


class WebElements:
    genus = None
    driver = None
    selWebElement = None;

    text = '';

    def __init__(self, inGenus, inDriver, inSelWebElement):
        self.genus = inGenus
        self.driver = inDriver
        self.selWebElement = inSelWebElement

    def finds_XPATH(self, inXPATH):
        if self.genus == 'selenium':
            from selenium.webdriver.common.by import By
            returnLst = [];

            for el in self.selWebElement.find_elements(By.XPATH, inXPATH):
                returnLst.append(WebElements(self.genus, self.driver, el));

            return  returnLst

    def find_XPATH(self, inXPATH):
        if self.genus == 'selenium':
            from selenium.webdriver.common.by import By

            try:
                fEl = self.selWebElement.find_element(By.XPATH, inXPATH)
                returnEL = WebElements(self.genus, self.driver, fEl)
            except:
                returnEL = None;

            return returnEL;

    @property
    def text(self):
        return self.selWebElement.text;

    @property
    def tag_name(self):
        return self.selWebElement.tag_name;

    def get_attribute(self, inAttribute):
        return self.selWebElement.get_attribute(inAttribute)

    def send_string(self, inString):
        self.selWebElement.send_keys(inString);

        return True;

    def click(self):
        self.selWebElement.click();

        return True;
