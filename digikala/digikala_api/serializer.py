from dataclasses import fields
from rest_framework import serializers
from digikala.models import Product , Color

from digikala.utils import  get_detail_url

class ScriptingSerializer(serializers.ModelSerializer):
    
    url = serializers.URLField(write_only = True)
    color = serializers.StringRelatedField(many = True)
    
    class Meta :
        model = Product
        fields = ['name','price','exist','color','url' , 'rate' , 'saler' , 'discription' , 'gurantee']    
        read_only_fields = ('name','price','exist','color','rate' , 'saler' , 'discription' , 'gurantee')
    
    def create(self, validated_data):
        result = get_detail_url (validated_data.get("url"))

        for elm in result:
            colors = elm.pop("color")
            obj , _ = Product.objects.get_or_create(**elm)
            if colors :
                for item in colors : 
                    color , _ = Color.objects.get_or_create(name = item)
                
                    obj.color.add(color)
                    
                obj.save()
            
        return obj