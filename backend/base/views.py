from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Record
from rest_framework import status
from base.serializers import RecordSerializer


# api for user to see his/her profile only if he is logged in

# api for admin to see the list of all the users present.
@api_view(['GET'])
def getRecords(request):
    records = Record.objects.all()
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)

# api for user to add a new student in the database


@api_view(['POST'])
def createRecord(request):
    data = request.data
    try:
        record = Record.objects.create(
            name=data['name'],
            description=data['description'],
            email=data['email'],
        )
        serializer = RecordSerializer(record, many=False)
        return Response("Record added successfully")
    except:
        message = {'detail': "Some error occured in creating the record"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
