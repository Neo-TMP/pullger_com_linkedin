import requests
import sys

server = 'localhost'
port = 8000

def getAPI_ENDPOINT(InMetod):
        return 'http://' + server + ':' + str(port) + '/tb/api/' + InMetod;

if len(sys.argv) == 4:
        method = sys.argv[1]
        user = sys.argv[2]
        passwprd = sys.argv[3]

        print('Metod:',method,'User:',user,'Password:',passwprd)

        # defining the api-endpoint

        if method == 'addDemo1':
                API_ENDPOINT = getAPI_ENDPOINT('create-task-interval');

                data = {'id_name': "demo_interval"
                        ,'name': 'Demo interval'
                        ,'type': "simple"
                        ,'max_instances': 1
                        ,'trigger_type': "interval"
                        ,'trigger_interval_weeks': None
                        ,'trigger_interval_days': None
                        ,'trigger_interval_hours': None
                        ,'trigger_interval_minutes': None
                        ,'trigger_interval_seconds': 5
                        ,'task_app_name': "djTaskBrocker"
                        ,'task_module_name': "Demo.demoSingleReglament"
                        ,'task_function_name': "Print"
                        }

                result = requests.post(url=API_ENDPOINT, data=data, auth=(user, passwprd))
                Information = result.text;
        elif method == 'stopDemo1':
                # DOC: https://djtaskbrocker.readthedocs.io/en/latest/apirest.html#stop-job-by-name
                API_ENDPOINT = getAPI_ENDPOINT('stop-job-by-name');

                data = {
                        'id_name': "demo_interval",
                        }
                result = requests.post(url=API_ENDPOINT, data=data, auth=(user, passwprd))
                Information = result.text;
        elif method == 'startDemo1':
                # DOC: https://djtaskbrocker.readthedocs.io/en/latest/apirest.html#start-job-by-name
                API_ENDPOINT = getAPI_ENDPOINT('start-job-by-name');

                data = {
                        'id_name': "demo_interval",
                }
                result = requests.post(url=API_ENDPOINT, data=data, auth=(user, passwprd))
                Information = result.text;
        elif method == 'delDemo1':
                # DOC: https://djtaskbrocker.readthedocs.io/en/latest/apirest.html#delete-task-job-by-name
                API_ENDPOINT = getAPI_ENDPOINT('delete-task-job-by-name');

                data = {
                        'id_name': "demo_interval",
                }
                result = requests.post(url=API_ENDPOINT, data=data, auth=(user, passwprd))
                Information = result.text;
        else:
                Information = 'Error. unknown metod:' + method;

        print(Information)
else:
        print('Incorrect number of parameters. Correct form: [' + __file__ + ' [addDemo1, stopDemo1, delDemo1, startDemo1] user password]. Example: ['+__file__+'] addDemo1 myName myPassword')