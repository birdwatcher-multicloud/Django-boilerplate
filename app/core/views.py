from django.shortcuts import render
from .models import SampleTest
from .serializers import SampleTestSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class SampleTestViewSet(ModelViewSet):
    queryset = SampleTest.objects.all()
    serializer_class = SampleTestSerializer

    @action(methods=['post'], detail = False, url_path = 'multicreate')
    def multiple_create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data, many = True)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    def create(self, request, *args, **kwargs):
        try:
           data = SampleTest.objects.get( class_name = request.data["class_name"], field = request.data["field"])
           # you can return success like
           serialized_data = self.serializer_class(instance = data)
           return Response(serialized_data.data, status = status.HTTP_201_CREATED)
        except SampleTest.DoesNotExist:
            pass
        return super().create(request, *args, **kwargs)
    

def sample_html(request):
    template = "main/index.html"
    return render(request, template)