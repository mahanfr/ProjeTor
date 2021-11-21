# Pro[ j ]tor

Online Project Management Platform

## Getting Started
to get started for development, run the following commands in install section:

### requirements:
- python 3.10
- node 14.x

### install:
install python requirements after creating virtual environment:
```bash 
pip install -r requirements.txt
```
install node requirements:
```bash
cd ./frontend
npm install 
```
build ui components like tailwindcss:
```bash
npm run build
```

### Running:
for running react app, you can run the following commands:
```bash
cd ./frontend
npm run start
```
for running django app first you need to migrate the database:
```bash
cd ./backend
python manage.py migrate user
python manage.py migrate
```
create a superuser:
```bash
python manage.py createsuperuser
```
then run the django app:
```bash
python manage.py runserver
```