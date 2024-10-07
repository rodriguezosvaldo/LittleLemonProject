
from django.urls import path
from . import views
from .views import MenuItemListView

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu-items/', MenuItemListView.as_view(), name='menu-items-list'),
]