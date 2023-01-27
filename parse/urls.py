from django.urls import path
from parse import views 

urlpatterns = [
    path('report/', views.upload_file, name="upload_file"),
    path('report/<str:name>/', views.get_report_shop, name='get_report_shop')
]