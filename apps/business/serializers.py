from rest_framework import serializers

from apps.business.models import Business, Category, BusinessDetail


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = (
            'id', 'title', 'owner', 'budget', 'term', 'description',
            'is_active', 'is_premium', 'location', 'image', 'category', 'created_at'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'title',
        )


class BusinessDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDetail
        fields = (
            'id', 'business', 'file', 'contact'
        )
