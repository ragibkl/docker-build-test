# docker-build-test
A simple repo for testing docker image building

## Running the services locally

You need to have Python 3 installed.

Run `api-messages`

```shell
cd api-messages

# only need to do this once or after adding new requirements
./setup.sh

./run.sh
```

In a second shell, run `web-frontend`

```shell
cd api-messages

# only need to do this once or after adding new requirements
./setup.sh

./run.sh
```

In your web browser, open the `web-frontend` site at [http://localhost:5000](http://localhost:5000)
You can also call the `api-messages` api directly at [http://localhost:5001/api/message](http://localhost:5001/api/message)


## Testing the docker build

You need `docker` and `docker compose` on your local machin
I recommend Docker for Desktop.

```
# With docker & docker-compose
docker-compose up -d --build

# OR if you use Docker for Desktop
docker-compose up -d --build
```

In your web browser, open the `web-frontend` site at [http://localhost](http://localhost) at port 80.
The `api-messages` service is not exposed in this way.
