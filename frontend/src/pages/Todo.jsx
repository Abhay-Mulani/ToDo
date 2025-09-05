import React from 'react'
import IonIcon from '@reacticons/ionicons';
import axios from 'axios';
import { useEffect, useState } from 'react';
import './Todo.css';
import TodoItem from '../components/TodoItem';

function Todo() {
  // js goes here
	const [todosList, setTodosList] = useState([]);
	const [error, setError] = useState('');
	const [successMessage, setSuccessMessage] = useState('');
	const [userEmail, setUserEmail] = useState(localStorage.getItem('user_email'));

	useEffect(() => {
		const email = localStorage.getItem('user_email');
		setUserEmail(email);
		if (!email) {
			setTodosList([]);
			return;
		}
		axios.get('http://localhost:8000/api/v1/todos', { params: { user_email: email } })
			.then((res) => {
				console.log(res.data);
				setTodosList(res.data);
			})
			.catch((error) => {
				console.error('Error loading todos:', error);
				setTodosList([]);
			});
	}, [userEmail]);

	function deleteTodo(idx){
		const todoItem = todosList[idx];
		console.log(`deleting todo item with idx=${idx}`);
		console.log(`deleting todo item ${todoItem}`);
		const user_email = localStorage.getItem('user_email');
		axios.delete(`http://localhost:8000/api/v1/todos/delete-by-title/${todoItem.title}?user_email=${user_email}`)
		.then((res) => {
			console.log(res.data);
			console.log(todosList); // 3
			//todosList.splice(idx,1); // in place update of array via a delete
			const todoListLatest = todosList.filter((todo) => (todo.title !== todosList[idx].title));
			/*const todoListLatest = [...todosList];
			todoListLatest.splice(idx,1); */

			console.log(todoListLatest); // 2
			setTodosList(todoListLatest);
		})
		.catch((error) => {
			console.error('Error deleting todo:', error);
			setError('Failed to delete todo. Please try again.');
			setSuccessMessage('');
		});
		 
	}
	function updateTodo(idx, newStatus) {
		const todoItem = todosList[idx];
		const user_email = localStorage.getItem('user_email');
		const updatedTodo = {
			...todoItem,
			status: newStatus,
			user_email,
		};
		axios.put('http://localhost:8000/api/v1/todos', updatedTodo)
			.then((res) => {
				// Update the todo in the UI
				const updatedList = todosList.map((todo, i) =>
					i === idx ? { ...todo, status: newStatus } : todo
				);
				setTodosList(updatedList);
				setSuccessMessage('Todo updated successfully!');
				setTimeout(() => setSuccessMessage(''), 2000);
			})
			.catch((error) => {
				setError('Failed to update todo. Please try again.');
				setTimeout(() => setError(''), 2000);
			});
	}
	function addTodo(e){
		e.preventDefault();
		console.log(e);
		const user_email = localStorage.getItem('user_email');
		const todoItem = {'title':e.target[0].value
						   ,'desc':e.target[1].value
						   ,'status':e.target[2].value
						   ,'user_email':user_email}
		
		// Validate that title is not empty
		if (!todoItem.title.trim()) {
			setError('Please enter a title for the todo');
			setSuccessMessage('');
			return;
		}
		
		axios.post( 'http://localhost:8000/api/v1/todos'
			        , todoItem
						  , {withCredentials : true})
		.then((res) => {
			console.log('Todo added successfully:', res.data);
			setTodosList([...todosList,todoItem]);
			setSuccessMessage('Todo added successfully!');
			setError('');
			// Clear the form after successful addition
			e.target[0].value = '' //title
			e.target[1].value = '' // desc
			e.target[2].value = '' // status
			
			// Clear success message after 3 seconds
			setTimeout(() => setSuccessMessage(''), 3000);
		})
		.catch((error) => {
			console.error('Error adding todo:', error);
			let errorMessage = 'Failed to add todo';
			
			if (error.response) {
				if (error.response.status === 409) {
					errorMessage = 'A todo with this title already exists. Please use a different title.';
				} else if (error.response.data && error.response.data.error) {
					errorMessage = error.response.data.error;
				}
			}
			
			setError(errorMessage);
			setSuccessMessage('');
		});
	}


	return (
		<div className="Todo">
			<div className="todo-card">
				<form className="Add_Todo" onSubmit={addTodo}>
					<input id="add_todo_title_input" name="add_todo_title_input" placeholder="Enter title here" />
					<input id="add_todo_desc_input" name="add_todo_desc_input" placeholder="Enter description here" />
					<input id="add_todo_status_input" name="add_todo_status_input" placeholder="Enter status here" />
					<button id="add-todo-btn" type="submit">
						<IonIcon id="add-todo-img" name="add-circle"></IonIcon>
					</button>
				</form>
				{/* Error and Success Messages */}
				{error && <div className="todo-error">{error}</div>}
				{successMessage && <div className="todo-success">{successMessage}</div>}
				<h1 className="todo-title">Todos</h1>
				<div className="todo-list">
					{todosList.map((todo, idx) => (
						<TodoItem
							key={idx}
							idx={idx}
							deleteTodo={deleteTodo}
							updateTodo={updateTodo}
							title={todo.title}
							desc={todo.desc}
							status={todo.status}
							created_at={todo.created_at}
						/>
					))}
				</div>
			</div>
		</div>
  );
}

export default Todo