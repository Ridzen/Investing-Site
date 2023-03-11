from rest_framework import generics, filters, status, permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.business.models import Business, Category, BusinessDetail
from apps.business.serializers import BusinessSerializer, CategorySerializer, BusinessDetailSerializer

from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class BusinessListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class BusinessDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response(status=403)
        self.perform_destroy(instance)
        return Response(status=204)


class BusinessPremiumView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_premium = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def post(self, request):
        request_body = request.data
        srz = CategorySerializer(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST )


class BusinessDetailPostAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BusinessDetailSerializer
    queryset = BusinessDetail.objects.all()

    def post(self, request):
        request_body = request.data
        srz = BusinessDetailSerializer(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessDetailUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = BusinessDetailSerializer
    queryset = BusinessDetail.objects.all()


class BusinessDetailGetAPIView(generics.RetrieveAPIView):
    queryset = BusinessDetail.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            product = BusinessDetail.objects.get(id=pk)
        except BusinessDetail.DoesNotExist:
            return Response({'msg': 'post not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = BusinessDetailSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)


