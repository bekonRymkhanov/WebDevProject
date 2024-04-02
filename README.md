# Newspaper Web App

Welcome to the Newspaper Web App! This is a simple web application developed by Alikhan Kassiman and Rymkhanov Bekarys.The application will contain the news and articles.

## Features

- Each article includes a title, content, and author information.
- Responsive design for various screen sizes.

## Technologies Used

- HTML
- CSS
- Angular
- Python
- Django

## Setup Instructions

1. Clone this repository to your local machine.
2. Install Angular CLI if you haven't already: `npm install -g @angular/cli`.
3. Navigate to the `frontend` directory and run `npm install` to install dependencies.
4. Run `ng serve` to start the Angular development server.
5. Navigate to the `backend` directory and create a virtual environment: `python -m venv env`.
6. Activate the virtual environment:
    - On Windows: `env\Scripts\activate`
    - On macOS and Linux: `source env/bin/activate`
7. Install Django and other dependencies: `pip install -r requirements.txt`.
8. Run Django migrations: `python manage.py migrate`.
9. Run the Django development server: `python manage.py runserver`.

## API Endpoints

- `/api/articles/`: GET - Retrieve all articles.

## Developers

- Alikhan Kassiman
- Rymkhanov Bekarys

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.