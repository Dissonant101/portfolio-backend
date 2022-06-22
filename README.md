# DynamicResumes API Docs

An API for the assets of resumes used in DynamicResumes.

## Details

API hosted on an AWS EC2 instance. The Flask server is invoked by Gunicorn and reverse-proxied by NGINX.

## Endpoints

### Resume

- URL

  http://ec2-3-17-146-230.us-east-2.compute.amazonaws.com/api/resume/{RESUME_NAME}

- Method

  GET

### Stylesheet

- URL

  http://ec2-3-17-146-230.us-east-2.compute.amazonaws.com/api/resume/{STYLESHEET_NAME}

- Method

  GET

### Layout

- URL

  http://ec2-3-17-146-230.us-east-2.compute.amazonaws.com/api/resume/{LAYOUT_NAME}

- Method

  GET
