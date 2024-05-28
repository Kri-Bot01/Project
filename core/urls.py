from django.urls import path
from .views import home,aboutcompany

urlpatterns = [
    path('', home, name="homepage"),
    path('aboutus',aboutcompany,name="aboutpage")
]