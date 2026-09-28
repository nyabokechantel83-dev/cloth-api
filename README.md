# Cloth API

A simple RESTful API for managing clothing products.

## Features

- Create a clothing product
- Get all products
- Get a single product
- Update a product
- Delete a product
- Input validation
- Error handling
- Edge case handling

## Technologies

- Python
- Flask
- REST API

## Product Fields

Each product contains:

- id
- name
- price
- category
- stock

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API welcome message |
| GET | /products | Get all products |
| GET | /products/<id> | Get one product |
| POST | /products | Create product |
| PATCH | /products/<id> | Update product |
| DELETE | /products/<id> | Delete product |

## Validation

The API validates:

- Product name must be a non-empty string
- Price must be greater than 0
- Category must be a non-empty string
- Stock must be a non-negative integer
- Product must exist before updating or deleting

## Running the API

Activate the virtual environment:

```bash
source venv/bin/activate# cloth-api
