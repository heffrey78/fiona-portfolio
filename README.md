# Fiona's Portfolio

This is a Flask-based portfolio website showcasing Fiona's work and skills as a software developer.

## Features

- Responsive design using the Laura template
- Home page with an introduction and featured projects
- About page with personal information and skills
- Portfolio page showcasing various projects
- Personal work page for side projects and experiments
- Contact form for getting in touch
- Google App Engine ready for deployment

## Requirements

- Python 3.9+
- Flask and other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fiona-portfolio.git
   cd fiona-portfolio
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application locally:

```
python app.py
```

The application will be available at `http://localhost:5000`.

## Running Tests

To run the test suite:

```
python -m unittest discover tests
```

## Deployment

This application is configured for deployment to Google App Engine. To deploy:

1. Make sure you have the Google Cloud SDK installed and configured.
2. Run the following command:
   ```
   gcloud app deploy
   ```

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please reach out through the contact form on the website or email at fiona@example.com.