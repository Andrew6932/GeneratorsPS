from django.shortcuts import render
from .models import Polynomial
from django.http import JsonResponse
from .FisrtTaskCalculator.SrwfCalculator import SrwfCalculator
from .SecondTaskCalculator.MsrCalculator import MsrCalculator

def base(request):
    return render(request, 'base.html')

def msr(request):
    return render(request, 'msr.html')
# def newtask1(request):
#     return render(request, 'newtask1.html')

def get_polynomials_view(request):
    return SrwfCalculator.get_polynomials(request)

def handle_matrix_operations_view(request):
    polynomial_id = request.GET.get('polynomial_id')
    polynomial = Polynomial.objects.get(pk=polynomial_id)
    selected_number = int(request.GET.get('select'))
    cal = SrwfCalculator()
    result = cal.calculate_srwf(polynomial, selected_number)
    return JsonResponse({'result': result})

def handle_matrix_operations_msr_view(request):
    polynomial_idFirst = request.GET.get('polynomial_idFirst')
    polynomialFirst = Polynomial.objects.get(pk=polynomial_idFirst)
    polynomial_idSecond = request.GET.get('polynomial_idSecond')
    polynomialSecond = Polynomial.objects.get(pk=polynomial_idSecond)
    cal = MsrCalculator()
    listResult = cal.calculate_msr(polynomialFirst, polynomialSecond)
    return JsonResponse({'listResult': listResult})