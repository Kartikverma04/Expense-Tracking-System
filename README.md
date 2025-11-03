# 💰 Expense Tracking System

> A full-stack expense management application with real-time analytics and interactive visualizations

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.119.0-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-red.svg)](https://streamlit.io/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)

## 📸 Screenshots


### Add/Update Expenses
![Add Expense](Screenshot 2025-11-03 204621.png)

### Analytics by Category
![Category Analytics](screenshots/category_analytics.png)

### Monthly Analytics
![Monthly Analytics](screenshots/monthly_analytics.png)

---

## 🎯 Project Overview

The **Expense Tracking System** is a comprehensive web application designed to help individuals manage their personal finances. Built as a beginner-friendly full-stack project, it demonstrates the integration of modern Python technologies including FastAPI for the backend, Streamlit for the frontend, MySQL for data persistence, and Pandas for data analysis.

### 🌟 Key Highlights

- **Real-time Data Visualization** - Interactive bar charts and tables
- **Dual Analytics Views** - Category-wise and month-wise expense analysis
- **Year-based Filtering** - Analyze expenses for any year (2020-2030)
- **RESTful API Architecture** - Clean separation of frontend and backend
- **Responsive UI** - Built with Streamlit's intuitive components

---

## ✨ Features

### 📝 Expense Management
- ✅ Add daily expenses with category, amount, and date
- ✅ Update existing expense records
- ✅ Delete unwanted entries
- ✅ Real-time data validation

### 📊 Analytics Dashboard

#### 1️⃣ **Category-wise Analytics**
Track your spending across different categories:
- 🍔 **Food** - Restaurant bills, groceries, and dining
- 🎬 **Entertainment** - Movies, streaming, and events
- 🛍️ **Shopping** - Retail purchases and online orders
- 📦 **Others** - Miscellaneous expenses

#### 2️⃣ **Monthly Analytics**
- 📅 Select any year from 2020-2030
- 📈 View month-by-month expense breakdown
- 🎨 Interactive bar chart visualization
- 📋 Detailed monthly summary table

### 💾 Data Features
- Persistent MySQL database storage
- Efficient SQL queries with aggregation
- Parameterized queries for security
- Transaction support for data integrity

---

## 🛠️ Tech Stack

| Category | Technology | Version |
|----------|-----------|---------|
| **Frontend** | Streamlit | 1.50.0 |
| **Backend** | FastAPI | 0.119.0 |
| **Database** | MySQL | 8.0+ |
| **Data Processing** | Pandas | 2.3.2 |
| **Validation** | Pydantic | 2.12.3 |
| **Server** | Uvicorn | 0.38.0 |
| **Testing** | Pytest | 8.4.2 |
| **HTTP Client** | Requests | 2.32.4 |
| **Database Connector** | mysql-connector-python | 9.5.0 |

---

## 📦 Installation

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **MySQL Server 8.0+** - [Download MySQL](https://dev.mysql.com/downloads/)
- **pip** - Python package manager (included with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)

### Setup Instructions

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/expense-tracking-system.git
cd expense-tracking-system
```

#### 2️⃣ Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure Database

**Create MySQL Database:**
```sql
CREATE DATABASE expense_tracker;
USE expense_tracker;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    expense_date DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

**Update Database Configuration:**
Create a `config.py` file or update your database connection settings:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'expense_tracker'
}
```

---

## 🚀 Running the Application

### Start Backend Server
```bash
cd backend
python server.py
```
Or using uvicorn directly:
```bash
uvicorn backend.server:app --reload --port 8000
```

The API will be available at: `http://localhost:8000`  
API Documentation: `http://localhost:8000/docs`

### Start Frontend Application
Open a **new terminal** and run:
```bash
cd frontend
streamlit run app.py
```

The application will be available at: `http://localhost:8501`

---

## 📖 Usage Guide

### Adding a New Expense
1. Navigate to the **"Add/Update Expenses"** tab
2. Select a category from the dropdown
3. Enter the expense amount
4. Choose the expense date
5. Add an optional description
6. Click **"Add Expense"** button

### Viewing Category Analytics
1. Go to the **"Analytics by Category"** tab
2. View the pie chart or bar chart showing category distribution
3. See the total spending per category in the table below

### Analyzing Monthly Expenses
1. Navigate to the **"Analytics by Month"** tab
2. Select a year from the dropdown (2020-2030)
3. View the interactive bar chart showing monthly totals
4. Review the detailed monthly breakdown table

---

## 📁 Project Structure

```
expense-management-system/
│
├── frontend/
│   └── app.py             # Streamlit application
│
├── backend/
│   ├── server.py          # FastAPI server
│   ├── db_helper.py       # Database operations
│   └── logging_setup.py   # Logging configuration
│
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```


---

## 🧪 Testing

Run the test suite:
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=backend --cov=frontend
```


---

## 🐛 Known Issues

- None at the moment! 🎉

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---



## 🙏 Acknowledgments

- Built with ❤️ using [Streamlit](https://streamlit.io/)
- API powered by [FastAPI](https://fastapi.tiangolo.com/)
- Data analysis with [Pandas](https://pandas.pydata.org/)
- Database management with [MySQL](https://www.mysql.com/)



Made with 💰 for better financial management

</div>

