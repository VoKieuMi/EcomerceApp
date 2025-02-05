from rest_framework import viewsets, generics,permissions,filters
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.models import AccessToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers, paginators
from .models import (
    User, StoreCategory, ProductCategory, Store, Product,
    Review, Order, OrderItem, Transaction, SaleStatistics, AdminStatistics
)
from .serializers import (
    UserSerializer, StoreCategorySerializer, ProductCategorySerializer,
    StoreSerializer, ProductSerializer, ReviewSerializer, OrderSerializer,
    OrderItemSerializer, TransactionSerializer, SaleStatisticsSerializer,
    AdminStatisticsSerializer
)



class UserViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #API: Đăng ký người dùng
    @action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user.role == 'seller':
                return Response({
                    "message": "Tài khoản của bạn đang chờ xác nhận từ nhân viên hệ thống.",
                    "user": UserSerializer(user).data
                }, status=201)
            return Response(UserSerializer(user).data, status=201)
        return Response(serializer.errors, status=400)

    # API: Xác nhận người bán (Chỉ dành cho nhân viên hệ thống)
    @action(methods=['post'], detail=True, permission_classes=[permissions.IsAuthenticated])
    def approve_seller(self, request, pk=None):
        if request.user.role not in ['staff', 'admin','user']:
            return Response({"error": "Bạn không có quyền xác nhận tài khoản"}, status=403)

        try:
            user = User.objects.get(pk=pk, role='seller', is_active=False)
            user.is_active = True
            user.save()
            return Response({"message": "Người bán đã được kích hoạt thành công."}, status=200)
        except User.DoesNotExist:
            return Response({"error": "Không tìm thấy tài khoản cần xác nhận."}, status=404)

    #API: Lấy hoặc cập nhật thông tin người dùng hiện tại
    @action(methods=['get', 'patch'], url_path='current-user', detail=False)
    def current_user(self, request):
        user = request.user
        if request.method == 'PATCH':
            for k, v in request.data.items():
                setattr(user, k, v)
            user.save()
        return Response(UserSerializer(user).data)

    #API: Đăng xuất (Thu hồi token)
    @action(methods=['post'], detail=False, permission_classes=[permissions.IsAuthenticated])
    def logout(self, request):
        try:
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return Response({"error": "Không tìm thấy token"}, status=400)

            token_key = auth_header.split(" ")[1]
            token = AccessToken.objects.get(token=token_key)

            if token.expires < now():
                return Response({"error": "Token đã hết hạn"}, status=400)

            token.delete()
            return Response({"message": "Đăng xuất thành công"}, status=204)
        except AccessToken.DoesNotExist:
            return Response({"error": "Token không hợp lệ"}, status=400)
# StoreCategory ViewSet
class StoreCategoryViewSet(viewsets.ViewSet):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer

# ProductCategory ViewSet
class ProductCategoryViewSet(viewsets.ViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

# Store ViewSet
class StoreViewSet(viewsets.ViewSet):
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def create_store(self, request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['get'])
    def list_stores(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

# Product ViewSet
class ProductViewSet(viewsets.ViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['store', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price']
    pagination_class = paginators.ProductPagination

    def get_paginated_response(self, data):
        paginator = PageNumberPagination()
        return paginator.get_paginated_response(data)
    def paginate_queryset(self, queryset):
        paginator = PageNumberPagination() # Hoặc sử dụng pagination tùy chỉnh của bạn
        return paginator.paginate_queryset(queryset, self.request)
    @action(detail=False, methods=['post'])
    def create_product(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['get'])
    def list_products(self, request):
        products = Product.objects.all()
        # Gọi paginate_queryset với request được truyền vào
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# Review ViewSet
class ReviewViewSet(viewsets.ViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Order ViewSet
class OrderViewSet(viewsets.ViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# OrderItem ViewSet
class OrderItemViewSet(viewsets.ViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# Transaction ViewSet
class TransactionViewSet(viewsets.ViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# SaleStatistics ViewSet
class SaleStatisticsViewSet(viewsets.ViewSet):
    queryset = SaleStatistics.objects.all()
    serializer_class = SaleStatisticsSerializer

# AdminStatistics ViewSet
class AdminStatisticsViewSet(viewsets.ViewSet):
    queryset = AdminStatistics.objects.all()
    serializer_class = AdminStatisticsSerializer
