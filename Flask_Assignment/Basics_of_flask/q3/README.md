# Dynamic Flask App

## Introduction
This is a Flask web application that demonstrates the use of URL parameters to display dynamic content. The application includes routes for user profiles and posts, each accepting parameters to display specific data.

## Getting Started

### Prerequisites
- Python 3.x
- Flask

To install Flask, run the following command:

```bash
pip install Flask
```

### Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory where `app.py` is located.

### Running the Application

Run the application with the following command:

```bash
python app.py
```

This will start a development server on `http://127.0.0.1:5000/`.

### Using the Application

Access the application through a web browser with the following URL patterns:

- **User Profile**: `http://127.0.0.1:5000/user/<username>`
- **Post**: `http://127.0.0.1:5000/post/<post_id>`

Replace `<username>` with any username and `<post_id>` with any integer to test the dynamic content display.

## Features

- Displays user profiles and posts using dynamic URL parameters.
- Simple and illustrative example of Flask routing and parameter handling.

## Customization

You can expand this application by:

- Adding more routes with different types of URL parameters.
- Connecting to a database to fetch real data based on the parameters.
- Integrating HTML templates to render more complex web pages.

## Contributing

If you have suggestions for improving the app, please feel free to fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

