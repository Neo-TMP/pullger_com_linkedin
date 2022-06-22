import sys
from django.apps import AppConfig
from datetime import datetime
import os
#print(os.path.join(os.path.dirname(__file__)))
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'FixedLibs'))
from apscheduler.schedulers.background import BackgroundScheduler
from .operations import stopJob

class djTaskBrockerConfig(AppConfig):
    name = 'djTaskBrocker';
    test = 'ok ok';
    scheduler = None;

    def ready(self):
        #print("start server")
        
        if 'runserver' in sys.argv:
            #print("runing parser")
            
            self.scheduler = BackgroundScheduler()
            
            #try:
            from djTaskBrocker.models import task
            
            fetchAll = task.objects.all().filter(execute = True);
            
            print("#Step 3: " + str(len(fetchAll)))
            print(fetchAll)

            from . import operations

            for elTask in fetchAll:

                print('uuid: ' + str(elTask.uuid))
                print('Name: ' + str(elTask.name))
                print('Type: ' + str(elTask.type))
                print('Trigger_type: ' + str(elTask.trigger_type))
                print('App name: ' + str(elTask.task_app_name))
                print('Module name: ' + str(elTask.task_module_name))
                print('Function name: ' + str(elTask.task_function_name))
                print('Execute: ' + str(elTask.execute))

                operations.startJob(elTask.uuid);

            self.scheduler.start()


        '''
        from reglament.models import task
        from time import sleep
        import rpyc
        
        fetchAll = task.objects.all();
        
        for elTask in fetchAll:
            print('Name: ' + elTask.name) 
            print('UUID: ' + elTask.uuid)
            print('Module name: ' + elTask.module_name)
        
        
        print("ok 1 " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'));
        conn = rpyc.connect('localhost', 12345)
        job = conn.root.add_job('server:print_text', 'interval', args=['Hello, World'], seconds=2)
        sleep(10)
        conn.root.remove_job(job.id)        
        print("ok 2 " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'));
        '''
