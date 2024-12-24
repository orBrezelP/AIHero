from django.db import models

class Recipe(models.Model):
    """
    Model to store recipe details.
    """
    title = models.CharField(max_length=200, help_text="Title of the recipe")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the recipe was created")

    def __str__(self):
        return f"Recipe created on {self.created_at}"

class RecipeStep(models.Model):
    """
    Model to store individual recipe steps.
    """
    step_number = models.PositiveIntegerField(help_text="Step number in the recipe")
    description = models.TextField(help_text="Description of the step")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")

    class Meta:
        ordering = ["step_number"]

    def __str__(self):
        return f"Step {self.step_number}: {self.description[:20]}..."

class RecipeIngredient(models.Model):
    """
    Model to store recipe ingredients.
    """
    name = models.CharField(max_length=100, help_text="Name of the ingredient")
    quantity = models.CharField(max_length=50, help_text="Quantity of the ingredient")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return f"{self.quantity} {self.name}"