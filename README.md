
# 📱 Mobile Store Inventory with Django

![Django](https://img.shields.io/badge/Django-3.2.7-green.svg) ![Python](https://img.shields.io/badge/Python-3.11-blue.svg) ![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)

## 🚀 Overview

This is a Django-based inventory management system for a mobile store. It allows store owners to manage their mobile products, including adding new items, updating product information, and removing items from the inventory. This project is ideal for small mobile stores to keep track of their stock and manage products efficiently.

## 🛠 Features

- 📦 **Manage Product Inventory**: Add, update, and delete mobile products.
- 🔍 **Search Functionality**: Quickly find products in the inventory.
- 📊 **Dashboard**: Visual representation of the inventory with product counts.
- 🔐 **Authentication**: Secure login for store managers.
- 🗃️ **Database**: Uses SQLite for simple and fast database operations.

## 📂 Project Structure

```
Mobile-store-Django/
├── inventory/           # Application files for managing products
│   ├── migrations/      # Database migrations
│   ├── static/          # Static files (CSS, JS, Images)
│   ├── templates/       # HTML templates for the app
│   ├── admin.py         # Django admin configurations
│   ├── apps.py          # Application configuration
│   ├── models.py        # Database models for products
│   ├── urls.py          # URL routing for the app
│   └── views.py         # Views for handling requests
├── venv/                # Virtual environment for the project
├── .env                 # Environment variables
├── .gitignore           # Git ignore file
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
├── entrypoint.sh        # Entrypoint script for Docker
├── manage.py            # Django's command-line utility
├── mobile.db            # SQLite database file
└── requirements.txt     # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2.7
- SQLite

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Mobile-store-Django.git
    cd Mobile-store-Django
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the application:

    ```bash
    python manage.py runserver
    ```

7. Access the application:

   - Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).
   - Access the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

## 🐳 Docker Deployment

1. Build the Docker image:

    ```bash
    docker build -t mobile-store-django .
    ```

2. Run the Docker container:

    ```bash
    docker-compose up -d
    ```

3. Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 💬 Contact

- **Author**: Kian Anbarestani
- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub**: [KianAnbarestani](https://github.com/KianAnbarestani)

Feel free to open an issue if you find a bug or have suggestions for improvements!
