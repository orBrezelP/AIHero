from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, AddTaskView, TaskStatusView
from django.urls import path

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')

urlpatterns = [
    *router.urls,
    path('add-task/', AddTaskView.as_view(), name='add-task'),
    path('task-status/<str:task_id>/', TaskStatusView.as_view(), name='task-status'),

]
