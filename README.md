# Project Management Application

Easiest way to **manage** your **project** and **tasks**. **Manage** all your team's work in one place and improve accountability.

## Features

* Create multiple projects.
* Create a description of a project.
* Set deadlines of the project.
* Create multiple tasks in one project.
* to-do list in a task.
* The person who creates a project can only delete and update.
* Track of user who has created project.

# Installation

## On Local Machine

Open Command Prompt and set a path where the project is cloned or downloaded.

For Example, My Project is located on the desktop.

```Command Prompt
    C:\Users\Shaan\Desktop\Project_Task
```

### Run the following commands to have the server up and running.

Make sure that in your system **python** is installed and the python --version should be **3.6** or **above**.

With the help of pip, a tool to manage and install python packages, to install **virtualenv**.

```Command Prompt
    C:\Users\Shaan\Desktop\Project_Task>pip install virtualenv
```
After installing **virtualenv** let's create it.

```Command Prompt
    C:\Users\Shaan\Desktop\Project_Task>virtualenv venv
```

Now your Project_Task directory looks like:

* Project_Task
    * myproject
    * venv
    * requirement

Virtual Environement is created, to **activate** it.

```Command Prompt
    C:\Users\Shaan\Desktop\Project_Task>venv\Scripts\activate
```

Your command Prompt looks like:

```Command Prompt
    (venv) C:\Users\Shaan\Desktop\Project_Task>
```

Now, let's install **django**

```Command Prompt
    (venv) C:\Users\Shaan\Desktop\Project_Task>pip install django
```

Make sure your django --version should be **3.2.7** or **above**.

Install a third party django application for **forms**.

```Command Prompt
    (venv) C:\Users\Shaan\Desktop\Project_Task>pip install django-crispy-forms
```

For a user, the profile picture should be saved. Run this command.

```Command Prompt
    (venv) C:\Users\Shaan\Desktop\Project_Task>pip install Pillow
```

After installing all libraries. Now it's time to run a project.Before that you have to go in myproject folder.

```Command Prompt
    (venv) C:\Users\Shaan\Desktop\Project_Task>cd myproject
```

Before running your project your **Command Prompt** should look like:

```Command Prompt
    (venv) C:\Users\Shaan\Desktop\Project_Task\myproject
```

Run the command below to run a project at localhost.

```Command Prompt
    (venv) C:\Users\Shaan\Desktop\Project_Task\myproject>python manage.py runserver
```

The **URL** which you will get run in your Web browser:**http://127.0.0.1:8000**

You will get a dummy data.

If you want that dummy data should not be there [connect me](https://www.linkedin.com/in/aadil-kadiwal)