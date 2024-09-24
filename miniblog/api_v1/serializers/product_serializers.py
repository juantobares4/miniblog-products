from rest_framework import serializers
from product.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    description = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__' # Cambiar por cada uno de los campos.

    def get_description(self, value):
        if value.description is None:
            return 'No posee descripción'
        
        return value.description
    
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        category, created = Category.objects.get_or_create(
            **category_data

        )

        instance.category = category
        
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.active = validated_data.get('active', instance.active)
        instance.stock = validated_data.get('stock', instance.stock)

        instance.save()
        return instance
    
    """ def create(self, validated_data):
        category_data = validated_data.pop(
            'category', None

        ) # Extrae del diccionario la key 'category' y la almacena en la variable.

        category, created = Category.objects.get_or_create(
            **category_data

        ) # Recibe dos parámetros: Categoría y un booleano. Si es True es que fue creado. Si es False, es que lo obtuvo.

        product = Product.objects.create(
            name = validated_data['name'],
            price = validated_data['price'],
            stock = validated_data['stock'],
            active = True,
            category = category
        
        )

        return product # El ProductSerializer se va a encargar de parsearlo a JSON para mostrarlo en el FrontEnd. """