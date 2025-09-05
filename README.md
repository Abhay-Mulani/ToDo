
# Todo Application

A modern full-stack Todo application built with React (frontend), FastAPI (backend), and PostgreSQL (database).

## 🚀 Features

- **User Authentication**: Sign up, log in, and log out securely
- **Todo Management**: Create, read, update, and delete your todos
- **User-specific Data**: Todos are private and tied to your account
- **Timestamps**: Each todo shows its creation time
- **Modern UI**: Beautiful, responsive, and intuitive interface
- **Error Handling**: Friendly error messages and robust backend validation

## 🏗️ Project Structure

```
todo/
├── backend/                 # FastAPI backend
│   ├── auth.py             # Authentication routes and logic
│   ├── config.py           # Loads environment variables
│   ├── database.py         # PostgreSQL connection
│   ├── greet.py            # Greeting routes
│   ├── main.py             # FastAPI app entrypoint
│   ├── todos.py            # Todo CRUD operations
│   ├── utils.py            # Utility functions
│   ├── requirements.txt    # Python dependencies
│   └── .env                # Environment variables (not committed)
├── frontend/               # React frontend
│   ├── public/            # Static files
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── App.jsx        # Main App component
│   │   └── index.js       # Entry point
├── .vscode/               # VS Code tasks
├── start_servers.bat      # Batch script to start both servers
└── README.md              # This file
```

## 🛠️ Getting Started

### Backend (FastAPI)
1. `cd backend`
2. Create a `.env` file with your PostgreSQL credentials (see `.env.example` if provided)
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `uvicorn main:app --reload`

### Frontend (React)
1. `cd frontend`
2. Install dependencies: `npm install`
3. Start: `npm start`

### Environment Variables
Store all sensitive info (DB credentials, secrets) in `backend/.env` (never commit this file).

## � Deployment

- Deploy backend (FastAPI) to Render, Railway, or Fly.io
- Deploy frontend (React) to Vercel or Netlify
- Set frontend API URLs to your deployed backend

## 📄 License

This project is licensed under the MIT License.

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
