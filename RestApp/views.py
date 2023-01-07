from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])
def main_GET(request):
    stu = Prof.objects.all()
    serializer = ProfSerializer(stu, many=True)

    return Response({'status': 200, 'payload': serializer.data,
                     'massage': ' get data from DB'})


@api_view(['POST'])
def main_POST(request):
    serializer = ProfSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status': 403, 'errors': serializer.errors,
                         'massage': 'something is wrong'})
    serializer.save()
    return Response({'status': 200, 'payload': serializer.data,
                     'massage': 'your data sent to backend'})


@api_view(['PUT'])
def main_Update(request, id):
    try:
        prof_obj = Prof.objects.get(id=id)
        serializer = ProfSerializer(prof_obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors,
                             'massage': 'something is wrong may be serializer not ok '})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data,
                         'massage': 'your data is updated in DB '})
    except Exception as e:
        return Response({'status': 403, 'massage': 'something is wrong may be ID not Found '})


@api_view(['DELETE'])
def main_Delete(request, id):
    try:
        prof_obj = Prof.objects.get(id=id)
        prof_obj.delete()
        return Response({'status': 200, 'massage': 'your data deleted from DB '})

    except Exception as e:
        return Response({'status': 403, 'massage': 'something Went wrong, may be invalid ID '})
