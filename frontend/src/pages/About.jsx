import React from 'react';
import './About.css';

function About() {
  return (
    <div className="about-container">
      <div className="about-card">
        <div className="about-title">About This Todo App</div>
        <div className="about-desc">
          This is a modern, full-stack Todo application built with React (frontend), FastAPI (backend), and PostgreSQL (database). It allows users to securely manage their personal todos with a beautiful and responsive interface.
        </div>
        <ul className="about-list">
          <li>🔒 User authentication (Sign Up, Login, Logout)</li>
          <li>📝 Add, edit, and delete todos</li>
          <li>📅 Each todo shows its creation time</li>
          <li>👤 Todos are private and user-specific</li>
          <li>💾 Data is stored securely in PostgreSQL</li>
          <li>✨ Modern, responsive UI with smooth UX</li>
        </ul>
        <div className="about-footer">
          Made with ❤️ by Abhay Mulani <br/>
          <span style={{fontSize: '0.95rem'}}>2025 &copy; All rights reserved.</span>
        </div>
      </div>
    </div>
  );
}

export default About