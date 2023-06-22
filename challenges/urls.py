from django.urls import path  
from . import views

# urlpatterns = [
#     path("january/",views.index),
#     path("february/",views.february),
#     path("march/",views.march),

# ] 

# urlpatterns = [
#     path("<month>/", views.monthly_challenge),
# ]

urlpatterns = [
    path("" , views.index , name="all-challenge"),
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>/", views.monthly_challenge , name= "monthly-challenge"),
]