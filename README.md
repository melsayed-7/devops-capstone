[![CircleCI](https://circleci.com/gh/mdominovic/aws_devops_capstone.svg?style=svg)](https://circleci.com/gh/mdominovic/aws_devops_capstone)

# Udacity AWS Cloud DevOps nano degree capstone project
Capstone project of Udacity AWS DevOps nanodegree

## Setup CircleCI environment variables
Couple environment variables are needed for authentication on different services, so one solution for safe storing credentials is to use CircleCI's environment variables which could be used very easily in pipeline.

| Variables  |
| ------------- |
| AWS_ACCESS_KEY_ID  |
| AWS_SECRET_ACCESS_KEY  |
| AWS_DEFAULT_REGION  |
| DOCKER_USERNAME  |
| DOCKER_PWD  |

## Project description
What is covered in this project:
 * Python code and Docker file is linted
 * Docker image containing flask web application is built, tested and pushed to Docker Hub
 * EKS cluster is created if it doesn't exist already
 * Deployment is created and/or updated with rolling update strategy
 * At the end cluster is deleted if no longer needed
