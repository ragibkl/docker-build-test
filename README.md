# docker-build-test

A simple repo for testing docker image building automation

## Running the services locally

You need to have Python 3 installed.

Run `api-messages`

```shell
cd api-messages

# only need to do this once or after adding new requirements
./scripts/setup.sh

./scripts/run.sh
```

In a second shell, run `web-frontend`

```shell
cd web-frontend

# only need to do this once or after adding new requirements
./scripts/setup.sh

./scripts/run.sh
```

In your web browser, open the `web-frontend` site at [http://localhost:5000](http://localhost:5000)
You can also call the `api-messages` api directly at [http://localhost:5001/api/message](http://localhost:5001/api/message)


## Testing the docker build

You need `docker` and `docker compose` on your local machine.
I recommend Docker for Desktop.

```
# With docker & docker-compose
docker-compose up -d --build

# OR if you use Docker for Desktop
docker compose up -d --build
```

In your web browser, open the `web-frontend` site at [http://localhost](http://localhost) at port 80.
The `api-messages` service is not exposed in this way.
