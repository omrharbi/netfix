
# NetFix - Home Services Platform

A Django-based web application that connects customers with service providers for various home maintenance and repair services.

## Project Overview

NetFix is a platform where:
- **Companies** can register and create services they offer
- **Customers** can browse and request services from registered companies

### Key Features

- Two user types: Companies and Customers
- Service categories: Air Conditioner, Carpentry, Electricity, Gardening, Housekeeping, Interior Design, Locks, Painting, Plumbing, Water Heaters, and more
- Company profiles with service listings
- Customer profiles with service request history
- Service browsing by category and popularity
- Service request system with cost calculation

## Project Structure

The project consists of three main Django apps:
- **services**: Handles service creation, display, and requests
- **users**: Manages user registration, authentication, and profiles
- **main**: Common features like homepage and navigation

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Setup Instructions

### 1. Install Python

#### On Windows:
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer and check "Add Python to PATH"
3. Verify installation: `python --version`

#### On macOS:
```bash
# Using Homebrew
brew install python3

# Or download from python.org
```

#### On Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. Create Project Directory
```bash
mkdir netfix-project
cd netfix-project
```

### 3. Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv netfix_env

# Activate virtual environment
# On Windows:
netfix_env\Scripts\activate

# On macOS/Linux:
source netfix_env/bin/activate
```

### 4. Install Django
```bash
# Install specific Django version
pip install Django==3.1.14

# Or install latest version
pip install Django

# Verify installation
python -m django --version
```

### 5. Create Django Project
```bash
# Create new Django project
django-admin startproject netfix

# Navigate to project directory
cd netfix

# Create the three required apps
python manage.py startapp main
python manage.py startapp users
python manage.py startapp services
```

### 6. Initial Database Setup
```bash
# Create initial migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to see the application.

## User Registration Requirements

### Customer Registration:
- Email (unique)
- Password & confirmation
- Username (unique)
- Date of birth

### Company Registration:
- Email (unique)
- Password & confirmation
- Username (unique)
- Field of work (from predefined list)

## Service Management

### Service Fields Available:
- Air Conditioner
- All in One
- Carpentry
- Electricity
- Gardening
- Home Machines
- Housekeeping
- Interior Design
- Locks
- Painting
- Plumbing
- Water Heaters

### Service Attributes:
- Name
- Description
- Field/Category
- Price per hour
- Creation date (auto-generated)

## Key Pages

1. **Homepage**: Overview and navigation
2. **Service Listings**: 
   - Most requested services
   - All services (newest first)
   - Services by category
3. **Individual Service Pages**: Detailed service information
4. **User Profiles**: 
   - Customer: Personal info + service request history
   - Company: Business info + services offered
5. **Registration/Login**: User authentication

## Development Commands

```bash
# Start development server
python manage.py runserver

# Create new app
python manage.py startapp <app_name>

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (production)
python manage.py collectstatic
```

## Project Files Structure

```
netfix/
├── manage.py
├── netfix/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/
├── users/
│   ├── templates/users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── services/
│   ├── templates/services/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
└── static/
    └── css/
        └── style.css
```

## Next Steps

1. Define models in `models.py` files
2. Create forms in `forms.py` files
3. Implement views in `views.py` files
4. Configure URLs in `urls.py` files
5. Create HTML templates
6. Implement authentication and authorization
7. Add service request functionality

## Bonus Features (Optional)

- Service rating system
- Pagination for service listings
- Advanced search and filtering
- Email notifications
- Service booking calendar

## Troubleshooting

### Common Issues:

1. **Django version conflicts**: Ensure you're using Django 3.1.14 or compatible version
2. **Database errors**: Run `python manage.py migrate` after model changes
3. **Static files not loading**: Check `STATIC_URL` and `STATICFILES_DIRS` in settings.py
4. **Import errors**: Verify app names are added to `INSTALLED_APPS` in settings.py

### Getting Help:
- Django Documentation: https://docs.djangoproject.com/
- Django Tutorial: https://docs.djangoproject.com/en/3.1/intro/tutorial01/

## License

This project is for educational purposes.
