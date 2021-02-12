from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import StudentsSerializer, ModulesSerializer
from ..models import Students, Modules


class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer

    def get_queryset(self):
        students = Students.objects.all()
        return students

    def create(self, request, *args, **kwargs):
        data = request.data

        new_student = Students.objects.create(name=data["name"], age=data["age"], grade=data["grade"])
        # new_student = Students.objects.create(name=data["name"], age=data['age'], grade=data["grade"])
        new_student.save()

        for module in data["modules"]:
            module_obj = Modules.objects.get(module_name=module["module_name"],)
            new_student.modules.add(module_obj)

        serializer = StudentsSerializer(new_student)
        return Response(serializer.data)

class ModulesViewSet(viewsets.ModelViewSet):
    serializer_class = ModulesSerializer

    def get_queryset(self):
        module = Modules.objects.all()
        return module
