from django.urls import path
from . import views

urlpatterns = [
    path('forms/wheel-specifications', views.WheelSpecificationListCreate.as_view()),
    path('forms/bogie-checksheet', views.BogieCheckSheetCreate.as_view()),
]
