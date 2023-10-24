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


- This project is made for anyone who is looking for an example of how to create a rest endpoint using Python and Flask

- This service calls a local sqlite database. Please see database directory for more details

- This project was written using VS Code

<h2>Installing Project Dependencies</h2>


[This project uses venv for virtual environment management.](https://docs.python.org/3/tutorial/venv.html)

- Create a virtual environment with:

    `python3 -m venv venv`

- Installing Flask dependencies with:
    `pip install flask[all]`


<h2>Running the application</h2>


- After you have preformed all the dependency installations from above, you can run the following command on your terminal to start this app

    `flask run --debug` or `python app.py`

<h2>Project Database</h2>


- This project uses local sqlite for a repository

<h2>Swagger</h2>


- This project contains a swagger ui. [For more information regarding swagger. Click here](https://swagger.io/)

- To view this api's swaggeer ui, run this application the navigate to [http://localhost:8000/ui/]

<h2>Rest Api</h2>


<h3>Users API</h3>

- GET - getAll:localhost:8000/users/v1
- GET - getByUsername: http://localhost:8000/users/darth
- PUT - updateUserEmail: http://localhost:8000/users/darth + include json bosy with new email
- DELETE - deleteUsername: http://localhost:8000/users/darth

<h2>TDD - Integration Tests</h2>


- This api is fully tested with Unit Tests and Intergration Tests. Please see tests directory for examples. 

- Tests connect to test.db for integration tests

<h2>Flask Project</h2>


- This project is a Flask project. [For more information. Click here](https://flask.palletsprojects.com/en/2.3.x/)

<h2>Continuous Integration(CI)</h2>


- A webhook can be setup with Travis CI for all Push and Pull requests

<h2>Questions/Contribute</h2>


- Feel free to fork this repo, add to it, and create a pull request if you like to contribute

## Docker 
- This application uses Docker. Pease see Dockerfile for image setup. Steps to create a docker image and how to run the app in a container list below. (must have docker installed)

- Create a Docker image: `docker build -t flask-api-sdetautomation .`

- Run a Docker container: `docker run -it p 5000:5000 flask-api-sdetautomation`

__***Once the app has started, view the swagger ui by navigating to [https://localhost:5000/ui/]***__

- View Docker images: `docker images`

- View Docker container: `docker ps` 
    - (This command can also be used to fine the container id for stopping or removing containers)

- Stop Docker container: `docker stop <the-container-id>`

- Remove a Docker container: `docker rm <the-container-id>`

- Remove a Docker image: `docker rmi <repository-name>:<tag>`

[Click here for more information regarding Docker](https://docs.docker.com/)

__*Note this flask app by default runs as a development server, not meant for production. Docker and gunicorn is used to productionize this app. This docker container runs as a production WSGI server, with 4 workers via [gunicorn](https://gunicorn.org/)*__