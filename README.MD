# Product API and Basic Frontend

## Objective
The objective of this project is to develop a backend API and a basic frontend interface to display product information. The backend will be responsible for handling product data and exposing endpoints to retrieve product information. The frontend will interact with the backend API to display products and provide basic search functionality.

### Technologies
- Backend: Python, Fastapi
- Frontend: HTML, CSS, JavaScript

## Backend Requirements
- Create a RESTful API using a backend framework of choice. 
- Design and implement a simple database schema to store product information, including product name, description, category, and price.
- Implement API endpoints for retrieving product information:
    - GET /api/products: Retrieve a list of all products with their basic details.
    - GET /api/products/{id}: Retrieve detailed information about a specific product.
- Implement basic error handling and appropriate HTTP status codes for API responses.
- Write unit tests to ensure the functionality of the API endpoints.

## Frontend Requirements
- Create a basic web interface using HTML, CSS, and JavaScript (vanilla JavaScript or a lightweight library like jQuery).
- Display a list of products retrieved from the backend API on the main page.
- Implement a simple search functionality to filter products by name or category.
- Create a product detail page that shows the details of a selected product, fetched from the backend API.

## Usage

### Backend
0. Make and actiavte a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
1. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```
3. Access the API documentation at `http://localhost:8000/docs` to test the API endpoints.


## Folder Structure

- main.py: FastAPI app entrypoint.
- crud.py: CRUD operations for interacting with the database.
- models.py: Pydantic models for database schema and request/response payloads.
- routers.py: API routers for handling requests.
- data.json: Sample data for products.
- tests_*: Unit test files for routers, crud, etc.