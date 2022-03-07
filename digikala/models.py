from django.db import models
from django.utils.translation import gettext as _


class Color(models.Model):
    
    name = models.CharField(max_length = 255 , verbose_name = _("name"), 
                            help_text = _("product name"),unique = True)  
    
    
    class Meta :

        verbose_name = "color"
        verbose_name_plural = "colors"    

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    
    name = models.CharField(max_length = 255 , verbose_name = _("name"), 
                            help_text = _("product name"),unique = True)  
    price = models.FloatField(verbose_name = _("price") , 
                                        help_text = _("product price"))
    color = models.ManyToManyField(Color , verbose_name = _("color") , help_text = _("product color"))
    
    exist = models.BooleanField(verbose_name = _("exist") , help_text = _("product existing check") ,default = True)
    
    rate = models.FloatField(verbose_name = _("rate") , 
                                        help_text = _("product rate") , null = True , blank = True)
    
    saler = models.CharField(max_length = 255,verbose_name = _("saler") , 
                                        help_text = _("product saler"), null = True , blank = True)
    
    discription = models.TextField(verbose_name = _("discription") , 
                                        help_text = _("product discription") , null = True , blank = True)
    
    gurantee = models.BooleanField(verbose_name = _("gurantee") , help_text = _("product gurantee check") ,default = True)
    
    
    class Meta : 
        
        verbose_name = "product"
        verbose_name_plural = "products"    


    def __str__(self) -> str:
        return self.name