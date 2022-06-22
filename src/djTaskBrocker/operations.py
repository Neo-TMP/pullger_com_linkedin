from datetime import datetime
import time 
from django.db.models.functions import Now
from django.apps import apps

def test_operation(arg):
    #print("test reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    #print("test reglament: " + datetime.utcnow().isoformat())
    print("#1 test reglament: " + str(datetime.utcnow().now()))
    #print(arg)
    #print("test reglament: " + Now())
    return_result = {"status":200, "message":("test" + str(arg))}
    return return_result;

def test2_operation(arg):
    
    print("step 0 reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    
    from MetaverseDomain.com.booking import port as bookingPort
    from MetaverseFootPrint.com.booking.www.pages import reviews as bookingReviews   
    import undetected_chromedriver.v2 as uc
    
    print("step 1 reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    country = bookingPort.LanguageWeb("ua")
    
    print("step 2 reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    try:
        bookingMD = bookingPort.Phantom("uk")
    except:
        print("Error") 
    
    print("step 3 reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    hotelMD = bookingMD.getHotelByIDName(country, 'marmaros')
    
    fetchHotelReview = hotelMD.fetchReviews();
    
    if fetchHotelReview != None:
        while fetchHotelReview.next():
            print("ROW [" + str(fetchHotelReview.curentNum) + "]: ");
            print("\tb" + "UUID: " + str(fetchHotelReview.el.uuid));
            print("\tb" + "Name: " + str(fetchHotelReview.el.userName));
            print("\tb" + "Post date:"  + str(fetchHotelReview.el.post_date));
            print("\tb" + "Review bad: " + str(fetchHotelReview.el.review_bad));
            print("\tb" + "Review bad language: " + str(fetchHotelReview.el.review_bad_lang));
            print("\tb" + "Review good: " + str(fetchHotelReview.el.review_good));
            print("\tb" + "Review good language: " + str(fetchHotelReview.el.review_good_lang));
    
    
            
    '''
    #print("test reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    #print("test reglament: " + datetime.utcnow().isoformat())
    print("#2 test reglament: " + str(datetime.utcnow().now()))
    print(arg)
    #print("test reglament: " + Now())
    return_result = {"status":200, "message":("test" + str(arg))}
    return return_result;
    '''

def test_multioperation(arg_task, arg_operation):
    print("#4.3: Start task")

    print("#4.4: Initialization")
    return_result = {"status": 0, "message": ""}

    '''
    #Template
    if return_result["status"] == 0: 
        try:
        except Exception, e: 
            return_result["status"] = 
            return_result["message"] = "Error initialization libraty: " + str(e);
    '''
    
    if return_result["status"] == 0: 
        try:
            #from gnFantom.com.youtube.www.pages import results as findResults
            import undetected_chromedriver.v2 as uc
            import random,time,os,sys
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.common.by import By
            import json
        except Exception as e:
            return_result["status"] = 1
            return_result["message"] = "Error initialization libraty: " + str(e);
    
    if return_result["status"] == 0: 
        try:
            print("#4.5: Parameters")
            print(arg_operation);
            
            print("#4.6: Parameters type");
            print(type(arg_operation));
            
            if type(arg_operation).__name__ == 'str':
                arg_dict = json.loads(arg_operation)
            else:
                arg_dict = {};
                
            print('#4.7: Parameters dict')
            print(arg_dict)
                
        except Exception as e: 
            return_result["status"] = 2 
            return_result["message"] = "Error in get parameters: " + str(e);
    
    if not "url" in arg_dict:
        return_result["status"] = 3 
        return_result["message"] = "No parametr 'url'";
    
    if return_result["status"] == 0: 
        chrome_options = uc.ChromeOptions()
        
        #chrome_options.add_argument("--headless")
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
        
        print("#4.4: Start chrome")
        driver = uc.Chrome(options=chrome_options)
        
        #url = 'https://www.youtube.com/results?search_query=%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D0%BB%D0%BE%D0%BC%D0%BA%D0%B8';
        url = arg_dict["url"]
        driver.execute_script('window.location.href = "' + url + '"');
        
        #driver.get('https://www.youtube.com/results?search_query=%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D0%BB%D0%BE%D0%BC%D0%BA%D0%B8');
        time.sleep(5)
        
        driver.close()
        
        
    print("End task")
    
    return return_result;

def stopJob(inUUID):
    from djTaskBrocker import models

    resultReturn = {
        'result': False
        ,'discription': 'Unknown'
    }

    reglament_app = apps.get_app_config('djTaskBrocker');
    listJobs = reglament_app.scheduler.get_jobs()

    jobExist = False;

    for curJob in listJobs:
        if curJob.id == inUUID:
            jobExist = True;
            break;

    if jobExist:
        reglament_app.scheduler.remove_job(inUUID);


        resultReturn = {
            'result': True
            , 'discription': 'Job with uuid: [' + inUUID + '] stop.'
        }
    else:
        resultReturn = {
            'result': True
            , 'discription': 'Job with uuid: [' + inUUID + '] not found.'
        }

    elTask = models.task.objects.filter(uuid=inUUID).first()
    elTask.execute = False;
    elTask.save();

    return resultReturn;

def deleteTask(inUUID):
    from djTaskBrocker import models

    elTask = models.task.objects.filter(uuid=inUUID).first()

    if elTask != None:
        if elTask.execute != True:
            reglament_app = apps.get_app_config('djTaskBrocker');
            listJobs = reglament_app.scheduler.get_jobs()

            jobExist = False;

            for curJob in listJobs:
                if curJob.id == inUUID:
                    jobExist = True;
                    break;

            if jobExist == True:
                resultReturn = {
                    'result': False
                    , 'discription': 'Job on task with <uuid>:' + inUUID + ' now runned, task can''t be deleted.'
                }
            else:
                elTask.delete();
                resultReturn = {
                    'result': True
                    , 'discription': 'Task with <uuid>:' + inUUID + ' successfully deleted.'
                }
        else:
            resultReturn = {
                'result': False
                , 'discription': 'Task with <uuid>:' + inUUID + ' now executind, and cant be deleted.'
            }
    else:
        resultReturn = {
            'result': False
            ,'discription': 'Task on DB not found'
        }
    return resultReturn;

def startJob(inUUID):

    #reglament_app = apps.get_app_config('djTaskBrocker');
    #reglament_app.scheduler.remove_job(inUUID);

    reglament_app = apps.get_app_config('djTaskBrocker');
    listJobs = reglament_app.scheduler.get_jobs()

    jobExist = False;

    for curJob in listJobs:
        if curJob.id == inUUID:
            jobExist = True;
            break;

    if not jobExist:
        resultReturn = addJob(inUUID)

        resultReturn = {
            'result': True
            , 'discription': 'Job with uuid: [' + inUUID + '] started.'
        }
    else:
        resultReturn = {
            'result': False
            , 'discription': 'Job with uuid: [' + inUUID + '] alrady started.'
        }


    return resultReturn;

def addJob(inUUID):
    from djTaskBrocker import models

    resultReturn = {
        'result': False
        ,'discription': 'Unknown'
    }

    elTask = models.task.objects.filter(uuid=inUUID).first()

    if elTask != None:
        triggerType = str(elTask.trigger_type);

        taskARG = ();
        taskARG = taskARG + (str(elTask.uuid),);
        taskARG = taskARG + (str(elTask.task_app_name),)
        taskARG = taskARG + (str(elTask.task_module_name),)
        taskARG = taskARG + (str(elTask.task_function_name),)
        taskARG = taskARG + (45,)

        parameters = {};

        for elTaskField in elTask._meta.get_fields():
            fieldName = elTaskField.name;
            # print("Len trigge type: " + str(len(triggerType)))
            # print("Row name: [" + fieldName + "] ", end = '');
            triggerTypeRow = fieldName[8:(8 + len(triggerType))]
            # print("Trigger Type ROW: {" + triggerTypeRow + "}");

            if triggerTypeRow == triggerType:
                triggerParameterName = fieldName[(8 + len(triggerType) + 1):]
                # print("Parameter Name: " + triggerParameterName);
                fieldValue = getattr(elTask, fieldName)
                if fieldValue != None:
                    parameters[triggerParameterName] = getattr(elTask, fieldName);

        print("all parameters:")  # Debug
        print(parameters)

        print("Sheduling job")  # Debug

        reglament_app = apps.get_app_config('djTaskBrocker');

        if elTask.type == 'multy':
            reglament_app.scheduler.add_job(multitask_schedule, str(elTask.trigger_type), **parameters, id=str(elTask.id),
                                   args=taskARG, max_instances=5)
        else:
            reglament_app.scheduler.add_job(schedule_api, str(elTask.trigger_type), **parameters, id=str(elTask.uuid), args=taskARG,
                                   max_instances=5)
        if elTask.execute == False:
            elTask.execute = True;
            elTask.save();

        resultReturn = {
            'result': True
            ,'discription': 'Task successfully started.'
        }

    return resultReturn;

def schedule_api(*args):
    from django.db.models.functions import Now
    from djTaskBrocker.models import task_log
    import importlib

    print("%%Start 'SHEDULE_APP' moment: " + str(datetime.utcnow().now()))
    print("ID: " + args[0]);
    print("App name: " + args[1]);
    print("Module name: " + args[2]);
    print("Function name: " + args[3]);
    print("Atribute: ", end="");
    print(args[3])

    # newTask = task_log(task_id=args[0], moment_start=Now())
    # newTask.save();

    operations = importlib.import_module(args[1] + '.' + args[2])

    result = getattr(operations, args[3])(args[4])

    # result = operations.test_operation(args[1]);

    '''
    if type(result) == 'dict':
        if "status" in result:
            if "status" in result:
                newTask.result_status = result["status"]
        if "message" in result:
            if "message" in result:       
                newTask.message = result["message"]


    newTask.moment_end = Now();
    newTask.save();
    '''

def multitask_schedule(*args):
    print("#1: Start task operation")  # Debug
    from django.db.models.functions import Now
    from djTaskBrocker.models import task_operation
    from djTaskBrocker.models import task_operation_log
    import importlib

    print("#2: Get operations")  # Debug
    # print("#1Start operation")#Debug
    firstOperation = task_operation.objects.all().filter(executing=False, finished=False).first();

    if firstOperation != None:

        start_moment = Now();

        firstOperation.executing = True;
        firstOperation.moment_start = start_moment;
        firstOperation.moment_end = None;
        firstOperation.result_status = None;
        firstOperation.result_status_internal = None
        firstOperation.message = None
        firstOperation.message_internal = None

        firstOperation.save();
        # print(firstOperation);

        newOperationLog = task_operation_log(task_operation_id=args[0], moment_start=Now())
        newOperationLog.moment_start = start_moment;
        newOperationLog.save();

        result_operation = {"status": 200, "message": ""}
        result = {"status": 0, "message": ""}

        try:
            print("#4: Start operation")  # Debug
            print("#4.1: Module library name: ", end="")
            print(args[1])

            operations = importlib.import_module(args[1] + '.' + args[2])
            # operations = importlib.import_module(args[1] + '.' + args[2])

            # resultOperation = getattr(operations, "test_multioperation")(3,4)
            result = getattr(operations, args[3])(args[4], firstOperation.parameters)

            if type(result) == 'dict':
                if not "status" in result:
                    result["status"] = 0;
                if "message" in result:
                    result["message"] = "";

                if result["status"] != 0:
                    result_operation["status"] = 207
                    result_operation["message"] = "Multistatus"

            else:
                result = {"status": 0, "message": ""}
                result_operation["status"] = 230
                result_operation["message"] = "No return status from operation"

        except Exception as e:
            result_operation["status"] = 500
            result_operation["message"] = "Executing exception: " + str(e)

        print("#5: wrire logs")  # Debug
        end_moment = Now()
        print('End moment: ' + str(end_moment))

        newOperationLog.parameters = firstOperation.parameters;
        newOperationLog.result_status = result_operation["status"]
        newOperationLog.result_status_internal = result["status"]
        newOperationLog.message = result_operation["message"]
        newOperationLog.message_internal = result["message"]

        newOperationLog.moment_end = end_moment;
        newOperationLog.save();

        firstOperation.executing = False;
        firstOperation.finished = True;

        firstOperation.result_status = result_operation["status"]
        firstOperation.result_status_internal = result["status"]
        firstOperation.message = result_operation["message"]
        firstOperation.message_internal = result["message"]

        firstOperation.moment_end = end_moment;
        firstOperation.save();

        print("#5: End operation")  # Debug

if __name__ == '__main__':
    #test2_operation("");
    test_multioperation(2,3)