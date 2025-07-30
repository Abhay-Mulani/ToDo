// css is imported here
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import Todo from './pages/Todo';
import NavBar from './components/NavBar';
import About from './pages/About';
import Login from './pages/Login';
import SignUp from './pages/SignUp';
import Error from './pages/Error';
import './App.css';
import React, { useState } from 'react';

function App() {
	const [isLoggedIn,setIsLoggedIn] = useState(false);

	return (
		<div className="App">
			<BrowserRouter>
				<NavBar isLoggedIn = {isLoggedIn}/>
				<Routes>
					<Route path='/' element = { isLoggedIn ? <Todo/> : <Login setIsLoggedIn = {setIsLoggedIn}/>} ></Route>
					<Route path='/about' element = {<About/>} ></Route>
					<Route path='/login' element = {<Login setIsLoggedIn = {setIsLoggedIn}/>} ></Route>
					<Route path='/signup' element = {<SignUp/>} ></Route>
					<Route path='/todo' element = {<Todo/>} ></Route>
					<Route path='*' element = {<Error/>} ></Route>
				</Routes>
			</BrowserRouter>
		</div>
	)	
}

export default App;