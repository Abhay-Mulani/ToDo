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
  axios.post('https://todo-7owg.onrender.com/signin', {"email": email,"password": password})
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
            // Store user email in localStorage
            localStorage.setItem('user_email', email);
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
    <div className="login-container">
      <form className="login-form" onSubmit={loginHandler}>
        <h2 className="login-title">Sign In</h2>
        <label htmlFor="signin_email">Email</label>
        <input type="text" id="signin_email" name="signin_email" placeholder="Enter your email" onChange={e => setEmail(e.target.value)} autoComplete="username" required />
        <label htmlFor="signin_password">Password</label>
        <input type="password" id="signin_password" name="signin_password" placeholder="Enter your password" onChange={e => setPassword(e.target.value)} autoComplete="current-password" required />
        {error && <div className="error">{error}</div>}
        <button type="submit">Log In</button>
      </form>
    </div>
  )
}

export default Login