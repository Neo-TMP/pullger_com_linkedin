from django.contrib import admin
from djTaskBrocker.models import task
from djTaskBrocker.models import task_log
#from djTaskBrocker.models import task_operation
#from djTaskBrocker.models import task_operation_log


admin.site.register(task)
admin.site.register(task_log)
#admin.site.register(task_operation)
#admin.site.register(task_operation_log)
