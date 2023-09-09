# Quiz Taker Expert

**Project No:** 0

## Project Overview

**Quiz Zone** is an online platform that empowers users to create and participate in quizzes. It accommodates two distinct user roles: administrators (admins) with the capability to craft quizzes, and end-users (viewers/users) who can engage in these quizzes.

## Project Features

### User Authentication

- **User Registration and Login:** A robust system for user registration and login is implemented.
- **User Profile Management:** Both admins and viewers have the ability to manage their profiles effectively.

### Quiz Creation for Admin

- **Quiz Creation:** Admins have the capability to create quizzes, including specifying titles, descriptions, categories, and other essential information.
- **Multiple-choice Questions:** Admins can add multiple-choice questions to their quizzes.
- **Question Quantity Control:** Each quiz must consist of a minimum of 5 and a maximum of 50 questions. Each question is required to have between 2 and 10 multiple-choice options.
- **Answer Specification:** Admins are allowed to specify correct answers and assign point values to each question.
- **Time Limits:** Admins can optionally set time limits for quizzes.

### Quiz Taking

- **Quiz Selection:** Users can easily explore and select quizzes they wish to take.
- **Sequential Question Presentation:** Questions are presented one at a time, with options for multiple-choice questions.
- **Quiz Timer:** A timer is integrated for quizzes with specified time limits.
- **Immediate Feedback:** Users receive immediate feedback on the correctness of their answers.
- **Final Score Display:** At the end of the quiz, the system calculates and displays the user's final score.

### User Progress

- **Quiz History:** User quiz history, including records of completed quizzes and scores, is meticulously tracked and displayed.
- **Progress Indicators:** Progress indicators for quizzes in progress are provided, either through a progress bar or numerical values.
- **Leaderboards:** Leaderboards showcasing top scores in quizzes are accessible.

### Quiz Categories and Filtering

- **Quiz Categorization:** Quizzes are categorized to facilitate efficient sorting and retrieval.
- **Category Filtering:** Users have the convenience of filtering quizzes by category.

### Quiz Ratings

- **User Ratings:** Users can contribute ratings for quizzes.
- **Average Ratings:** The platform displays an average rating for each quiz.
- **Sorting by Rating:** Quizzes can be sorted by their ratings on a scale from 1 to 7.

### Deployment and Submission

- **Deployment:** The Django-based Quiz Zone website is deployed on a secure and scalable hosting platform.
- **Assignment Submission:** All assignment-related data is submitted in accordance with the instructions provided in the assignment instruction module.

## Conclusion

**Quiz Taker Expert** aspires to deliver an engaging and interactive online quiz platform. With a clear set of features and a well-structured plan, we are confident in our ability to develop a high-quality product that fully aligns with the requirements and expectations outlined in this proposal.

**Backend Development (Django):**
- Python
  
**Frontend Development:**
- HTML5
- CSS3
- Bootstrap 4
- JavaScript
- React.js
  



# Deployment Guide 
```markdown
# Quiz Taker Expert Deployment Guide

This guide will walk you through the process of deploying the Quiz Taker Expert Django web application on PythonAnywhere.com. PythonAnywhere is a cloud-based platform that allows you to host web applications and run Python scripts online.

## Prerequisites

Before you begin, make sure you have the following:

- A PythonAnywhere.com account (you can sign up for free).
- Basic knowledge of Django and Python.
- Git installed on your local machine.

## Deployment Steps

### 1. Clone the Repository

Clone your Quiz Taker Expert repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/Quiz_Taker_Expert.git
```

Replace `yourusername` with your actual GitHub username.

### 2. Create a Virtual Environment

Create a virtual environment on PythonAnywhere using the `mkvirtualenv` command:

```bash
mkvirtualenv env_name
```

Replace `env_name` with the desired name for your virtual environment.

### 3. Activate the Virtual Environment

Activate the virtual environment you just created:

```bash
workon env_name
```

### 4. Install Django and Pillow

Install Django and Pillow within your virtual environment using pip:

```bash
pip install django
pip install pillow
```

### 5. Configure WSGI File

In your PythonAnywhere account, locate the WSGI configuration file. The file should be located at `/var/www/nihadgo75_pythonanywhere_com_wsgi.py`. Edit the file to include the following code:

```python
import os
import sys

# Add the path to your Django project source code
path = '/home/nihadgo75/Quiz_Taker_Expert/quiztaker'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'quiztaker.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Make sure to replace `/home/nihadgo75/Quiz_Taker_Expert/quiztaker` with the correct path to your Django project.

### 6. Update Django Settings

Update your Django `settings.py` file with the following configurations:

```python
DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'core/static/',
]

STATIC_ROOT = BASE_DIR / 'core/static/'

MEDIA_ROOT = BASE_DIR / 'core/media/'
MEDIA_URL = '/media/'
```

Ensure that the `STATIC_URL` and `MEDIA_URL` settings are correctly set based on your project structure.

### 7. Collect Static Files

Collect static files by running the following Django management command:

```bash
python manage.py collectstatic
```

### 8. Restart the Web App

In your PythonAnywhere account, go to the "Web" tab, find your web app, and click the "Reload" button to restart the web app with the updated configurations.

### 9. Access Your Application

Your Quiz Taker Expert web application should now be accessible via the PythonAnywhere URL associated with your web app.

### Additional Information

- **Source Code Location:** `/home/nihadgo75/Quiz_Taker_Expert`
- **Working Directory:** `/home/nihadgo75/`
- **WSGI Configuration File:** `/var/www/nihadgo75_pythonanywhere_com_wsgi.py`

- **URL:** `/static/`
- **Directory:** `/home/nihadgo75/Quiz_Taker_Expert/quiztaker/core/static/`

Congratulations! You have successfully deployed the Quiz Taker Expert Django application on PythonAnywhere.com. You can now access and use your application online.
```

I've added the requested details to the deployment guide.
