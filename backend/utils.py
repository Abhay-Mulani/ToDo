#import hashlib
from passlib.context import CryptContext
import bcrypt,uuid
bcrypt.__about__ = bcrypt
pwd_context = CryptContext(schemes=["bcrypt"])

def encode(plain_text_password: str) -> str:
  #return hashlib.md5(plain_text_password.encode('utf-8'),usedforsecurity=True).hexdigest()
  return pwd_context.hash(plain_text_password)

def verify_passwords(plain_text_password: str,encoded_password: str) -> bool:
  print(plain_text_password,encoded_password)
  res = pwd_context.verify(plain_text_password,encoded_password)
  print(res)
  return res

def generate_session_token() -> str:
  return str(uuid.uuid4())