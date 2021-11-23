# Deploy a Fargate API with AWS Copilot

_Presented as part of the Coffee & Cloud Series_

Let's connect: https://linktr.ee/fortejas

## Objective

In this lab we will deploy an API to AWS Fargate using the AWS CoPilot CLI. We will use the FastAPI framework to build the API in Python.

## Requirements

- Git Installed
- Python 3 Installed
- Docker Installed
- AWS Account
- AWS CLI Installed and Configured
- CoPilot Installed (we use v1.12.0 here)

## Expected Time

You should be able to deploy this in about 60mins.

## Getting Started

### Creating the API

First we'll need the actual code for the application we're going to deploy. For this example we'll create a Python 3 virtual environment to be able to install python dependencies without affecting globally installed packages.

```bash
$ pip install fastapi "uvicorn[standard]"
```
