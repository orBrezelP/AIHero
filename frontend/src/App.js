import React, { useEffect, useState } from 'react';
import RecipeGenerator from './components/RecipeGenerator';
import RecipeOverview from './components/RecipeOverview';
import axios from 'axios';

function App() {

  const [recipes, setRecipes] = useState([]);

  const fetchRecipes = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/recipes/');
      setRecipes(response.data);
    } catch (error) {
      console.error('Error fetching recipes:', error);
    }
  };


  useEffect(() => {
    fetchRecipes();
  }, []);


  return (
    <div>
      <h1>Recipe App</h1>
      <RecipeGenerator fetchRecipes={fetchRecipes}/>
      <hr />
      <RecipeOverview recipes={recipes}/>
    </div>
  );
}

export default App;

