from datetime import datetime
#from django.apps import AppConfig

def Print(InArg = None):
    print("execute task at " + str(datetime.utcnow().now()))
