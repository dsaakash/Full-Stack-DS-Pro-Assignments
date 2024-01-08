# Flask Static Site

## Introduction
This Flask application demonstrates a simple static site with multiple pages. It includes basic navigation between a home page and an about page, serving as an example of how to structure a Flask app with static HTML content.

## Getting Started

### Prerequisites
- Python 3.x
- Flask

You can install Flask via pip:

```bash
pip install Flask
```

### Project Structure

Your project should have the following structure:

```
/your-app
    /static
        /css
        /js
        /images
    /templates
        home.html
        about.html
    app.py
```

### Installation

1. Clone the repository or download the source code.
2. Navigate to the directory containing `app.py`.

### Running the Application

Execute the following command to run the application:

```bash
python app.py
```

The server should start on `http://127.0.0.1:5000/`.

### Viewing the Application

Open a web browser and go to `http://127.0.0.1:5000/` to view the home page. Use the navigation links to switch between the Home and About pages.

## Features

- Basic Flask application setup.
- Static HTML pages for content.
- Simple navigation between multiple pages.

## Customization

You can add more pages by creating new HTML files in the `templates` directory and adding corresponding routes in `app.py`. Static assets like CSS and JavaScript can be added to the `static` folder.

## Contributing

Contributions to improve the application are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.