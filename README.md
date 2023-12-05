# Task manager
Task Manager is a custom-built task management system designed to streamline collaboration and enhance productivity within your team. It allows Developers, Designers, Project Managers, and QA specialists to create tasks, assign them to team members, and track progress in the IT-sphere. Team members can efficiently manage their work, ensuring tasks are completed before deadlines.

## The content


- [Check it out!](#check-it-out)
- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Contribute](#contribute)


## Check it out!

[Task manager deployed to Render](https://task-manager-o8qw.onrender.com/accounts/login/)

## Features


- **Create tasks:** Team members can create tasks with detailed descriptions.
- **Assign tasks:** Assign tasks to specific team members based on their roles.
- **Track progress:** Mark tasks as done to track their completion status.
- **Worker management:** Manage team members' information, including their positions.



## Requirements

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SelFisher1488/task-manager.git
2. **Navigate to the project directory:**
   ```bash
   cd task-manager

3. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate # (For Windows)
   source venv/bin/activate # (For Linux/Mac)

4. **Install requirements:**
   ```bash
   pip install -r requirements.txt
5. **Apply database migrations:**
   ```bash
   python manage.py migrate
6. **Load some data in database (optional):**
   ```bash
   python manage.py loaddata data.json
7. **Start the development server:**
   ```bash
   python manage.py runserver
8. **Access the application:**
Open a web browser and go to http://127.0.0.1:8000/ to access the Task Manager application.

## Getting Started

- Create and manipulate tasks 
- Assign team members to task and assign yourself if you need
- Monitor the task process
- Extend existing positions, task types

## Contribute
Contributions are welcome!

- If you load data from prepared file, you can use prepared admin user:
  - Login: "admin"
  - Password: "admin"


Feel free to add new data and exploit admin panel by your wishes.

