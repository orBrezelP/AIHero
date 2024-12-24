import React, { useState } from 'react';

const RecipeOverview = ({ recipes = [] }) => {
  const [expandedRecipes, setExpandedRecipes] = useState({});

  const toggleRecipe = (id) => {
    setExpandedRecipes((prevState) => ({
      ...prevState,
      [id]: !prevState[id],
    }));
  };

  return (
    <div>
      <h2>Recipe Overview</h2>
      <ul>
        {recipes.map((recipe) => (
          <li key={recipe.id}>
            <h3 onClick={() => toggleRecipe(recipe.id)} style={{ cursor: 'pointer' }}>
              {recipe.title} {expandedRecipes[recipe.id] ? '[-]' : '[+]'}
            </h3>
            {expandedRecipes[recipe.id] && (
              <div>
                <h4>Ingredients</h4>
                <ul>
                  {recipe.ingredients.map((ingredient, index) => (
                    <li key={index}>{`${ingredient.quantity} ${ingredient.name}`}</li>
                  ))}
                </ul>
                <h4>Steps</h4>
                <ol>
                  {recipe.steps.map((step, index) => (
                    <li key={index}>{step.description}</li>
                  ))}
                </ol>
                <p>Created at: {new Date(recipe.created_at).toLocaleString()}</p>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RecipeOverview;
