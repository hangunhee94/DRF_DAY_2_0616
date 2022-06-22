from rest_framework import serializers

from product.models import Product as ProductModel


class ProductSerializer(serializers.ModelSerializer):
    
    # 유저네임으로 불러오기
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )


    class Meta:
        model = ProductModel
        fields = [
            "user", "title", "thumbnail", "description", "created",
            "exposure_start_date", "exposure_end_date", 
        ]