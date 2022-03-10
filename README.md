# Pitches app
## Owner

Brian Otieno

### Contact
Email: brian.otieno@student.moringaschool.com

## User Story
 - Register or sign up on subsequent visits
 - Post short pitches of different categories
 - Comment on and like pitches from different users
 - Register to be allowed to log in to the application
 - View pitches from the different categories.
 - Submit a pitch to a specific category of their choice.


## Technology used

* [Python3.8]
* [Flask]
* [Heroku]


## BDD
| Behaviour | Input | Output |
* Load the page | **On page load**  View Pitches, Select between signup and login
* Select SignUp| **Email**,**Username**,**Password**  Redirect to login
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories, author and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|


## Development Installation
To get the code..

1. Cloning the repository:
  ```terminal
 https://github.com/Otybrian/pitch-project.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd pitch-project
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `https://127.0.0.1:5000`.

## License
* *MIT License:*