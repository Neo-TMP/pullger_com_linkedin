from django.db import models
#from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import signals
#from .models import task, task_log

class task(models.Model):
    TASK_TRIGGER_TYPE_CHOICE = [('interval','interval'),('cron','cron'),('date', 'date')]
    TASK_TYPE_CHOICE = [('single','single'),('multy','multy')]

    uuid = models.CharField(max_length=36, primary_key = True)

    name = models.CharField(max_length=150)
    id_name = models.CharField(max_length=50)
    #type = models.CharField(choices = TASK_TYPE_CHOICE, max_length=50, null=True, blank=True)
    type = models.CharField(choices=TASK_TYPE_CHOICE, max_length=50)
    max_instances = models.IntegerField(null=True, blank=True)
    trigger_type = models.CharField(choices = TASK_TRIGGER_TYPE_CHOICE , max_length=50)

    #trigger_type = models.CharField(max_length=50)
    #trigger_interval = models.CharField(max_length=50)
    #trigger_property = models.CharField(max_length=100)

    #interval parameters
    #source: https://apscheduler.readthedocs.io/en/3.x/modules/triggers/interval.html?highlight=triggers.interval
    trigger_interval_weeks = models.IntegerField(null=True, blank=True)
    trigger_interval_days = models.IntegerField(null=True, blank=True)
    trigger_interval_hours = models.IntegerField(null=True, blank=True)
    trigger_interval_minutes = models.IntegerField(null=True, blank=True)
    trigger_interval_seconds = models.FloatField(null=True, blank=True)
    trigger_interval_start_date = models.DateTimeField(null=True, blank=True)
    trigger_interval_end_date  = models.DateTimeField(null=True, blank=True)
    trigger_interval_timezone = models.CharField(max_length=10, null=True, blank=True)
    trigger_interval_jitter = models.IntegerField(null=True, blank=True)

    #date parameter
    #source: https://apscheduler.readthedocs.io/en/3.x/modules/triggers/date.html?highlight=trigger.date
    trigger_date_run_date = models.DateTimeField(null=True, blank=True)
    
    #cron parameter
    #source: https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html?highlight=triggers.cron
    trigger_cron_year = models.CharField(max_length=4, null=True, blank=True);
    trigger_cron_month = models.CharField(max_length=250, null=True, blank=True);
    trigger_cron_day = models.CharField(max_length=50, null=True, blank=True);
    trigger_cron_week = models.CharField(max_length=100, null=True, blank=True); 
    trigger_cron_day_of_week = models.CharField(max_length=100, null=True, blank=True);
    trigger_cron_hour = models.CharField(max_length=50, null=True, blank=True);
    trigger_cron_minute = models.CharField(max_length=50, null=True, blank=True);
    trigger_cron_second = models.CharField(max_length=50, null=True, blank=True);
    trigger_cron_start_date = models.DateTimeField(null=True, blank=True)
    trigger_cron_end_date = models.DateTimeField(null=True, blank=True)
    trigger_cron_timezone = models.CharField(max_length=10, null=True, blank=True) 
    trigger_cron_jitter = models.CharField(max_length=10, null=True, blank=True)
    
    task_app_name = models.CharField(max_length=100)
    task_module_name = models.CharField(max_length=100)
    task_function_name = models.CharField(max_length=100)
    
    execute = models.BooleanField(default = False)

@receiver(signals.pre_save, sender=task)
def add_task_uuid(sender, instance, **kwargs):
    import uuid

    if not instance.uuid:
        instance.uuid = str(uuid.uuid1())
#pre_save.connect(add_task_uuid, sender=task)

class task_log(models.Model):
    uuid = models.CharField(max_length=36, primary_key = True)

    task_id = models.BigIntegerField()
    moment_start = models.DateTimeField(null=True, blank=True) 
    moment_end = models.DateTimeField(null=True, blank=True)
    result_status = models.IntegerField(null=True, blank=True);
    result_status_internal = models.IntegerField(null=True, blank=True);
    message = models.CharField(max_length=250, null=True, blank=True);

@receiver(signals.pre_save, sender=task_log)
def add_task_log_uuid(sender, instance, **kwargs):
    import uuid

    if not instance.uuid:
        instance.uuid = str(uuid.uuid1())
#pre_save.connect(add_task_log_uuid, sender=task_log)

'''
class task_operation(models.Model):
    task_id = models.BigIntegerField()
    parameters = models.CharField(max_length=500, null=True, blank=True);
    
    shedule_start = models.DateTimeField(null=True, blank=True)

    moment_start = models.DateTimeField(null=True, blank=True) 
    moment_end = models.DateTimeField(null=True, blank=True)
     
    executing = models.BooleanField(null=True, blank=True, default=False)
    finished = models.BooleanField(null=True, blank=True, default=False)
    result_status = models.IntegerField(null=True, blank=True);
    result_status_internal = models.IntegerField(null=True, blank=True);
    message = models.CharField(max_length=250, null=True, blank=True);
    message_internal = models.CharField(max_length=250, null=True, blank=True);

class task_operation_log(models.Model):
    task_operation_id = models.BigIntegerField()  
    parameters = models.CharField(max_length=500, null=True, blank=True);
    moment_start = models.DateTimeField(null=True, blank=True) 
    moment_end = models.DateTimeField(null=True, blank=True)
    result_status = models.IntegerField(null=True, blank=True);
    result_status_internal = models.IntegerField(null=True, blank=True);
    message = models.CharField(max_length=250, null=True, blank=True);
    message_internal = models.CharField(max_length=250, null=True, blank=True);
'''

'''
class list(models.Model):
    uuid=models.CharField(max_length=36)
    active=models.BinaryField()
    version = models.IntegerField(default=0)
    char_field = models.CharField(max_length=32)    
    
    def __str__(self):
        return self.firstname
'''