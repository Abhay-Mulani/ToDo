import IonIcon from '@reacticons/ionicons';
import React from 'react';
import './TodoItem.css';
import { useState } from 'react';
// add(a,b) add(a=1,b-2)
function TodoItem(props) {
	console.log(props);
	
	let {title = "default title", desc:description, status, createdAt,idx,updateTodo,deleteTodo} = props;
	let [isEditable,setIsEditable] = useState(false);
	console.log(`isEditable: ${isEditable}`);
	function editTodo(){
		setIsEditable(true);
		console.log(`isEditable: ${isEditable}`);
	}
  return (
		<div className='TodoItem'>
			<div className="TodoItem__header">
				<h2>{title}</h2>
				<div className="TodoItem__header__actions">
					{
					isEditable ? <button id="close-todo-btn" onClick={() => editTodo()}> 
					<IonIcon id = "close-todo-img" name='close'></IonIcon>
				</button> :  <p>{status}</p> 
					}
					<button id="update-todo-btn" onClick={() => editTodo()}> 
						<IonIcon id = "update-todo-img" name='create'></IonIcon>
					</button>
					<button id="delete-todo-btn" onClick={() => deleteTodo(idx)}> 
						<IonIcon id = "delete-todo-img" name='trash'></IonIcon>
					</button>
				</div>
			</div>
			<p>{description}</p>
			{
				isEditable ? <input id = "input__status" name = "input__status" type="text" placeholder={status}></input> :  <p>{status}</p> 
			}
			<p>created at: {createdAt}</p>
		</div>
	)
}
export default TodoItem