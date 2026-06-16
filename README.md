# Employee Portal Management System

A modern Employee Management Portal built using Django that helps organizations manage employee records, profiles, authentication, and administrative tasks through a clean and responsive web interface.

## Project Overview

This project is a full-stack web application designed to simplify employee management within an organization. It provides secure authentication, employee profile management, dashboard insights, dark mode support, and an easy-to-use administrative interface.

The application demonstrates backend development, database management, authentication systems, responsive web design, and full-stack development using Django.

---

## Features

### Authentication & Security

* Secure Login System
* User Authentication
* Session Management
* Protected Routes
* Admin Access Control

### Employee Management

* Add New Employees
* Update Employee Information
* Delete Employee Records
* Employee Profile Management
* Employee Image Upload Support

### Dashboard

* Employee Statistics
* Employee Directory
* Quick Access Navigation
* Modern Dashboard Interface

### User Interface

* Responsive Design
* Mobile-Friendly Layout
* Dark Mode Support
* Professional UI Design
* Clean Navigation System

### Administration

* Django Admin Panel
* Employee Data Management
* User Management
* Database Operations

---

## Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Database

* SQLite

### Tools

* Git
* GitHub
* VS Code / PyCharm

---

## Screenshots

### Login Page

<img src="screenshots/login.png" width="900">

### Dashboard

<img src="screenshots/dashboard.png" width="900">

### Employee List

<img src="screenshots/employees.png" width="900">

### Employee Profile

<img src="screenshots/profile.png" width="900">

### Dark Mode

<img src="screenshots/darkmode.png" width="900">

> Create a folder named `screenshots` and place your images there.

---

## Project Structure

```text
employee-portal/
│
├── employees/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── media/
├── static/
├── templates/
├── screenshots/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation Guide

### 1. Clone Repository

```bash
git clone https://github.com/Ayush01-asr/employee-portal.git
```

### 2. Navigate to Project Folder

```bash
cd employee-portal
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Skills Demonstrated

* Full-Stack Web Development
* Django Framework
* Database Design
* CRUD Operations
* Authentication Systems
* Responsive Web Design
* Backend Development
* Frontend Development
* Git Version Control
* Software Engineering Principles

---

## Key Learning Outcomes

* Building real-world Django applications
* Designing database models
* Managing user authentication
* Implementing CRUD functionality
* Creating responsive interfaces
* Structuring scalable projects
* Working with Git and GitHub

---

## Future Enhancements

* Leave Management System
* Attendance Tracking
* Payroll Management
* Email Notifications
* Employee Performance Analytics
* REST API Integration
* Docker Deployment
* AI-Based Employee Insights
* PDF Report Generation
* Excel Export Functionality

---

