from django.urls import path
from diabetes_prediction_app import views
urlpatterns = [
   path('',views.home_view,name='home'),
   path('predict/',views.predict_diabetes,name='predict')
]
