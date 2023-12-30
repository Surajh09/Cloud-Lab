from array import array
from atexit import register
from multiprocessing import context
from multiprocessing.dummy import Array
from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .form import *


def index_view(request,*args,**kwargs):
    
    return render(request,"index.html", {})


def error_view(request,exception):

    return render(request,"error.html",{})


def bubble_view(request,*args,**kwargs):
    
    return render(request,"bubble.html", {})

def login_view(request,*args,**kwargs):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
            
    #         # Save the data to the database here
    #         form.save()
    #         return render(request, '/', {forms:form})
    # else:
    #     form = SignUpForm()
    
    return render(request,"login.html", {})

def merge_view(request,*args,**kwargs):
    
    return render(request,"merge.html", {})

def insertion_view(request,*args,**kwargs):
    
    return render(request,"insertion.html", {})

def array_view(request,*args,**kwargs):
    
    return render(request,"array.html", {})


def list_view(request,*args,**kwargs):
    
    return render(request,"list.html", {})


def linkedlist_view(request,*args,**kwargs):
    
    return render(request,"linklist.html", {})

def assesment_view(request,*args,**kwargs):
    return render(request,"#", {})

def aboutUs_view(request,*args,**kwargs):
    
    return render(request,"about_us.html", {})

def stack_view(request,*args,**kwargs):
    
    return render(request,"stack.html", {})


# TRAIL TRAIL


def algorithm_list(request):
    algorithms = Algorithm.objects.filter(user=request.user)
    return render(request, '', {'algorithms': algorithms})


def algorithm_create(request):
    if request.method == 'POST':
        algorithm = Algorithm(user=request.user,
                              name=request.POST['name'],
                              code=request.POST['code'])
        algorithm.save()
        return redirect('algorithm_list')
    return render(request, '')


def algorithm_delete(request, pk):
    algorithm = Algorithm.objects.get(pk=pk)
    if request.user != algorithm.user:
        return redirect('algorithm_list')
    algorithm.delete()
    return redirect('algorithm_list')


# ALGORITHMS

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    for k in range(n):
        print(arr)
        return arr

def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1