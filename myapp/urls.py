
from django.urls import path
from . import views

# localhost:8000/chia
urlpatterns = [
    path('', views.allchai, name='all_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),
]
