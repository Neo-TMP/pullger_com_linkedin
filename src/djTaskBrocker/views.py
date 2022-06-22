from django.shortcuts import render
from django.http import JsonResponse
#from h11 import Data
from .models import task
from . import serealizers
from . import operations

from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
import rest_framework


class CreateSimpleTaskCronView(APIView):
    serializer_class = serealizers.CreateSimpleTaskCronSerializer;
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            from .metods import CreateSimpleTaskCron

            appendResult = CreateSimpleTaskCron(serializer.data);
            if appendResult['result'] == True:
                return Response(appendResult['data'], status=rest_framework.status.HTTP_200_OK)
            else:
                return Response({'Error': appendResult['discription']}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'Bad Request': 'Broken data'}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

class StopJobViewByName(APIView):
    serializer_class = serealizers.StopJobByNameSerializer;
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            if serializer.data['id_name'] != "" and serializer.data['id_name'] != None:
                from djTaskBrocker.models import task
                taskByName = task.objects.filter(id_name=serializer.data['id_name']).first()

                if taskByName != None:
                    resultRequest = operations.stopJob(taskByName.uuid)

                    if resultRequest['result'] == True:
                        return Response(
                            {
                                'result': 'success'
                                ,'discription':'Task with \id_name\: [' + serializer.data['id_name'] + '] was stopped successful.'
                            }
                            , status=rest_framework.status.HTTP_200_OK)
                    else:
                        return Response(
                            {
                                'result' : 'error'
                                 ,'discription' : 'Task with \id_name\ : [' + serializer.data['id_name'] + '] was NOT stopped. ' + resultRequest['discription']}
                            ,status=rest_framework.status.HTTP_400_BAD_REQUEST)

                else:
                    return Response({'Bad Request': 'No task with "id_name": ' + request.data['id_name']}, status=rest_framework.status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'Bad Request': 'No data in request'}, status=rest_framework.status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Bad Request': 'Broken data'}, status=rest_framework.status.HTTP_400_BAD_REQUEST)


class StopJobViewByUUID(APIView):
    serializer_class = serealizers.StopJobByUUIDSerializer;
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        if 'uuid' in  serializer.data:
            resultRequest = operations.stopJob(serializer.data['uuid'])

            if resultRequest['result'] == True:
                return Response({'OK': 'Task with <uuid>: ' + serializer.data['uuid'] + ' stopped.'}, status=rest_framework.status.HTTP_200_OK)
            else:
                return Response(
                    {
                        'result': 'error'
                        ,
                        'discription': 'Task with \id_name\ : [' + serializer.data['uuid'] + '] was NOT started. ' +
                                       resultRequest['discription']}
                    , status=rest_framework.status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Bad Request': 'Broken data'}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

class StartJobViewByName(APIView):
    serializer_class = serealizers.StopJobByNameSerializer;
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            if serializer.data['id_name'] != "" and serializer.data['id_name'] != None:
                from djTaskBrocker.models import task
                taskByName = task.objects.filter(id_name=serializer.data['id_name']).first()

                if taskByName != None:
                    
                    resultRequest = operations.startJob(taskByName.uuid)
                    
                    if resultRequest['result'] == True:
                        return Response(
                            {
                                'result': 'success'
                                ,'discription':'Task with \id_name\: [' + serializer.data['id_name'] + '] was started successful.'
                            }
                            , status=rest_framework.status.HTTP_200_OK)
                    else:
                        return Response(
                            {
                                'result' : 'error'
                                 ,'discription' : 'Task with \id_name\ : [' + serializer.data['id_name'] + '] was NOT started. ' + resultRequest['discription']}
                            ,status=rest_framework.status.HTTP_400_BAD_REQUEST)

                else:
                    return Response(
                        {
                            'result': 'error'
                            ,'discription': 'No task with "id_name": ' + request.data['id_name']
                        }
                        , status=rest_framework.status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {
                        'result': 'error'
                        , 'discription': 'No data in request'
                    }
                    , status=rest_framework.status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {
                    'result': 'error'
                    ,'discription': 'Broken data'
                }
                , status=rest_framework.status.HTTP_400_BAD_REQUEST
            )

class StartJobViewByUUID(APIView):
    serializer_class = serealizers.StopJobByUUIDSerializer;
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        if 'uuid' in  serializer.data:
            resultRequest = operations.startJob(serializer.data['uuid'])

            if resultRequest['result'] == True:
                return Response(
                    {
                    'result': 'success'
                    ,'discription': 'Task with \id_name\ : [' + serializer.data['uuid'] + '] successfully started.'
                    }
                    , status=rest_framework.status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'result': 'error'
                        ,
                        'discription': 'Task with \id_name\ : [' + serializer.data['uuid'] + '] was NOT started. ' +
                                       resultRequest['discription']}
                    , status=rest_framework.status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    'result': 'error'
                    ,'discription': 'Broken data'
                }
                , status=rest_framework.status.HTTP_400_BAD_REQUEST
            )

