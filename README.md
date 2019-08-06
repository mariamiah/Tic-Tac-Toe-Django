### Tic-Tac-Toe
Web application to play the game of Tic-Tac-Toe
### Features
- User login
- Database
- Making Moves
- Sending invitations
### Getting started
#### Step 1(Install Python version 3)
- Install Python3 on your local machine by following this [link](https://realpython.com/installing-python/)

#### Step 2(Set up and activate the virtual environment)
- Set up a virtual environment in your project folder via your `terminal`. This will help you isolate dependencies for each project to avoid conflicting dependencies in different projects
- Run `python3 -m venv django-env`
- In order to activate the virtual environment, run `. django-env/bin/activate` for linux and macOS. For windows, run `django-env\Scripts\activate.bat`

#### Step 3(Install Django)
- Ensure you are working in your virtual environment `django-env`
- Run `pip install django`
- To specify a version of django, run `pip install django==1.11`

#### Step 4(Start a Django project)
- Create a new django project by running `django-admin startproject tictactoe`
- Navigate to the newly created folder `tictactoe` by running `cd tictactoe`
- Run the project by typing `python manage.py runserver`
- Also run the project in a code editor such as `pycharm`, `vscode` or `atom`