# Deployment instructions for ACMAS @ RCOS v2 (Django, Docker, Postgres, Gunicorn, Nginx)
## Production server
_Note: Running migrations and serving static files are now handled in entrypoint.prod.sh. and entrypoint.sh._

[Docker](https://docs.docker.com/get-docker/) is a pre-requisite installation to run the deployment server.
If you do not have Docker installed, please do so before continuing to the remainder of the instructions.
### Build images and spin up production containers
`docker-compose -f docker-compose.prod.yml up -d --build`
### Bring the containers down once done
`docker-compose -f docker-compose.prod.yml down -v`

---
## Development server
_Note: [Docker](https://docs.docker.com/get-docker/) is a pre-requisite installation to run the development server.
It is __highly__ recommended to use [Docker Desktop](https://www.docker.com/products/docker-desktop/) instead of Docker CLI.
If you do not have Docker installed, please do so before continuing to the remainder of the instructions._
### Build images and spin up development containers
`docker-compose -f docker-compose.yml up -d --build`
### Bring down development containers and associated volumes
`docker-compose down -v`