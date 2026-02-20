# 🔐 Flask Authentication System

A simple and secure User Authentication System built using **Flask** and **SQLite**.  
This project demonstrates backend validation, session management, password security, and protected routes.

---

## 🚀 Features

- User Registration
- User Login
- Password Validation
- Unique Email Validation
- Flash Messages for Errors & Success
- Secure Password Hashing
- Session-based Authentication
- Protected Dashboard Route
- Logged-in User Name Displayed on Dashboard
- Logout Functionality

---

## 🛠 Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML (Jinja2 Templates)
- Bootstrap (for styling)

---

## 📂 Project Structure


auth-project/
│
├── app.py
├── users.db
│
├── templates/
│ ├── base.html
│ ├── register.html
│ ├── login.html
│ └── dashboard.html
│
└── README.md


---

## 🧠 Authentication Flow

### 1️⃣ Registration

Validations implemented:
- Name cannot be empty
- Email cannot be empty
- Password cannot be empty
- Password must be at least 6 characters
- Email must be unique

If validation fails:
- Flash error message is displayed

If validation succeeds:
- Password is hashed
- User is saved in database
- Success message shown

---

### 2️⃣ Login

Validations:
- Email cannot be empty
- Password cannot be empty
- Email must exist
- Password must match (hashed comparison)

If successful:
- Session is created
- User is redirected to dashboard

---

### 3️⃣ Dashboard

- Route is protected
- Only logged-in users can access
- Displays logged-in user's name dynamically
- If user not logged in → redirected to login page

Example:

Welcome, Raghav!


---

### 4️⃣ Logout

- Clears session
- Redirects to login page
- Flash message displayed

---

## 🔒 Security Implementation

- Password hashing using:
  ```python
  from werkzeug.security import generate_password_hash, check_password_hash

Session-based authentication

Redirect-after-POST pattern

Backend validation for all forms

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/Raghav007-maker/FULL_STACK/edit/main/AuthPage.git
cd AuthPage
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install flask flask-sqlalchemy
4️⃣ Run Application
python app.py

App will run at:

http://127.0.0.1:5000
🗄 Database

SQLite database (users.db)

Automatically created using:

db.create_all()
📌 Future Improvements

Add Email Validation Regex

Add Remember Me functionality

Implement Flask-Login

Add Password Reset via Email

Add CSRF Protection using Flask-WTF

Add User Roles (Admin/User)

🎯 Why This Project?

This project demonstrates:

Understanding of backend validation

Secure password handling

Session management

Authentication flow

Clean Flask architecture

It is suitable for:

Backend beginner projects

College assignments

Internship submissions

Interview portfolio

👨‍💻 Author

Your Name : Raghav Bansal
GitHub: https://github.com/Raghav007-maker/FULL_STACK/edit/main/AuthPage

⭐ If you like this project, give it a star!
