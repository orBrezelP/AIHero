import axios from 'axios';

export const fetchRecipes = () => axios.get('http://localhost:8000/api/recipes/');
export const addTask = () => axios.get('http://localhost:8000/api/add-task/');
export const fetchTaskStatus = (taskId) => axios.get(`http://localhost:8000/api/task-status/${taskId}/`);

