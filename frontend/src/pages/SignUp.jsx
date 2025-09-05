import React, { useState } from 'react';
import './SignUp.css'
import axios from 'axios'; 
import { useNavigate } from 'react-router-dom';

function SignUp() {
  const [username,setUserName] = useState('');
  const [email,setEmail] = useState('');
  const [password,setPassword] = useState('');
  const [confirm_password,setConfirmPassword] = useState('');
  const [error,setError] = useState('');
  const navigate = useNavigate();
  function validate_email(){
      return true;
    }
  
  function validate_passwords(){
    if (password !== confirm_password){
      setError('passwords do not match');
      return false;
    }else{
      setError('');
      return true;
    }
  }

  function signupHandler(e){
    e.preventDefault();
    console.log('hello from signup Handler');
    console.log(username,email,password,confirm_password);
    

    if(!validate_email()){
      return;
    }

    if(!validate_passwords()){
      return;
    }
    
    console.log('calling backend services');
    // make a backend call with email , password and confirm_password
  axios.post('https://todo-7owg.onrender.com/signup'
              , {"username":username,"email": email,"password": password}
              , {withCredentials : true })
         .then((res)=> {
          console.log("-----------------");
          console.log(res);
          console.log("-----------------");
          if (res.data.status !== "ok"){
            setError(res.data.error || res.data.detail || 'Signup failed')
          }else{
            console.log(res.data);
            navigate('/login');
          }
          
         })
         .catch((err) => {
          // Handle different error response formats
          let errMsg = 'Signup failed';
          if (err.response && err.response.data) {
            errMsg = err.response.data.error || err.response.data.detail || errMsg;
          }
          console.log(errMsg)
          setError(errMsg)
        })

  }

  return (
    <div className="signup-container">
      <form className="signup-form" onSubmit={signupHandler}>
        <h2 className="signup-title">Sign Up</h2>
        <label htmlFor="signup_username">Username</label>
        <input type="text" id="signup_username" name="signup_username" placeholder="Enter your username" onChange={e => setUserName(e.target.value)} required />
        <label htmlFor="signup_email">Email</label>
        <input type="email" id="signup_email" name="signup_email" placeholder="Enter your email" onChange={e => setEmail(e.target.value)} required />
        <label htmlFor="signup_password">Password</label>
        <input type="password" id="signup_password" name="signup_password" placeholder="Enter your password" onChange={e => setPassword(e.target.value)} required />
        <label htmlFor="signup_confirm_password">Confirm Password</label>
        <input type="password" id="signup_confirm_password" name="signup_confirm_password" placeholder="Confirm your password" onChange={e => setConfirmPassword(e.target.value)} required />
        {error && <div className="error">{error}</div>}
        <button type="submit">Sign Up</button>
      </form>
    </div>
  )
}

export default SignUp