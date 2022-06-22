from django.db import models
from . import models_companies_functions
from pyPullgerDomain.com.linkedin import port
import importlib

class companiesManager(models.Manager):
    testVar = None

    def getList(self, **kparams):
        if 'date_loaded' in kparams:
            return companies.objects.filter(date_full_loaded=kparams['date_loaded'])
        elif 'lte_date_loaded' in kparams:
            return companies.objects.filter(date_full_loaded__lte=kparams['lte_date_loaded'])
        else:
            return companies.objects.all()

    def printData(self):
        print(self)

class companies(models.Model):
    uuid = models.CharField(max_length=36, primary_key = True)
    id = models.IntegerField(blank=False, null=False)
    nick = models.CharField(max_length=300, null=True)
    name = models.CharField(max_length=300, null=True)

    discription = models.CharField(max_length=300, null=True)
    overview = models.TextField(null=True)

    url = models.CharField(max_length=300, null=True)
    url_company = models.CharField(max_length=300, null=True)

    industry = models.CharField(max_length=300, null=True)

    company_size = models.CharField(max_length=300, null=True)
    employee_linkedin = models.CharField(max_length=300, null=True)
    followers = models.IntegerField(blank=False, null=False)

    countryISO = models.CharField(max_length=3, null=True)
    location = models.CharField(max_length=300, null=True)
    locationNameGeneral = models.CharField(max_length=300, null=True)

    headquarter = models.CharField(max_length=300, null=True)
    founded = models.IntegerField(blank=False, null=False)

    date_small_loaded = models.DateField(null=True)
    date_full_loaded = models.DateField(null=True)

    domain = None
    objects = companiesManager()

    def __next__(self):
        print("Next")

    # Variation of kwargs
    # root
    def domainConnection(self, **kwargs):
        result = None

        if self.domain == None:
            if 'root' in kwargs:
                self.domain = port.CompanyDomain(root=kwargs['root'])
            elif 'squirrel' in kwargs:
                self.domain = port.CompanyDomain(squirrel=kwargs['squirrel'])
            else:
                self.domain = port.CompanyDomain()

        if self.domain != None:
            if self.domain.authorizated != True:
                if 'user' in kwargs and 'password' in kwargs:
                    self.domain.authorization(kwargs['user'], kwargs['password'])

            if self.domain.authorizated == True:
                self.domain.setCompany(id = self.id)
                self.domain.pullDATA()
                result = True

        return result

    @classmethod
    def domainDisconection(cls):
        cls.domain == None

    def fillDATA(self):
        result = None
        try:
            models_companies_functions.fillDATA(self)
            result = True
        except Exception as e:
            print(e)
        return result

    def updateDATA(self):
        if self.fillDATA():
            from datetime import date
            self.date_full_loaded = date.today()
            self.save()

    # def exec(self, inFunction):
    #     inFunction()

    def reloadFunctions(self):
        try:
            importlib.reload(models_companies_functions)
        except Exception as e:
            print(e)