# ML - Delivery

## Description

This project is an API built with FastAPI that performs authentication operations, data handling, and web scraping of production, processing, commercialization, import, and export data for products.

## Project Structure

- **auth.py**: Contains functions for creating and decoding JWT tokens.
- **database.py**: SQLite database configuration.
- **datacess.py**: Functions for web scraping production, processing, commercialization, import, and export data.
- **entities.py**: Pydantic and SQLAlchemy data models.
- **models.py**: Pydantic data models for users and tokens.
- **utils.py**: Utility functions for password hashing and verification.
- **main.py**: Main FastAPI configuration and API endpoints.

## Requirements

- Python 3.9+
- FastAPI
- SQLAlchemy
- Pydantic
- Pandas
- Passlib
- python-jose

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Set the secret key for JWT in `auth.py`:

    ```python
    SECRET_KEY = "your-secret-key"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    ```

2. Set the database URL in `database.py`:

    ```python
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
    ```

## Running

1. Start the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints

### Authentication

- **POST /token**: Generates an access token for authentication.
  - Request: `username` and `password`
  - Response: `access_token` and `token_type`

### Users

- **POST /users/**: Creates a new user.
  - Request: `username`, `email`, `password`
  - Response: Details of the created user

- **GET /users/me**: Returns details of the authenticated user.
  - Response: User details

### Production Data

- **GET /producao/{year}**: Returns production data for the specified year.
  - Request: `year`
  - Response: List of production records

### Processing Data

- **GET /processamento/{year}/{subopt}**: Returns processing data for the specified year and sub-option.
  - Request: `year`, `subopt`
  - Response: List of processing records

### Commercialization Data

- **GET /comercializacao/{year}**: Returns commercialization data for the specified year.
  - Request: `year`
  - Response: List of commercialization records

### Import Data

- **GET /importacao/{year}/{subopt}**: Returns import data for the specified year and sub-option.
  - Request: `year`, `subopt`
  - Response: List of import records

### Export Data

- **GET /exportacao/{year}/{subopt}**: Returns export data for the specified year and sub-option.
  - Request: `year`, `subopt`
  - Response: List of export records

### Authentication Usage

1. Obtain an access token:

    ```bash
    curl -X POST "http://127.0.0.1:8000/token" -d "username=your-username&password=your-password"
    ```

2. Use the token to access protected endpoints:

    ```bash
    curl -H "Authorization: Bearer your-token" "http://127.0.0.1:8000/users/me"
    ```

### Accessing Production Data

1. Access production data for a given year:

    ```bash
    curl "http://127.0.0.1:8000/producao/2023"
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
