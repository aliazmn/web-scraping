from rest_framework.generics import ListCreateAPIView
from digikala.models import Product
from .serializer import ScriptingSerializer

class ScrapingApiView(ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ScriptingSerializer