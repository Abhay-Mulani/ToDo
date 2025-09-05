import IonIcon from '@reacticons/ionicons';
import React from 'react';
import './TodoItem.css';
import { useState } from 'react';
// add(a,b) add(a=1,b-2)
function TodoItem(props) {
	let {title = "default title", desc: description, status, created_at, idx, updateTodo, deleteTodo} = props;
	const [isEditable, setIsEditable] = useState(false);
	const [editStatus, setEditStatus] = useState(status);

	// Format created_at for display
	let createdAtStr = created_at ? new Date(created_at).toLocaleString() : "";

	function handleEditClick() {
		setIsEditable(true);
	}
	function handleCancelEdit() {
		setIsEditable(false);
		setEditStatus(status);
	}
	function handleSaveEdit() {
		// Call updateTodo with new status
		updateTodo(idx, editStatus);
		setIsEditable(false);
	}

	return (
		<div className='TodoItem'>
			<div className="TodoItem__header">
				<h2>{title}</h2>
				<div className="TodoItem__header__actions">
					{isEditable ? (
						<>
							<button id="close-todo-btn" onClick={handleCancelEdit}>
								<IonIcon id="close-todo-img" name='close'></IonIcon>
							</button>
							<button id="update-todo-btn" onClick={handleSaveEdit}>
								<IonIcon id="update-todo-img" name='checkmark'></IonIcon>
							</button>
						</>
					) : (
						<>
							<p>{status}</p>
							<button id="update-todo-btn" onClick={handleEditClick}>
								<IonIcon id="update-todo-img" name='create'></IonIcon>
							</button>
						</>
					)}
					<button id="delete-todo-btn" onClick={() => deleteTodo(idx)}>
						<IonIcon id="delete-todo-img" name='trash'></IonIcon>
					</button>
				</div>
			</div>
			<p>{description}</p>
			{isEditable ? (
				<input
					id="input__status"
					name="input__status"
					type="text"
					value={editStatus}
					onChange={e => setEditStatus(e.target.value)}
					placeholder="Status"
				/>
			) : (
				<p>{status}</p>
			)}
			<p style={{fontSize: '0.95rem', color: '#888'}}>created at: {createdAtStr}</p>
		</div>
	);
}
export default TodoItem