from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('/teste', IndexView.as_view())
]