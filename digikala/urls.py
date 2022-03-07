
from django.urls import path , include
from .digikala_api.api import ScrapingApiView

app_name = "digikala"
urlpatterns = [
    path("script/" , ScrapingApiView.as_view() , name = "script")
]
