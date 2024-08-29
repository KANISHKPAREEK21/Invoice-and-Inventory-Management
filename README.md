# Invoice-and-Inventory-Management
![Project Screenshot](link-to-screenshot)
The screenshots of other pages are here[] 

## Table of Contents

1. [About the Project](#about-the-project)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)


## Overview

This Django-based Inventory and Billing Management System is designed to help businesses efficiently handle their invoicing, customer management, product tracking, expenses, and payment processing. The system provides a user-friendly interface for creating, viewing, and managing invoices, along with comprehensive tools for managing customers, products, expenses, and payments.

## Features

- **User Authentication**: Secure login and logout functionalities to ensure authorized access.
- **Invoice Management**:
  - Create invoices by selecting customers and products from dropdown menus.
  - Auto-population of customer contact details and product costs.
  - Options to modify prices, select units, and add invoice details such as comments, GST, and taxes.
- **Invoice Viewing**:
  - Search invoices by invoice number.
  - Filter invoices by customer or date.
  - Download invoices individually or by date range.
- **Customer, Product, and Expense Management**:
  - Create, view, edit, and delete customers, products, and expenses.
- **Payment Management**:
  - Record payments received from customers, specifying bank and payment amount.
  - View payment history with filtering options by date or bank.

## Technologies Used

- **Django**: Web framework for building the backend.
- **SQLite**: Database for storing data.
- **Bootstrap**: Frontend framework for responsive design.
- **Jinja2**: Templating engine for dynamic HTML pages.
- **Styling**: SCCS and CSS


## Installation

To get started with the Inventory and Billing Management System, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KANISHKPAREEK21/Invoice-and-Inventory-Management.git
   cd Invoice-and-Inventory-Management
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv env
   ```

3. **Activate the virtual environment**:  
   - **Windows**:  
     ```bash
     .\env\Scripts\activate
     ```
   - **MacOS/Linux**:  
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (to access the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   Open a web browser and navigate to `http://127.0.0.1:8000/` to start using the system.

## Usage

- **Login** with your credentials to access the system.
- **Create Invoices** on the home page by selecting customers and products, and entering necessary details.
- **View Invoices** by navigating to the "View Invoice" section, where you can search and filter invoices.
- **Manage Customers, Products, and Expenses** by using the respective management pages to add, edit, or delete entries.
- **Record Payments** in the "Payment" section by specifying the bank and amount received, and view payment history as needed.

## Contributing

Contributions are welcome! To contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bugfix (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

Thank you to all contributors and supporters of this project. Your feedback and contributions help make this system better!