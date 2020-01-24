from django.shortcuts import render

def exersices_list(request):
    return render(request, 'exercises/exercises_index.html')

