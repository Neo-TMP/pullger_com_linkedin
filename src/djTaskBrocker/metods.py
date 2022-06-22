from . import serealizers

def appendOperation(idNameTask, inParameters):
    from djTaskBrocker.models import task
    from djTaskBrocker.models import task_operation
    
    multyTask = task.objects.filter(id_name = idNameTask).first()
    
    if multyTask != None:
        newOperation = task_operation()
        newOperation.task_id = multyTask.id
        newOperation.parameters = inParameters;
        newOperation.save()

def CheckContein(inValue, inTypleList):
    for inData in inTypleList:
        if inValue in inData:
            return True;
    return False;


def CreateSimpleTaskInterval(inParameters):
    from djTaskBrocker.models import task

    resultReturn = {
        'result': False
        ,'discription': 'Unknown'
    }

    multyTask = task.objects.filter(id_name=inParameters['id_name']).first()

    if multyTask == None:
        newTask = task(
            id_name=inParameters["id_name"]
            , name=inParameters["name"]
            , type="single"
            , max_instances=1
            , trigger_type="interval"
            , trigger_interval_weeks=inParameters["trigger_interval_weeks"]
            , trigger_interval_days=inParameters["trigger_interval_days"]
            , trigger_interval_hours=inParameters["trigger_interval_hours"]
            , trigger_interval_minutes=inParameters["trigger_interval_minutes"]
            , trigger_interval_seconds=inParameters["trigger_interval_seconds"]
            , task_app_name=inParameters["task_app_name"]
            , task_module_name=inParameters["task_module_name"]
            , task_function_name=inParameters["task_function_name"]
            , execute=False
        )

        newTask.save();

        resultReturn['result'] = True;
        resultReturn['discription'] = '';
        resultReturn['data'] = serealizers.TaskSerializer(newTask).data
    else:
        resultReturn['result'] = False;
        resultReturn['discription'] = 'Data error id_name: [' + inParameters['id_name'] + '] is alrady exist';

    return resultReturn

def CreateSimpleTaskCron(inParameters):
    from djTaskBrocker.models import task

    resultReturn = {
        'result': False
        ,'discription': 'Unknown'
    }

    multyTask = task.objects.filter(id_name=inParameters['id_name']).first()

    if multyTask != None:
        resultReturn['result'] = False;
        resultReturn['discription'] = 'Data error id_name: [' + inParameters['id_name'] + '] is alrady exist';

    return resultReturn

def CreateSimpleTaskDate(inParameters):
    from djTaskBrocker.models import task

    resultReturn = {
        'result': False
        ,'discription': 'Unknown'
    }

    multyTask = task.objects.filter(id_name=inParameters['id_name']).first()

    if multyTask != None:
        resultReturn['result'] = False;
        resultReturn['discription'] = 'Data error id_name: [' + inParameters['id_name'] + '] is alrady exist';

    return resultReturn

def appendTask(inParameters):
    from djTaskBrocker.models import task

    resultReturn = {
        'result': False
        ,'discription': 'Unknown'
    }

    multyTask = task.objects.filter(id_name=inParameters['id_name']).first()

    if multyTask == None:
        resultReturn['result'] = True;
        resultReturn['discription'] = '';

        if CheckContein(inParameters['type'], task.TASK_TYPE_CHOICE):

            if CheckContein(inParameters['trigger_type'], task.TASK_TRIGGER_TYPE_CHOICE):
                newTask = task(id_name=inParameters["id_name"], name=inParameters["name"], type=inParameters["type"], max_instances=1, trigger_type=inParameters["trigger_type"], task_app_name="sdfsdf", task_module_name="dsfsdf", task_function_name="sdf3wew", execute=False)
                newTask.save();

                resultReturn['result'] = True;
                resultReturn['discription'] = '';
                resultReturn['data'] = serealizers.TaskSerializer(newTask).data
            else:
                resultReturn['result'] = False;
                resultReturn['discription'] = 'Data error unknown value on "trigger_type": [' + inParameters['trigger_type'] + ']';
        else:
            resultReturn['result'] = False;
            resultReturn['discription'] = 'Data error unknown value on "type": [' + inParameters['type'] + ']';
    else:
        resultReturn['result'] = False;
        resultReturn['discription'] = 'Data error id_name: [' + inParameters['id_name'] + '] is alrady exist';

    return resultReturn