from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from .models import Student


# class StudentListView(ListView):
#     model = Student
#     template_name = 'users/liststudent.html'

#     def get_queryset(self):
#         user_id = self.kwargs['pk']
#         return Student.objects.all()


# class StudentDetailView(DetailView):
#     model = Student
#     template_name = 'users/liststudent.html'
#     context_object_name = 'student'

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return Student.objects.filter(user_id=pk)
