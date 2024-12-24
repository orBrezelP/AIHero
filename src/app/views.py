from rest_framework import viewsets, serializers
from .models import Recipe, RecipeStep, RecipeIngredient
from app.tasks import generate_recipe
from rest_framework.response import Response
from rest_framework.views import APIView
from celery.result import AsyncResult

# Serializers
class RecipeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ['id', 'step_number', 'description']


class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ['id', 'name', 'quantity']


class RecipeSerializer(serializers.ModelSerializer):
    steps = RecipeStepSerializer(many=True)
    ingredients = RecipeIngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'created_at', 'steps', 'ingredients']

    def create(self, validated_data):
        steps_data = validated_data.pop('steps')
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)

        # Create Recipe Steps
        for step_data in steps_data:
            RecipeStep.objects.create(recipe=recipe, **step_data)

        # Create Recipe Ingredients
        for ingredient_data in ingredients_data:
            RecipeIngredient.objects.create(recipe=recipe, **ingredient_data)

        return recipe

    def update(self, instance, validated_data):
        steps_data = validated_data.pop('steps')
        ingredients_data = validated_data.pop('ingredients')

        # Update Recipe Steps
        instance.steps.all().delete()
        for step_data in steps_data:
            RecipeStep.objects.create(recipe=instance, **step_data)

        # Update Recipe Ingredients
        instance.ingredients.all().delete()
        for ingredient_data in ingredients_data:
            RecipeIngredient.objects.create(recipe=instance, **ingredient_data)

        return super().update(instance, validated_data)


# ViewSets
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class AddTaskView(APIView):
    def post(self, request):
        # Trigger the Celery task
        task = generate_recipe.delay(request.data.get("description"))
        return Response({"task_id": task.id, "status": task.status})


class TaskStatusView(APIView):
    def get(self, request, task_id):
        # Retrieve the task by its ID
        task_result = AsyncResult(task_id)
        return Response({
            "task_id": task_id,
            "status": task_result.status,
            "result": task_result.result if task_result.status == "SUCCESS" else None,
        })