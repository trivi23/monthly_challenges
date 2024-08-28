from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page,name="index"),
    path("<int:month>",views.monthly_challenge_bynumber_redirect),
    path("<int:month>",views.monthly_challenge_bynumber),
    path("<str:month>", views.monthly_challenge,name="monthly-challenges"),
    
]
