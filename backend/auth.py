from fastapi import APIRouter,HTTPException,status,Response,Request
import database,utils
from datetime import datetime,timedelta
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request, call_next):
    # For now, disable authentication middleware to get the app running
    # You can re-enable this later when you set up session management
    return await call_next(request)
    
router = APIRouter(tags=["auth"])

@router.post('/signup')
def sign_up(user_data: dict):
  print(user_data)
  conn = database.get_db()
  cursor = conn.cursor()
  try:
    username = user_data['username']
    email = user_data['email']
    password = user_data['password']
    encoded_password = utils.encode(password)
    query = f"select * from auth where email = '{email}'"
    print(query)
    cursor.execute(query)
    user_record_from_db = cursor.fetchone() 
    if user_record_from_db: # user record is found, report error
      conn.close()
      raise Exception(f"user with {email} already exists, please sign in")
    else: # user record is not found, proceed with sign up
      query = f"insert into auth(user,email,password) values ('{username}','{email}','{encoded_password}')"
      cursor.execute(query)
      conn.commit()
      conn.close()
      return {"status": "ok", "data": 'user signed up successfully'}
  except Exception as e:
    raise HTTPException(status.HTTP_400_BAD_REQUEST
                       ,str(e))
  finally:
    cursor.close()
    conn.close()  

@router.post('/signin')
def sign_in(response : Response,user_data: dict):
  print(user_data)
  conn = database.get_db()
  cursor = conn.cursor()
  try:
    email = user_data['email']
    password = user_data['password']
    query = f"select * from auth where email = '{email}'"
    print(query)
    cursor.execute(query)
    user_record_from_db = cursor.fetchone() 
    if not user_record_from_db: # user record is not found, report error
      conn.close()
      raise Exception(f"user with {email} doesnt exists, please signup first")
    else: # user record is found, proceed with sign in
      print(user_record_from_db)
      # For SQLite with row_factory, access by column name
      stored_password = user_record_from_db["password"]
      if not utils.verify_passwords(password, stored_password): # user entered wrong password
        conn.close()
        raise Exception(f"incorrect username or password. Please try again")
      else: # user record found and passwords match
        # For now, just return success without session management
        conn.close()
        return {"status": "ok", "data": 'user logged in successfully'}

  except Exception as e:
    raise HTTPException(status.HTTP_400_BAD_REQUEST
                       ,str(e))

@router.get('/signout')
def sign_out(request: Request, response : Response): 
  # Simplified signout without session management
  return {"status": "ok", "data": 'user signed out successfully'}  
