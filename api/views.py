from rest_framework import viewsets
from .models import Programmer
from .serializer import ProgrammerSerializer

# Create your views here.


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
