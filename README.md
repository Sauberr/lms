## Learning Management System (LMS)

This project showcases a streamlined Learning Management System (LMS) built with Django 4.2, developed as part of the Hillel Python Pro course.  It demonstrates the fundamental concepts of building a web application for educational purposes, featuring user authentication with email verification and social media login options.  To populate the system with realistic data, the project utilizes the faker library for generating sample users, courses, and other relevant information.

#### Stack:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.11 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files> 
   ```

4. Run application
   ```
      py manage.py runserver
   ```

## License

This project uses the [MIT] license(https://github.com/Sauberr/lms/blob/master/LICENSE)

## Contact 

To contact the author of the project, write to email 𝚍𝚖𝚒𝚝𝚛𝚒𝚢𝚋𝚒𝚛𝚒𝚕𝚔𝚘@𝚐𝚖𝚊𝚒𝚕.𝚌𝚘𝚖.
