from django.urls import path, include
from home_page.views import HomePage

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
]
