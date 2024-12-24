import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RecipeGenerator = ({fetchRecipes=()=>null}) => {
  const [isLoading, setIsLoading] = useState(false);
  const [taskId, setTaskId] = useState(null);
  const [recipe, setRecipe] = useState(null);

  const generateRecipe = async () => {
    setIsLoading(true);
    try {
      const description = prompt('Enter a description for the recipe:');
      const response = await axios.post('http://localhost:8000/api/add-task/',
        {
          "description": description
        }
      );
      setTaskId(response.data.task_id);
    } catch (error) {
      console.error('Error triggering task:', error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (!taskId) return;

    const interval = setInterval(async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/task-status/${taskId}/`);
        if (response.data.status === 'SUCCESS') {
          fetchRecipes();
          clearInterval(interval);
        }
      } catch (error) {
        console.error('Error checking task status:', error);
        clearInterval(interval);
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [taskId]);

  return (
    <div>
      <button onClick={generateRecipe} disabled={isLoading}>
        {isLoading ? 'Generating...' : 'Generate Recipe'}
      </button>
      {recipe && (
        <div>
          <h2>{recipe.title}</h2>
          <h3>Ingredients</h3>
          <ul>
            {recipe.ingredients.map((ingredient, index) => (
              <li key={index}>{`${ingredient.quantity} ${ingredient.name}`}</li>
            ))}
          </ul>
          <h3>Steps</h3>
          <ol>
            {recipe.steps.map((step, index) => (
              <li key={index}>{step.description}</li>
            ))}
          </ol>
        </div>
      )}
    </div>
  );
};

export default RecipeGenerator;

