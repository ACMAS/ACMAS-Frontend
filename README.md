# ACMAS-Frontend

[![Lint Code Base](https://github.com/ACMAS/ACMAS-Frontend/actions/workflows/super-linter.yml/badge.svg)](https://github.com/ACMAS/ACMAS-Frontend/actions/workflows/super-linter.yml)  [![Django CI](https://github.com/ACMAS/ACMAS-Frontend/actions/workflows/django.yml/badge.svg)](https://github.com/ACMAS/ACMAS-Frontend/actions/workflows/django.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c4e7f48ee49a4504bc2a4cdef806dfa8)](https://www.codacy.com/gh/ACMAS/ACMAS-Frontend/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ACMAS/ACMAS-Frontend&amp;utm_campaign=Badge_Grade)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/L4L4GMYID)

## Usage

---
_Note: [Docker](https://docs.docker.com/get-docker/) is a pre-requisite installation to run ACMAS in a development
 environment.
It is __highly__ recommended to use [Docker Desktop](https://www.docker.com/products/docker-desktop/) instead of
 Docker CLI. If you do not have Docker installed, please do so before continuing to the remainder of the instructions._

### Setup
#### Using the Docker containers
Each time you make changes to the code you will need to turn off the Docker container and then turn it back on.
 Make sure to turn off the container when you are done working. Some changes to the database structure may require
 manual deletion of docker "volumes" associated with ACMAS.
#### Start Docker
In order to run Docker applications you must open __Docker Desktop__ or start the Docker service on your device.
#### Navigate to "/ACMAS-Frontend/ACMAS"
Open the repository directory `ACMAS-Frontend` and navigate to the `ACMAS` directory within. Open this `ACMAS`
 directory in the command-line or terminal.

---
#### __Turn on the Docker containers when you want to start working__
`docker-compose up -d --build`
#### __Turn off the Docker containers when you are done working__
If you want to shut down normally: `docker-compose down`

If you want to flush your database and project files: `docker-compose down -v`

---
### Using ACMAS with Docker
___After turning on the Docker container follow these steps:___
#### Ensure that the Docker application was successfully built and is running
- Successful builds will return no errors (red)

- One of the following messages will appear in your command prompt

  - __Note:__ If you do not flush, only the affected containers will appear

  ```shell
  Running 3/3
  - Container acmas-db-1      Started
  - Container acmas-web-1     Started
  - Container acmas-nginx-1   Started
  ```

- Ensure that the application's containers in Docker Desktop all appear as __green__

- Navigate to `localhost:80` in any web browser
  - If this does not work, default to using `127.0.0.1:80`
---

### Resolving issues with Docker and/or ACMAS
1) Check for an error message. If one appears, search it on Google or talk to other ACMAS developers on your sub-team
2) If you are unable to find the exact error code on Google, attempt to search for similar or more generic versions
3) Discuss the issue with other ACMAS sub-teams
4) Talk to the project co-leads Jacob @jaw12346 or Susan @susanh
5) __Open an issue!__

---

## Executive Summary

  ACMAS, or Automatic Course Material Archiving System is a free to use database site for anyone to both upload and view documents, materials, coursework, etc. for various courses and questions from any school/institute.
On the internet today, there are many services that allow students to help each other with homework from various courses all over the world. However, those services are not free to access, which can make it difficult for everyone to use. ACMAS is a free to use database available for anyone to upload, and view backtests from their specific college’s courses, which can be very helpful for test preparation.

## Features

  There are many features that ACMAS will contain to make accessing content and using the database as simple and straightforward as possible. First, ACMAS will be able to support uploading problems as photos/PDFs/scanned in documents.
In addition to this, there will also be the ability to search for problems by a specific school and course, or by specific question, or by image, which would all allow the user to then find the backtests and back work that they are looking for and use them for their own studying.
There also will be links from questions on a backtests to alternative answers to the same question from other sources.
