# Demon's Souls Wiki
This is the codebase for the Demon's Souls Wiki, a fan-created wiki for the video game Demon's Souls. The wiki is built using Django and Python.

## About
The Demon's Souls Wiki is a collaborative website dedicated to documenting everything related to the Demon's Souls video game series. The wiki format allows anyone to create and edit articles, making it easy for fans to share information and strategies about these classic games.

The goal is to create a comprehensive and accurate informational resource for Demon's Souls fans new and old.

## Features
- User registration and profiles
- Article creation and editing
- Comments

## Tech Stack
- Framework: Django
- Language: Python
- Database: SQLite

## Setup
To run this project locally:
- Clone this repo
- Create and activate a virtual environment
- Configure settings and database: python manage.py migrate
- Create admin user: python manage.py createsuperuser
- Run development server: python manage.py runserver

The wiki should now be running at http://localhost:8000! Sign in with your admin credentials.
