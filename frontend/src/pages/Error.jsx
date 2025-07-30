import React from 'react';
import './Error.css';
import {Link} from 'react-router-dom';

function Error() {
  return (
    <div className='Error'>
      <h1>This page could not be found!</h1>
      <p>We are sorry. But the page you are looking for is not available. </p>
      <Link to="/" >Click here to navigate to Home </Link>
    </div>
  )
}

export default Error