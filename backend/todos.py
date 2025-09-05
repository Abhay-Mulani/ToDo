from typing import List, Optional
from fastapi import APIRouter,HTTPException,status,Query
import database,auth

router = APIRouter(tags=["todos"])


# read all Todos for a user
@router.get('/api/v1/todos',status_code=status.HTTP_200_OK)
def get_all_todos(user_email: str, limit: Optional[int] = Query(10), offset:Optional[int] = Query(0)) -> List[dict]: 
	start_idx = int(offset)
	end_idx = start_idx + int(limit)
	query = "select title,descr,status,created_at from todo where user_email=%s"
	conn = database.get_db()
	cursor = conn.cursor()
	cursor.execute(query, (user_email,))
	todos_from_db = cursor.fetchall() # list of tuples
	todos = [] # list of dict
	for row in todos_from_db:
		todos.append({"title" : row[0]
				 , "desc" : row[1]
				 , "status" : row[2]
				 , "created_at": row[3]})
	conn.close()
	return todos[start_idx: end_idx]

# read Todo by title
@router.get('/api/v1/todos/title/{title}'
				 ,status_code=status.HTTP_200_OK)
def get_todo_by_title(title: str) -> dict: 
	query = f"select title,descr,status,created_at from todo where title='{title}'"
	conn = database.get_db()
	cursor = conn.cursor()
	cursor.execute(query)
	todos_from_db = cursor.fetchall() # list of tuples
	todos = [] # list of dict
	for row in todos_from_db:
		todos.append({"title" : row[0]
				 , "desc" : row[1]
				 , "status" : row[2]
				 , "created_at": row[3]})
	conn.close()
	if len(todos) == 1:
		return todos[0]
	else:
		raise HTTPException(status.HTTP_404_NOT_FOUND
											,f"todo not found with the title {title}")

# read Todo by status
@router.get('/api/v1/todos/status/{status}'
				,status_code=status.HTTP_200_OK)
def get_todos_by_status(status: str) -> List[dict]: 
	query = f"select title,descr,status,created_at from todo where status='{status}'"
	conn = database.get_db()
	cursor = conn.cursor()
	cursor.execute(query)
	todos_from_db = cursor.fetchall() # list of tuples
	todos = [] # list of dict
	for row in todos_from_db:
		todos.append({"title" : row[0]
				 , "desc" : row[1]
				 , "status" : row[2]
				 , "created_at": row[3]})
	conn.close()
	return todos


# create a todo for a user
@router.post('/api/v1/todos',status_code=status.HTTP_201_CREATED)
def create_todo(todo: dict) -> bool:
	# todo dict must include user_email
	query = "select title,descr,status from todo where title=%s and user_email=%s"
	conn = database.get_db()
	cursor = conn.cursor()
	cursor.execute(query, (todo['title'], todo['user_email']))
	todos_from_db = cursor.fetchall() # list of tuples
	conn.close()
    
	if (len(todos_from_db) > 0):
		message = f"todo with title {todo['title']} already exists for this user."
		raise HTTPException(status.HTTP_409_CONFLICT,message)
    
	query = "insert into todo(title,descr,status,user_email) values(%s, %s, %s, %s)"
	conn = database.get_db()
	cursor = conn.cursor()
	cursor.execute(query, (todo['title'], todo['desc'], todo['status'], todo['user_email']))
	conn.commit()
	conn.close()
	return True


@router.put('/api/v1/todos'
				,status_code=status.HTTP_200_OK)
def update_todo(payload: dict) -> bool:
	query = "update todo set descr = %s, status = %s where title=%s and user_email=%s"
	conn = database.get_db()
	cursor = conn.cursor()
	cursor.execute(query, (payload['desc'], payload['status'], payload['title'], payload['user_email']))
	conn.commit()
	conn.close()
	return True

from fastapi import Query

@router.delete('/api/v1/todos/delete-by-title/{title}')
def delete_todo(title: str, user_email: str = Query(...)) -> bool:
	query = "delete from todo where title=%s and user_email=%s"
	conn = database.get_db()
	cursor = conn.cursor()
	cursor.execute(query, (title, user_email))
	conn.commit()
	conn.close()
	return True