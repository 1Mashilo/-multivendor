# Multivendor Django Backend

Welcome to the backend of the Multivendor Django project. This backend supports a digital marketplace with multivendor capabilities, providing features for product management, sales analytics, user registration, and more.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

### Product Management

- Create, edit, and delete products.
- Associate products with sellers.
- Showcase product details, including name, price, and image.

### Sales Analytics

- Track total sales amount and quantity.
- View sales statistics on a daily, monthly, and yearly basis.
- Analyze product-specific sales.

### User Registration and Authentication

- Allow users to register for vendor accounts.
- Authenticate users for secure transactions.
- Provide a dashboard for vendors to manage their products.

### Checkout Process with Stripe

- Enable a secure checkout process using the Stripe API.
- Handle payment methods with support for card payments.

### Modern Design and Responsiveness

- Utilize a modern and responsive design for a seamless user experience.
- Implement features to complement a digital marketplace.

## Prerequisites

Ensure the following prerequisites are met before setting up the project:

- Python 3.x
- Django
- Stripe API keys

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/1mashilo/multivendor.git
   
2. **Navigate to the Project Directory:**

   ```bash
   cd multivendor

3. **Create a Virtual Environment (Optional, but recommended):**
   
    ```bash
    Create a virtual environment
    python -m venv venv
    Activate the virtual environment
    On Windows
    venv\Scripts\activate
    On macOS/Linux
    source venv/bin/activate
    
4. **Install Project Dependencies:**
 
     ```bash
     pip install -r requirements.txt

5. **Configure the Database:**
   
     ```bash
     python manage.py migrate
     
6. **Run the Server:**
   
    ```bash
    python manage.py runserver

7. **Access the Application:**

   
    ```bash
   Open a web browser and go to http://127.0.0.1:8000/ to access the application.
    Note: Make sure to configure the Stripe API keys in your settings before using the checkout process.

## Contributing

Contributions are welcome! Feel free to open an issue or create a pull request.

## License  
This project is licensed under the MIT License. Enjoy building your multivendor digital marketplace!
   
