import React, { useState } from 'react';
import './Login.css'
import axios from 'axios'; 
import { useNavigate } from 'react-router-dom';

function Login(props) {
  const [email,setEmail] = useState('');
  const [password,setPassword] = useState('');
  const [error,setError] = useState('');
  const navigate = useNavigate();
  function loginHandler(e){
    e.preventDefault();
    console.log('hello from login Handler');
    console.log(email,password);   
    console.log('calling backend services');
    // make a backend call with email , password and confirm_password
    axios.post('http://localhost:8000/signin', {"email": email,"password": password})
         .then((res)=> {
          console.log("-----------------");
          console.log(res);
          console.log("-----------------");
          if (res.data.status !== "ok"){
            setError(res.data.detail);
          }else{
            console.log(res.data);
            setError('');
            if (props.setIsLoggedIn) {
              props.setIsLoggedIn(true);
            }
            navigate('/todo');
          }
          
         })
         .catch((err) => {
          console.log(err);
          // Handle different error response formats
          let errMsg = 'Login failed';
          if (err.response && err.response.data) {
            errMsg = err.response.data.error || err.response.data.detail || errMsg;
          }
          console.log(errMsg);
          setError(errMsg);
        })

  }

  return (
    <div className='Login'>
      <form action="submit" className='SignUp'>
        <label htmlFor="signin_email">Email</label>
        <input type="text" id = "signin_email" name="signin_email" placeholder='enter email' onChange={(e) => setEmail(e.target.value)}/>
        <label htmlFor="signin_password">Password</label>
        <input type="password" id = "signin_password" name="signin_password" placeholder='enter password' onChange={(e) => setPassword(e.target.value)}/>
        <p id="signin_error">{error}</p>
        <button id = "signin_btn" type="submit" onClick={(e) => loginHandler(e)}>Log In</button>
      </form>  
      
    </div>
  )
}

export default Login