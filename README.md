# Todo Application

A full-stack todo application built with React frontend and Python backend using SQLite database.

## 🚀 Features

- **User Authentication**: Sign up and log in functionality
- **Todo Management**: Create, read, update, and delete todos
- **Real-time Updates**: Dynamic UI updates without page refresh
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Responsive Design**: Clean and intuitive user interface

## 🏗️ Project Structure

```
todo/
├── backend/                 # Python backend
│   ├── auth.py             # Authentication routes and middleware
│   ├── database.py         # SQLite database connection and setup
│   ├── greet.py            # Greeting routes
│   ├── main.py             # FastAPI main application (unused)
│   ├── simple_server.py    # HTTP server implementation (active)
│   ├── todos.py            # Todo CRUD operations
│   ├── utils.py            # Utility functions (password hashing, etc.)
│   ├── requirements.txt    # Python dependencies
│   └── todos.db           # SQLite database file (auto-generated)
├── frontend/               # React frontend
│   ├── public/            # Static files
│   ├── src/
│   │   ├── components/    # React components
│   │   │   ├── NavBar.jsx
│   │   │   └── TodoItem.jsx
│   │   ├── pages/         # Page components
│   │   │   ├── About.jsx
│   │   │   ├── Error.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── SignUp.jsx
│   │   │   └── Todo.jsx
│   │   ├── App.jsx        # Main App component
│   │   └── index.js       # Entry point
│   ├── package.json       # Node.js dependencies
│   └── package-lock.json
├── .vscode/
│   └── tasks.json         # VS Code tasks for easy development
├── start_servers.bat      # Batch script to start both servers
└── README.md             # This file
```

## 🛠️ Technologies Used

### Backend
- **Python 3.12**
- **SQLite** - Lightweight database
- **bcrypt** - Password hashing
- **HTTP Server** - Custom implementation for API endpoints

### Frontend
- **React 18** - UI framework
- **React Router DOM** - Client-side routing
- **Axios** - HTTP client for API calls
- **CSS** - Custom styling

## 📋 Prerequisites

Before running this application, make sure you have:

- **Python 3.12+** installed
- **Node.js** and **npm** installed
- **Git** (optional, for cloning)

## 🚀 Quick Start

### Option 1: Using the Batch Script (Recommended)
```cmd
# Navigate to the project directory
cd c:\CODING\Projects\todo

# Run the batch script to start both servers
start_servers.bat
```

### Option 2: Manual Setup

#### 1. Start the Backend Server
```bash
# Navigate to backend directory
cd c:\CODING\Projects\todo\backend

# Install Python dependencies (if not already installed)
pip install -r requirements.txt

# Start the backend server
python simple_server.py
```
The backend will be available at: `http://127.0.0.1:8000`

#### 2. Start the Frontend Server
```bash
# Open a new terminal and navigate to frontend directory
cd c:\CODING\Projects\todo\frontend

# Install Node.js dependencies (if not already installed)
npm install

# Start the React development server
npm start
```
The frontend will be available at: `http://localhost:3000`

### Option 3: Using VS Code Tasks
1. Open the project in VS Code
2. Press `Ctrl+Shift+P` to open the command palette
3. Type "Tasks: Run Task"
4. Select "Start Both Servers" to run both backend and frontend simultaneously

## 🔧 API Endpoints

### Authentication
- `POST /signup` - Create a new user account
- `POST /signin` - User login

### Todos
- `GET /api/v1/todos` - Get all todos
- `GET /api/v1/todos/title/{title}` - Get todo by title
- `GET /api/v1/todos/status/{status}` - Get todos by status
- `POST /api/v1/todos` - Create a new todo
- `PUT /api/v1/todos` - Update an existing todo
- `DELETE /api/v1/todos/delete-by-title/{title}` - Delete a todo

### General
- `GET /` - API status check

## 💾 Database Schema

### Users Table (`auth`)
```sql
CREATE TABLE auth (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user VARCHAR(60),
    email VARCHAR(30) UNIQUE,
    password VARCHAR(60)
);
```

### Todos Table (`todo`)
```sql
CREATE TABLE todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(30),
    descr VARCHAR(60),
    status VARCHAR(30)
);
```

## 🎯 How to Use

1. **Sign Up**: Create a new account with username, email, and password
2. **Log In**: Access your account using email and password
3. **Add Todos**: Fill out the form with title, description, and status
4. **View Todos**: See all your todos listed on the main page
5. **Update Todos**: Edit existing todos (feature available)
6. **Delete Todos**: Remove todos you no longer need

## 🐛 Troubleshooting

### Backend Issues
- **Import errors**: Make sure you're running the server from the `backend` directory
- **Database errors**: The SQLite database is automatically created on first run
- **Port conflicts**: The backend uses port 8000 by default

### Frontend Issues
- **npm start fails**: Make sure you're in the `frontend` directory and run `npm install` first
- **API connection errors**: Ensure the backend server is running on port 8000
- **CORS errors**: The backend is configured to allow requests from `localhost:3000`

### Common Solutions
1. **Restart both servers** if you encounter issues
2. **Check that both servers are running** on their respective ports
3. **Clear browser cache** if you see old error messages
4. **Check console logs** in browser developer tools for detailed error information

## 🔄 Development Workflow

1. Make changes to backend code (Python files)
2. The simple server will need to be restarted manually
3. Make changes to frontend code (React/JavaScript files)
4. The React development server will auto-reload
5. Test your changes in the browser

## 📝 Sample Data

The application comes with sample todos:
- "class_start" - "class starts at 5:30PM" (status: open)
- "class_end" - "class ends at 7:30PM" (status: open)

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Credits

Built as a learning project demonstrating full-stack web development with React and Python.

---

**Happy Coding!** 🚀
