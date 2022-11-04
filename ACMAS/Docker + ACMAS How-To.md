# Deployment instructions for ACMAS @ RCOS v2 (Django, Docker, Postgres, Gunicorn, Nginx)

---
_Note: [Docker](https://docs.docker.com/get-docker/) is a pre-requisite installation to run ACMAS in a development 
environment.
It is __highly__ recommended to use [Docker Desktop](https://www.docker.com/products/docker-desktop/) instead of
 Docker CLI. If you do not have Docker installed, please do so before continuing to the remainder of the instructions._

## Setup
### Using the Docker containers
Each time you make changes to the code you will need to turn off the Docker container and then turn it back on.
 Make sure to turn off the container when you are done working. Some changes to the database structure may require
 manual deletion of docker "volumes" associated with ACMAS.
### Start Docker
In order to run Docker applications you must open __Docker Desktop__ or start the Docker service on your device.
### Navigate to "/ACMAS-Frontend/ACMAS"
Open the repository directory `ACMAS-Frontend` and navigate to the `ACMAS` directory within. Open this `ACMAS`
 directory in the command-line or terminal.

---
### Turn on the Docker containers when you want to start working
`docker-compose -f docker-compose.prod.yml up -d --build`
### Turn off the Docker containers when you are done working
`docker-compose -f docker-compose.prod.yml down -v`

---
## Using ACMAS with Docker
___After turning on the Docker container follow these steps:___
### Ensure that the Docker application was successfully built and is running
- Successful builds will return no errors (red)
- One of the following messages will appear in your command prompt

  ```shell
  Running 3/3
  - Container acmas-db-1      Started
  - Container acmas-web-1     Started
  - Container acmas-nginx-1   Started
  ```
  
- Ensure that the application's containers in Docker Desktop all appear as __green__
- Navigate to `localhost:1337` in any web browser
  - If this does not work, default to using `127.0.0.1:1337`
---

## Resolving issues with Docker and/or ACMAS
1) Check for an error message. If one appears, search it on Google or talk to other ACMAS developers on your sub-team
2) If you are unable to find the exact error code on Google, attempt to search for similar or more generic versions
3) Discuss the issue with other ACMAS sub-teams
4) Talk to the project co-leads Jacob @jaw12346 or Susan @susanh
5) __Open an issue!__