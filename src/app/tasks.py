import json

from app.models import Recipe, RecipeIngredient, RecipeStep
from celery import shared_task
from openai import OpenAI

tools = [
    {
      "type": "function",
      "function": {
          "name": "create_recipe_title",
          "description": "Create a title for the recipe.",
          "parameters": {
              "type": "object",
              "properties": {
                  "title": {
                      "type": "string",
                      "description": "Title of the recipe.",
                  },
              },
              "required": ["order_id"],
              "additionalProperties": False,
          },
      }
  },
    {
        "type": "function",
        "function": {
            "name": "create_recipe_step",
            "description": "Create a step for the recipe.",
            "parameters": {
                "type": "object",
                "properties": {
                    "step_number": {
                        "type": "integer",
                        "description": "Step number in the recipe.",
                    },
                    "description": {
                        "type": "string",
                        "description": "Description of the step.",
                    },
                },
                "required": ["step_number", "description"],
                "additionalProperties": False,
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_recipe_ingredient",
            "description": "Create an ingredient for the recipe.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name of the ingredient.",
                    },
                    "quantity": {
                        "type": "string",
                        "description": "Quantity of the ingredient.",
                    },
                },
                "required": ["name", "quantity"],
                "additionalProperties": False,
            },
        }
    },

]


@shared_task
def generate_recipe(description):
    # Simulate recipe generation
    description = f"return a list of tool calls, at least 10 tool calls for the recipe: {description}"
    client = OpenAI()
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": description}
        ],
        tools=tools
    )
    for item in response.choices[0].message.tool_calls:
        # Parse the arguments as JSON
        arguments = json.loads(item.function.arguments)

        if item.function.name == 'create_recipe_title':
            # Create the recipe
            recipe = Recipe.objects.create(title=arguments['title'])

        elif item.function.name == 'create_recipe_ingredient':
            if recipe:
                # Create a recipe ingredient
                RecipeIngredient.objects.create(
                    name=arguments['name'],
                    quantity=arguments['quantity'],
                    recipe=recipe
                )

        elif item.function.name == 'create_recipe_step':
            if recipe:
                # Create a recipe step
                RecipeStep.objects.create(
                    step_number=arguments['step_number'],
                    description=arguments['description'],
                    recipe=recipe
                )

    return response.choices[0].message.content
