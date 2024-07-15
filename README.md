# RESTapi

This project is a REST API application built with Django and Django REST framework. The application models two main entities: Company and Employee. It provides endpoints to perform CRUD operations on these entities.

Endpoints
GET /companies/: List all companies.<br />
POST /companies/: Create a new company.<br />
GET /companies/{id}/: Retrieve a company by ID.
PUT /companies/{id}/: Update a company by ID.
DELETE /companies/{id}/: Delete a company by ID.
GET /companies/{id}/employees/: List all employees for a specific company.
GET /employees/: List all employees.
POST /employees/: Create a new employee.
GET /employees/{id}/: Retrieve an employee by ID.
PUT /employees/{id}/: Update an employee by ID.
DELETE /employees/{id}/: Delete an employee by ID.

Usage
Once the server is running, you can access the API at http://127.0.0.1:8000/. You can use tools like Postman or cURL to interact with the API.
