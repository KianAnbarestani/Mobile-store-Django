# Mobile Store Inventory Management Project

## Overview

The Mobile Store Inventory Management project is a web application developed using Django, a high-level Python web framework. This application serves as an inventory management system for mobile phones, allowing users to add, update, delete, and search for mobile phones and brands. The project utilizes a responsive design to ensure usability across various devices, including desktops, tablets, and smartphones.

## Project Functionality

### How the Project Works

This application provides the following functionalities:
1. **Brand Management**: Users can add, update, and delete brands. Each brand includes a name and nationality.
2. **Phone Management**: Users can add, update, and delete phones. Each phone is associated with a brand and includes details such as model, price, color, screen size, status, manufacturer country, and quantity.
3. **Search and Filter**: Users can search and filter phones based on various criteria such as brand, nationality, manufacturing country, color, screen size, and price range. A dynamic filter system allows users to apply multiple filters simultaneously.
4. **Responsive Design**: The application is designed to be responsive, ensuring a seamless user experience across all devices.

### What Has Been Done

1. **Model Definition**:
   - Defined `Brand` and `Phone` models with appropriate fields.
   - Implemented validation to ensure unique brand names and phone models.
2. **Form Handling**:
   - Created forms for adding and updating brands and phones.
   - Added custom validation in forms to prevent negative values for price, quantity, and screen size.
3. **Views**:
   - Implemented views for listing, adding, updating, and deleting brands and phones.
   - Developed a comprehensive search and filter functionality in the `phone_list` view.
4. **Templates**:
   - Designed responsive templates using Bootstrap for a clean and professional look.
   - Added a dynamic filter system in the `phone_list` template.
5. **Custom Template Tags**:
   - Created custom template tags to differentiate between brands and phones in the delete confirmation template.
6. **Responsive Design**:
   - Ensured the project is responsive by using Bootstrap's grid system and responsive classes.

## How to Set Up the Project

### Prerequisites

1. **Python 3.x**: Version 3.6 or higher is recommended.
2. **Django**: Version 3.2.10

### Installation

1. Clone the project repository:
   ```bash
   git clone <repository-url>
   cd mobile_store


## 🚀 Deployment

### Local Deployment

1. Ensure all dependencies are installed by running:

    ```bash
    pip install -r requirements.txt
    ```

2. Start the FastAPI server locally:

    ```bash
    uvicorn main:app --reload
    ```

3. Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Docker Deployment

1. Build the Docker image:

    ```bash
    docker build -t todo-list-fastapi .
    ```

2. Run the Docker container:

    ```bash
    docker run -d --name todo-list -p 8000:8000 todo-list-fastapi
    ```

3. Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Deployment on Heroku

1. Create a `Procfile` in the root directory with the following content:

    ```
    web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-8000}
    ```

2. Login to Heroku:

    ```bash
    heroku login
    ```

3. Create a new Heroku app:

    ```bash
    heroku create todo-list-fastapi
    ```

4. Push the code to Heroku:

    ```bash
    git push heroku main
    ```

5. Access the application at your Heroku app URL.

