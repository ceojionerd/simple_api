from rest_framework.views import APIView

from rest_framework.response import Response

from .serializers import *
import uuid
from .models import UUID

def create_record(): 
    while True:
        uidd = uuid.uuid4().hex
        if not UUID.objects.filter(uuid=uidd).exists():
            record = UUID(uuid=uidd)
            record.save()
            break

class UUIDList(APIView):
    def get(self, request):
        create_record()
        model = UUID.objects.order_by('timestamp').reverse()
        serializer = UUIDSerializer(model, many=True)

        return Response(serializer.data)
