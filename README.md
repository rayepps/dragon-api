# Dragon 🐉🔥
## A service that handles todos... like a dragon?

Api can currently be hit at `https://sandbox-dragon-api.greendragon.pro`. Contact me to request an api key for access. If you need help creating the proper request to interact with the api import the `postman.json` file to postman and use the template requests provided.

*api key* = `4a7bdfb5cfb0453ebe2c3628a6edac07`

### TODO

- [] Setup integration tests :(
- [] Actually write out all the unit tests :(
- [] Please the gods of lint
- [] Add helpful log lines
- [] Add parameter validation for data posted in upload and update forms
- [] Handle s3 and dynamo changes as a single transaction and roll one back when another fails so that the file storage is never out of sync with the database
- [] Treat thumbnails like actual thumbnails and resize them and store as a second image
- [] Add nginx (or some other gateway interface) so were not working off of the flask devlopment server
- [] Add Travis build step that verifies the `version.cfg` has been incremented and implements semvar

### Running The Project Locally
The project uses Docker to build and run locally. So long as you have the dependencies installed (Docker and Docker Compose) you should simply need to run:

- `docker-compose build`
- `docker-compose up`

The api will start and be available at `localhost:5000`. The following endpoints will be available:

- `POST /api/v1/todos` => Create a new todo
- `GET /api/v1/todos` => Get a list of all todos
- `GET /api/v1/todos/<todo_id>` => Get a todo by id
- `PUT /api/v1/todos/<todo_id>` => Update a todo by id
- `DELETE /api/v1/todos/<todo_id>` => Remove a todo by id
- `POST /api/v1/todos/<todo_id>/attach` => Add an attachent file to a todo
- `DELETE /api/v1/todos/<todo_id>/detatch` => Remove attachment from todo

### Developing The Project Locally
Make your changes and before pushing a feature branch run

- `make lint`
- `make test-unit`

both of these will be run by travis before allowing any PRs to be merged to develop.

## Deploying The Service
Deployments are setup using GitHub web hooks configured from branches named `deploy-{env}`. If you push/merge a change to the `deploy-sandbox` branch GitHub will tell AWS Code Pipeline and the pipeline will build the docker image and deploy it to the sandbox environment.