class DeleteTaskViewByName(APIView):
    serializer_class = serealizers.DeleteTaskByNameSerializer;
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if serializer.data['id_name'] != "" and serializer.data['id_name'] != None:
                from djTaskBrocker.models import task
                taskByName = task.objects.filter(id_name=serializer.data['id_name']).first()

                if taskByName != None:

                    resultRequest = operations.deleteTask(taskByName.uuid)

                    if resultRequest['result'] == True:
                        return Response(
                            {
                                'result': 'success'
                                , 'discription': 'Task with \id_name\: [' + serializer.data[
                                'id_name'] + '] was started successful.'
                            }
                            , status=rest_framework.status.HTTP_200_OK)
                    else:
                        return Response(
                            {
                                'result': 'error'
                                , 'discription': 'Task with \id_name\ : [' + serializer.data[
                                'id_name'] + '] was NOT started. ' + resultRequest['discription']}
                            , status=rest_framework.status.HTTP_400_BAD_REQUEST)

                else:
                    return Response(
                        {
                            'result': 'error'
                            , 'discription': 'No task with "id_name": ' + request.data['id_name']
                        }
                        , status=rest_framework.status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {
                        'result': 'error'
                        , 'discription': 'No data in request'
                    }
                    , status=rest_framework.status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {
                    'result': 'error'
                    ,'discription': 'Broken data'
                }
                , status=rest_framework.status.HTTP_400_BAD_REQUEST
            )

class DeleteTaskViewByUUID(APIView):
    serializer_class = serealizers.DeleteTaskByUUIDSerializer;
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        if 'uuid' in serializer.data:
            resultRequest = operations.deleteTask(serializer.data['uuid'])

            if resultRequest['result'] == True:
                return Response(
                    {
                    'result': 'success'
                    ,'discription': 'Task with \id_name\ : [' + serializer.data['uuid'] + '] successfully deleted.'
                    }
                    , status=rest_framework.status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'result': 'error'
                        ,
                        'discription': 'Task with \id_name\ : [' + serializer.data['uuid'] + '] was NOT deleted. ' +
                                       resultRequest['discription']}
                    , status=rest_framework.status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    'result': 'error'
                    ,'discription': 'Broken data'
                }
                , status=rest_framework.status.HTTP_400_BAD_REQUEST
            )


class CreateSimpleTaskDateView(APIView):
    serializer_class = serealizers.CreateSimpleTaskDateSerializer;
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            from .metods import CreateSimpleTaskDate

            appendResult = CreateSimpleTaskDate(serializer.data);
            if appendResult['result'] == True:
                return Response(appendResult['data'], status=rest_framework.status.HTTP_200_OK)
            else:
                return Response({'Error': appendResult['discription']}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'Bad Request': 'Broken data'}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

class CreateSimpleTaskIntervalView(APIView):
    serializer_class = serealizers.CreateSimpleTaskIntervalSerializer;
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            from .metods import CreateSimpleTaskInterval

            appendResult = CreateSimpleTaskInterval(serializer.data);
            if appendResult['result'] == True:
                return Response(appendResult['data'], status=rest_framework.status.HTTP_200_OK)
            else:
                return Response({'Error': appendResult['discription']}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'Bad Request': 'Broken data'}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

class CreateTaskView(APIView):
    serializer_class = serealizers.CreateTaskSerializer;
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            from .metods import appendTask

            appendResult = appendTask(serializer.data);
            if appendResult['result'] == True:
                return Response(appendResult['data'], status=rest_framework.status.HTTP_200_OK)
            else:
                return Response({'Error': appendResult['discription']}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'Bad Request': 'Broken data'}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

class TaskView(generics.ListAPIView):
    queryset =  task.objects.all()
    serializer_class = serealizers.TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GetTask(APIView):
    serializer_class = serealizers.TaskSerializer
    lookup_url_kwarg = 'id_name'

    def get(self, request, format=None):
        id_name = request.GET.get(self.lookup_url_kwarg)
        if id_name != None:
            task_result = task.objects.filter(id_name=id_name)
            if len(task_result) > 0:
                data = serealizers.TaskSerializer(task_result[0]).data
                #data['is_host'] = self.request.session.session_key == room[0].host
                return Response(data, status=rest_framework.status.HTTP_200_OK)
            return Response({'Room Not Found': 'Invalid task name.'}, status=rest_framework.status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Code paramater not found in request'}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

def getRoutes(request):

    return JsonResponse('Our API', safe=False)

# Create your views here.
