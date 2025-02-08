import sqlite3
import re
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('company.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to process user queries
def process_query(user_input):
    user_input = user_input.lower()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Pattern matching for different query types
    match = re.match(r'show me all employees in the (\w+) department', user_input)
    if match:
        department = match.group(1).capitalize()
        cursor.execute("SELECT Name FROM Employees WHERE Department = ?", (department,))
        employees = [row["Name"] for row in cursor.fetchall()]
        response = employees if employees else "No employees found in this department."

    else:
        match = re.match(r'who is the manager of the (\w+) department', user_input)
        if match:
            department = match.group(1).capitalize()
            cursor.execute("SELECT Manager FROM Departments WHERE Name = ?", (department,))
            manager = cursor.fetchone()
            response = manager["Manager"] if manager else "Department not found."

        else:
            match = re.match(r'list all employees hired after (\d{4}-\d{2}-\d{2})', user_input)
            if match:
                date = match.group(1)
                cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
                employees = [row["Name"] for row in cursor.fetchall()]
                response = employees if employees else "No employees hired after this date."

            else:
                match = re.match(r'what is the total salary expense for the (\w+) department', user_input)
                if match:
                    department = match.group(1).capitalize()
                    cursor.execute("SELECT SUM(Salary) FROM Employees WHERE Department = ?", (department,))
                    total_salary = cursor.fetchone()[0]
                    response = f"Total salary expense: ${total_salary}" if total_salary else "Department not found or no salaries available."
                else:
                    response = "Sorry, I didn't understand that question."
    
    conn.close()
    return response

# API route to handle chat queries
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_query = data.get("query", "")
    response = process_query(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
