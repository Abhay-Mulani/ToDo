import React from 'react'
import './NavBar.css'
import {Link,useNavigate} from 'react-router-dom';
import axios from 'axios'; 

function NavBar(props) {
  const isLoggedIn = props.isLoggedIn;
  const navigate = useNavigate();
  function logoutHandler(e){
    e.preventDefault();
    console.log('hello from logout Handler');
    console.log('calling backend services');
    // make a backend call with email , password and confirm_password
    axios.post('http://localhost:8000/signout'
              , {withCredentials : true })
         .then((res)=> {
          console.log("-----------------");
          console.log(res);
          console.log("-----------------");
          if (res.data.status !== "ok"){
          }else{
            console.log(res.data);
            navigate('/login');
          }
          
         })
         .catch((err) => {
          const errMsg = err.response.data.detail
          console.log(errMsg)
        })

  }
  return (
    <div className="NavBar">
      {console.log('navbar rendered')}
      <Link to="/">Home</Link>
      <Link to="/about">About </Link>
      {isLoggedIn ? 
      <button onClick={logoutHandler}>Logout</button> : 
      <>
        <Link to='/login'>Login</Link>
        <Link to='/signup'>SignUp</Link>
      </>
      }
    </div>
  )
}

export default NavBar