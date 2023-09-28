```
#             .___      __     _____          __                         __  .__               
#    ______ __| _/_____/  |_  /  _  \  __ ___/  |_  ____   _____ _____ _/  |_|__| ____   ____  
#   /  ___// __ |/ __ \   __\/  /_\  \|  |  \   __\/  _ \ /     \\__  \\   __\  |/  _ \ /    \ 
#   \___ \/ /_/ \  ___/|  | /    |    \  |  /|  | (  <_> )  Y Y  \/ __ \|  | |  (  <_> )   |  \
#  /____  >____ |\___  >__| \____|__  /____/ |__|  \____/|__|_|  (____  /__| |__|\____/|___|  /
#       \/     \/    \/             \/                         \/     \/                    \/ 
```
# flask-api

- sample project building an api using flask and python

<h2>Introduction</h2>
<hr>

- This project is made for anyone who is looking for an example of how to create a rest endpoint using Python and Flask

- This serice calls a local sqlite database. Please see database directory for more details

- This project was written using VS Code

<h2>Installing Project Dependencies</h2>
<hr>

[This project uses venv for virtual environment management.](https://docs.python.org/3/tutorial/venv.html)

- Create a virtual environment with:

    `python3 -m venv venv`

- Installing Flask dependencies with:
    `pip install flask[all]`


<h2>Running the application</h2>
<hr>

- After you have preformed all the dependency installations from above, you can run the following command on your terminal to start this app

    `flask run --debug` or `python app.py`

<h2>Project Database</h2>
<hr>

- This project uses local sqlite for a repository

<h2>Swagger</h2>
<hr>

- This project contains a swagger ui. [For more informationregarding swagger. Click here](https://swagger.io/)

- To view this api's swaggeer ui, run this application the navigate to [http://localhost:8000/ui/]

<h2>Rest Api</h2>
<hr>

<h3>Users API</h3>

- GET - getAll:localhost:8000/users/v1
- GET - getByUsername: http://localhost:8000/users/darth
- PUT - updateUserEmail: http://localhost:8000/users/darth + include json bosy with new email
- DELETE - deleteUsername: http://localhost:8000/users/darth

<h3>Locations API</h3>

- GET - getByUsername: http://localhost:8000/locations/v1
- GET - getByUsername: http://localhost:8000/locations/v1/ca
- PUT - updateUserEmail: http://localhost:8000/locations/v1/ca + include json bosy with new capital
- DELETE - deleteUsername: http://localhost:8000/locations/v1/ca

<h2>TDD - Integration Tests</h2>
<hr>

- This api is fully tested with Unit Tests and Intergration Tests. Please see tests directory for examples. 

- Tests connect to test.db for integration tests

<h2>Flask Project</h2>
<hr>

- This project is a Flask project. [For more information. Click here](https://flask.palletsprojects.com/en/2.3.x/)

<h2>Continuous Integration(CI)</h2>
<hr>

- A webhook can be setup with Travis CI for all Push and Pull requests

<h2>Questions/Contribute</h2>
<hr>

- Feel free to fork this repo, add to it, and create a pull request if you like to contribute