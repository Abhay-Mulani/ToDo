import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Landing.css';

function Landing() {
  const navigate = useNavigate();
  return (
    <div className="landing-container">
      <h1 className="landing-title">Welcome to Todo App</h1>
      <p className="landing-desc">Organize your tasks efficiently and stay productive!</p>
      <div className="landing-actions">
        <button className="landing-btn" onClick={() => navigate('/login')}>Sign In</button>
        <button className="landing-btn" onClick={() => navigate('/signup')}>Sign Up</button>
      </div>
    </div>
  );
}

export default Landing;
