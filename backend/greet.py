from fastapi import APIRouter

router = APIRouter(tags=["greets"])

@router.get('/')
def greet():
	return 'hello 2k26!'

@router.get('/greet/{name}')
def greet_by_name(name: str):
	return f'hello {name}'