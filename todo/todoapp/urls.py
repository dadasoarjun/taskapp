from django.urls import path
from todoapp import views
urlpatterns = [
    path('',views.home_page),
    path('contact',views.contact_page),
    path('home',views.home_page),
    path('student',views.student_page),
    path('product',views.product_page),
    path('placement',views.placement_page),
    path('add_task',views.add_task),
    path('dtl',views.dtl),
]
