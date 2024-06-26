from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    # path('', views.newtask1, name='newtask1'),
    path('msr/', views.msr, name='msr'),
    path('get_polynomials_view/', views.get_polynomials_view, name='get_polynomials_view'),
    path('handle_matrix_operations_view/', views.handle_matrix_operations_view, name='handle_matrix_operations_view'),
    path('handle_matrix_operations_msr_view/', views.handle_matrix_operations_msr_view,
         name='handle_matrix_operations_msr_view')
]
