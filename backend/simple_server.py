

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse
from database import get_db, init_db
import utils

class TodoHandler(BaseHTTPRequestHandler):
    
    def _send_cors_headers(self):
        """Send CORS headers"""
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:3000')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Access-Control-Allow-Credentials', 'true')
    
    def _send_json_response(self, data, status=200):
        """Send JSON response"""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self._send_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def _send_error(self, message, status=400):
        """Send error response"""
        self._send_json_response({"error": message}, status)
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        path = self.path
        
        if path == '/api/v1/todos':
            self._get_all_todos()
        elif path.startswith('/api/v1/todos/title/'):
            title = path.split('/')[-1]
            self._get_todo_by_title(title)
        elif path.startswith('/api/v1/todos/status/'):
            status = path.split('/')[-1]
            self._get_todos_by_status(status)
        elif path == '/':
            self._send_json_response({"message": "Todo API Server", "status": "running"})
        else:
            self._send_error("Not found", 404)
    
    def do_POST(self):
        """Handle POST requests"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode())
        except json.JSONDecodeError:
            self._send_error("Invalid JSON")
            return
        
        if self.path == '/api/v1/todos':
            self._create_todo(data)
        elif self.path == '/signup':
            self._signup(data)
        elif self.path == '/signin':
            self._signin(data)
        else:
            self._send_error("Not found", 404)
    
    def do_PUT(self):
        """Handle PUT requests"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode())
        except json.JSONDecodeError:
            self._send_error("Invalid JSON")
            return
        
        if self.path == '/api/v1/todos':
            self._update_todo(data)
        else:
            self._send_error("Not found", 404)
    
    def do_DELETE(self):
        """Handle DELETE requests"""
        if self.path.startswith('/api/v1/todos/delete-by-title/'):
            title = self.path.split('/')[-1]
            self._delete_todo(title)
        else:
            self._send_error("Not found", 404)
    
    def _get_all_todos(self):
        """Get all todos"""
        conn = get_db()
        if not conn:
            self._send_error("Database connection failed", 500)
            return
        
        cursor = conn.cursor()
        cursor.execute("SELECT title, descr, status FROM todo")
        todos = []
        for row in cursor.fetchall():
            todos.append({
                "title": row["title"],
                "desc": row["descr"],
                "status": row["status"]
            })
        conn.close()
        self._send_json_response(todos)
    
    def _get_todo_by_title(self, title):
        """Get todo by title"""
        conn = get_db()
        if not conn:
            self._send_error("Database connection failed", 500)
            return
        
        cursor = conn.cursor()
        cursor.execute("SELECT title, descr, status FROM todo WHERE title = ?", (title,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            todo = {
                "title": row["title"],
                "desc": row["descr"],
                "status": row["status"]
            }
            self._send_json_response(todo)
        else:
            self._send_error(f"Todo not found with title {title}", 404)
    
    def _get_todos_by_status(self, status):
        """Get todos by status"""
        conn = get_db()
        if not conn:
            self._send_error("Database connection failed", 500)
            return
        
        cursor = conn.cursor()
        cursor.execute("SELECT title, descr, status FROM todo WHERE status = ?", (status,))
        todos = []
        for row in cursor.fetchall():
            todos.append({
                "title": row["title"],
                "desc": row["descr"],
                "status": row["status"]
            })
        conn.close()
        self._send_json_response(todos)
    
    def _create_todo(self, todo):
        """Create a new todo"""
        conn = get_db()
        if not conn:
            self._send_error("Database connection failed", 500)
            return
        
        cursor = conn.cursor()
        # Check if title already exists
        cursor.execute("SELECT COUNT(*) FROM todo WHERE title = ?", (todo['title'],))
        if cursor.fetchone()[0] > 0:
            conn.close()
            self._send_error(f"Todo with title {todo['title']} already exists", 409)
            return
        
        # Create the todo
        cursor.execute(
            "INSERT INTO todo (title, descr, status) VALUES (?, ?, ?)",
            (todo['title'], todo['desc'], todo['status'])
        )
        conn.commit()
        conn.close()
        self._send_json_response({"success": True}, 201)
    
    def _update_todo(self, todo):
        """Update a todo"""
        conn = get_db()
        if not conn:
            self._send_error("Database connection failed", 500)
            return
        
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE todo SET descr = ?, status = ? WHERE title = ?",
            (todo['desc'], todo['status'], todo['title'])
        )
        conn.commit()
        conn.close()
        self._send_json_response({"success": True})
    
    def _delete_todo(self, title):
        """Delete a todo"""
        conn = get_db()
        if not conn:
            self._send_error("Database connection failed", 500)
            return
        
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todo WHERE title = ?", (title,))
        conn.commit()
        conn.close()
        self._send_json_response({"success": True})
    
    def _signup(self, user_data):
        """User signup"""
        conn = get_db()
        if not conn:
            self._send_error("Database connection failed", 500)
            return
        
        cursor = conn.cursor()
        # Check if user exists
        cursor.execute("SELECT COUNT(*) FROM auth WHERE email = ?", (user_data['email'],))
        if cursor.fetchone()[0] > 0:
            conn.close()
            self._send_error(f"User with {user_data['email']} already exists", 409)
            return
        
        # Create user
        encoded_password = utils.encode(user_data['password'])
        cursor.execute(
            "INSERT INTO auth (user, email, password) VALUES (?, ?, ?)",
            (user_data['username'], user_data['email'], encoded_password)
        )
        conn.commit()
        conn.close()
        self._send_json_response({"status": "ok", "data": "user signed up successfully"})
    
    def _signin(self, user_data):
        """User signin"""
        conn = get_db()
        if not conn:
            self._send_error("Database connection failed", 500)
            return
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM auth WHERE email = ?", (user_data['email'],))
        user_record = cursor.fetchone()
        conn.close()
        
        if not user_record:
            self._send_error(f"User with {user_data['email']} doesn't exist", 404)
            return
        
        if not utils.verify_passwords(user_data['password'], user_record['password']):
            self._send_error("Incorrect username or password", 401)
            return
        
        self._send_json_response({"status": "ok", "data": "user logged in successfully"})

def run_server(port=8000):
    """Run the server"""
    # Initialize database
    print("Initializing database...")
    init_db()
    
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, TodoHandler)
    print(f"Todo API Server running on http://127.0.0.1:{port}")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
