# Task manager
Task Manager is a custom-built task management system designed to streamline collaboration and enhance productivity within your team. It allows Developers, Designers, Project Managers, and QA specialists to create tasks, assign them to team members, and track progress in the IT-sphere. Team members can efficiently manage their work, ensuring tasks are completed before deadlines.

## The content


- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)

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
3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
4. **Apply database migrations:**
   ```bash
   python manage.py migrate
5. **Load some data in database (optional):**
   ```bash
   python manage.py loaddata data.json
6. **Start the development server:**
   ```bash
   python manage.py runserver
7. **Access the application:**
Open a web browser and go to http://127.0.0.1:8000/ to access the Task Manager application.

## Getting Started

- Create and manipulate tasks 
- Assign team members to task and assign yourself if you need
- Monitor the task process
- Extend existing positions, task types

## How to Contribute
Contributions are welcome! To contribute, follow these steps:

- **Fork the repository:** Click the "Fork" button on the top right corner of this repository's page.

- **Clone your fork:** Clone the repository to your local machine using the following command:
   ```bash
  git clone https://github.com/SelFisher1488/task-manager.git
- **Create Your Feature Branch:** Start working on a new feature by creating a dedicated branch. Choose a descriptive name for the branch, such as feature/YourFeature:
   ```bash
  git checkout -b feature/YourFeature
- **Commit Your Changes:** Make your desired changes to the codebase and commit them:
   ```bash
   git add .
   git commit -m "name your commit"

- **Push To The Branch:** Push your changes to your fork on GitHub:
   ```bash
  git push origin feature/YourFeature

- **Create A New Pull Request:** Go to the original repository on GitHub and click on the "New Pull Request" button. Provide details about your changes and submit the pull request for review.

- If you load data from prepared file, you can use prepared admin user:
  - Login: "admin"
  - Password: "admin"

Feel free to add new data and exploit admin panel by your wishes.

