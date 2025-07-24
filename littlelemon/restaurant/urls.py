from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'booking', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('', include(router.urls)),  # <-- Adds booking endpoints properly
]
