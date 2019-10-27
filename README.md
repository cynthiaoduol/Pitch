# Minute-Pitch

#### By [cynthiaoduol](https://github.com/cynthiaoduol)

# Description
This  is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application

## Live Link
[View Site](https://cynthiapitch.herokuapp.com/)


## User Story
* Comment on the different pitches posted py other uses.
* See the pitches posted by other uses.
* Vote on s pitch they have viwed by giving it a upvote or a downvote.
* Register to be allowed to log in to the application
* View pitches from the different categories.
* Submit a pitch to a specific category of their choice.


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | On page load | Select between sign up and  sign in|
| Select SignUp| Email, Username and Password | Redirect to sign in|
| Select Sign in | Username and password | Redirect to page with app pitches and a form to add your own pitch and the pitch category|
| Select comment button | Comment | Form that you input your comment|


## Development Installation
To get the application..

1. Clone the repository:
  https://github.com/cynthiaoduol/Pitch.git


2. Run the application
  ```bash
  ./start.sh
  ```
3. Testing the application
  ```bash
  python3.6 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* Python3.6
* Flask 
* Html for the templates
* CSS for styling


## Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any questions or contributions, please email me at cynthiaobu940@gmail.com

## License
*MIT License*
Copyright (c) 2019 **Cynthia Oduol**