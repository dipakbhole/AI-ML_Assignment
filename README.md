# 📝 Project Name
Flask Chat Assistant for Employee Database

# 📌 Overview
A chatbot that interacts with an SQLite database to answer user queries about employees, departments, and salaries. The assistant processes natural language queries, converts them into SQL, and returns formatted responses.

# 📌 Features

✅ Supports the following queries:

- “Show me all employees in the [department] department.”

- “Who is the manager of the [department] department?”

- “List all employees hired after [date].”

- “What is the total salary expense for the [department] department?”

✅ Handles errors gracefully:

- Returns meaningful messages when no results are found.
- Validates department names and input formats.
- Prevents SQL injection risks.

# 📂 Project Structure

📦 flask-chat-assistant/
 - ┣ 📜 app.py                 # Main Flask API
 - ┣ 📜 requirements.txt        # Dependencies
 - ┣ 📜 company.db              # SQLite database
 - ┣ 📜 README.md               # Project documentation

# 🔧 Installation & Setup

# 📌 Prerequisites

Ensure you have the following installed:

- Python 3.7+

- Flask (pip install flask)

- SQLite3 (pre-installed in Python)

- Optional: Render, AWS, Docker for deployment

# 📌 Install Dependencies

- Clone the repository and install required Python packages:

- git clone https://github.com/dipakbhole/AI-ML_Assignment.git

- pip install -r requirements.txt

# 📌 Run Locally

Start the Flask API:

- python app.py

 - Test the API using curl or Postman

# 🚀 Deployment Instructions

🔹 Deploy with Render

- Go to Render

- Click New Web Service.

- Connect your GitHub repository.

- Select:

  Build Command:
  
      pip install -r requirements.txt

  Start Command:
  
      gunicorn app:app

- Click Deploy.


- Test Your API

   Once deployed, Render will provide a URL like:

      https://chat-assistant-slc9.onrender.com

- Test using curl or Postman


# 🗄️ Database Schema

Table: Employees

![image](https://github.com/user-attachments/assets/c01587e4-c811-4490-99a9-be8f46051a69)

Table: Departments

![image](https://github.com/user-attachments/assets/0b8887ed-a2a4-471a-95af-831a51198df3)



# 📝 API Endpoints

1️⃣ /chat (POST)
Handles user queries and returns responses.

Request Format:

    {
       "query": "Who is the manager of the Engineering department?"
    }

Response Format:

    {
       "response": "Bob"
    }

# 📌 Deliverables:

- Hosted URL: https://chat-assistant-slc9.onrender.com

- GitHub Repo: https://github.com/dipakbhole/AI-ML_Assignment.git

# 📌 Future Improvements

- Add more flexible NLP processing to understand varied query structures.

- Improve security and implement authentication.

- Expand dataset to include more fields and complex queries.

# 📌 License

This project is open-source under the MIT License.

# 📩 Contact

👤 Dipak Bhole

📧 Email: dipakbhole1995@gmail.com



