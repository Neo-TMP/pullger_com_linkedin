#from attr import field
from rest_framework import serializers
from .models import task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = (
            'uuid'
            , 'id_name'
            , 'name'
            , 'type'
            , 'max_instances'
            , 'trigger_type'
            , 'trigger_interval_weeks'
            , 'trigger_interval_days'
            , 'trigger_interval_hours'
            , 'trigger_interval_minutes'
            , 'trigger_interval_seconds'
            , 'task_app_name'
            , 'task_module_name'
            , 'task_function_name'
            , 'execute'
        )

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = (
            'name'
            , 'id_name'
            , 'type'
            , 'trigger_type'
        )

class CreateSimpleTaskIntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = (
            'name'
            , 'id_name'
            , 'trigger_interval_weeks'
            , 'trigger_interval_days'
            , 'trigger_interval_hours'
            , 'trigger_interval_minutes'
            , 'trigger_interval_seconds'
            , 'task_app_name'
            , 'task_module_name'
            , 'task_function_name'
        )

class CreateSimpleTaskCronSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = (
            'name'
            , 'id_name'
            , 'type'
            , 'trigger_type'
        )

class CreateSimpleTaskDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = (
            'name'
            , 'id_name'
            , 'type'
            , 'trigger_type'
        )

class StopJobByNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = (
            'id_name',
        )

class StopJobByUUIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = (
            'uuid',
        )

class DeleteTaskByNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = (
            'id_name',
        )

class DeleteTaskByUUIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = (
            'uuid',
        )