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


## Testing the docker build locally

You need `docker` and `docker compose` on your local machine.
I recommend Docker for Desktop.

Build the docker images locally, and run them with `docker compose`
```
# With docker & docker-compose
docker-compose up -d --build

# OR if you use Docker for Desktop
docker compose up -d --build
```

In your web browser, open the `web-frontend` site at [http://localhost](http://localhost) at port 80.
The `api-messages` service is not exposed in this way.

## Building the image for release

### Building the image on Github Actions

Make sure that you are on the `master` git branch, and you are up to date with upstream.

Update the version number in the `docker-tag` file in the service you want to build.
Do be careful to remove any new lines in the file.
Commit the `docker-tag` file and push that to `origin master`

The github actions configured for this repo will pick up this change, and automatically trigger a build.
It will also tag the images using the version in the `docker-tag` file.
The images will then be pushed to docker hub.

You can check the progress on Github Actions [here](https://github.com/ragibkl/docker-build-test/actions).
You can check the uploades images on docker hub:
- https://hub.docker.com/r/ragibkl/example-api-messages
- https://hub.docker.com/r/ragibkl/example-web-frontend


### Manually building images

You need `docker` on your local machine.
I recommend Docker for Desktop.

Make sure that you are logged in to docker hub.
This allows the build scripts to push the images to the docker hub.
You can also disable this by commenting the relevant lines in the `build.sh` files.

Update the version number in the `docker-tag` file in the service you want to build.
In your shell, cd into the directory of the service, and run the build script.
This will build the images with the specified tag version.

Example of building each service.
```shell
echo 0.2.0 > api-messages/docker-tag
echo 0.2.0 > web-frontend/docker-tag

(cd api-messages && ./scripts/build.sh)
(cd web-frontend && ./scripts/build.sh)
```

Check the images have been built.
```shell
docker images

# output
REPOSITORY                            TAG                IMAGE ID       CREATED          SIZE
ragibkl/example-web-frontend          0.2.0              08b9aa8ee0f2   18 minutes ago   79.6MB
ragibkl/example-api-messages          0.2.0              6053cf31e22a   29 minutes ago   91.8MB
```

## Deploying

### Docker Compose

This is the easiest way to deploy.
You need a server with docker and docker-compose installed.
For a server setup, instead of Docker for Desktop, opt for docker-engine setup as well.

SSH into the server you want to deploy.
Create a `docker-compose.yaml` file as follows:
```yaml
services:
  api-messages:
    image: ragibkl/example-api-messages:0.1.0 # update the version number as needed
    restart: always

  web-frontend:
    image: ragibkl/example-web-frontend:0.1.0 # update the version number as needed
    restart: always
    ports:
      - 80:80
    environment:
      API_MESSAGES_BASE_URL: http://api-messages
```

Run the services using `docker-compose`
```shell
docker-compose up -d
```
