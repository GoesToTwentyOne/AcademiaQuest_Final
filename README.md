# AcademiaQuest

## Project Overview
AcademiaQuest is a web-based application designed to make learning fun and easy for both students and teachers. It serves as an educational hub offering features such as quizzes, studying old questions, ranking systems, and more. Developed using the python,Django framework and following the Model-View-Template (MVT) pattern, AcademiaQuest aims to provide a seamless and user-friendly experience for users in universities.

## Objectives
- Construct a user-friendly educational hub.
- Make learning enjoyable through quizzes, studying old questions, and a ranking system.
- Boost efficiency in education by simplifying quiz creation and study access.

## Project Stakeholders
- **Development Team**: Implement proposed features including user authentication, quiz creation, taking, progress tracking, categories, filtering, ratings, and deployment.
- **Students**: End users who will utilize AcademiaQuest for quizzes, studying old questions, and accessing educational features.
- **Teachers/Instructors/Admins**: Admins who create quizzes and manage educational content. Instructors will use AcademiaQuest for creating quizzes, managing questions, tracking student progress, and accessing features tailored for educators.

## Key Features
1. **User Authentication:**
   - Multi-Factor Authentication (MFA)
   - Account Recovery
   - Role-Based Access Control (RBAC)

2. **Quiz Creation for Admin (Teachers):**
   - Create quizzes with titles, descriptions, categories, and other necessary fields.
   - Add multiple-choice questions to quizzes.
   - Specify correct answers, point values, and time limits for quizzes.
   - Support for rich media in questions.

3. **Quiz Taking:**
   - Display questions one at a time with multiple-choice options.
   - Allow users to browse and select quizzes.
   - Implement timers for quizzes with time limits.
   - Provide immediate feedback and display final scores.

4. **User Progress:**
   - Track and display user quiz history and scores.
   - Show progress indicators for ongoing quizzes.
   - Display leaderboards for top scores.

5. **Quiz Categories and Filtering:**
   - Search functionality for finding quizzes based on keywords or topics.
   - Access to past exam questions sorted by year and level-term.

6. **Quiz Ratings:**
   - Moderation system for reviewing and filtering ratings.

7. **Deployment and Submission:**
   - Continuous Integration/Continuous Deployment (CI/CD)
   - Backup and Recovery

## To Sum Up
AcademiaQuest aims to be an enjoyable learning companion for both students and teachers. By providing features that enhance the learning experience, we're excited about our idea and hope you join us in bringing it to life.

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
