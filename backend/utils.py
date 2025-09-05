#import hashlib
from passlib.context import CryptContext
import bcrypt,uuid
bcrypt.__about__ = bcrypt
pwd_context = CryptContext(schemes=["bcrypt"])

def encode(plain_text_password: str) -> str:
  #return hashlib.md5(plain_text_password.encode('utf-8'),usedforsecurity=True).hexdigest()
  return pwd_context.hash(plain_text_password)

def verify_passwords(plain_text_password: str,encoded_password: str) -> bool:
  print(f"Verifying password. Plain: '{plain_text_password}', Hash: '{encoded_password}'")
  try:
    res = pwd_context.verify(plain_text_password,encoded_password)
    print(f"Password match result: {res}")
    return res
  except Exception as e:
    print(f"Password verification error: {e}")
    return False

def generate_session_token() -> str:
  return str(uuid.uuid4())