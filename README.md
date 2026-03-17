# DemoProject_Python_Playwright_Concepts
A demo project to demonstrate **Playwright with Python** along with **Page Object Model (POM)** basics.
This repository contains simple tests built using Playwright with Python to explain key concepts like POM, test structure, usage of locators, helpers/utils, and environment configurations.

---

## 🧠 What You'll Learn
- How to structure Playwright tests in Python using **Page Object Model (POM)**.
- How to write basic browser automation tests.
- Using helpers and utilities for reusable code.
- Running tests across different environments (via simple `.env` setups).

---

## 🚀 Features
✔ Basic test examples  
✔ Page Object Model structure  
✔ Environment configs (`.env.dev`, `.env.QAEnv`, `.env.preprod`, etc.)  
✔ Utilities & test data segregation  
✔ Screenshot & report captures for visual debugging  
✔ Covers alerts, file upload/download, keyboard/mouse events, API testing, and more  

---

## 📁 Project Structure

```
DemoProject_Python_Playwright_concepts/
│
├── assets/                            # Static assets used in tests (e.g. files for upload)
├── pages/                             # Page Object Model (POM) classes
├── reports/                           # Generated test reports
├── screenshots/                       # Captured screenshots during test runs
├── testData/                          # Test data files (JSON, CSV, XLSX, etc.)
├── tests/                             # Test cases
│   ├── test_alert_options.py          # JS alert handling tests
│   ├── test_api_product.py            # API testing examples
│   ├── test_data_results_from_CL.py   # Data-driven tests via command line args
│   ├── test_data_results_from_csv.py  # Data-driven tests from CSV
│   ├── test_data_results_from_json.py # Data-driven tests from JSON
│   ├── test_data_results_from_pydantic.py  # Data validation with Pydantic
│   ├── test_data_results_from_xlsx.py # Data-driven tests from Excel
│   ├── test_datePicker_events.py      # Date picker interaction tests
│   ├── test_file_upload_download_events.py  # File upload/download tests
│   ├── test_keyBoardEvents.py         # Keyboard event tests
│   ├── test_lambda_execution.py       # Lambda/cloud execution tests
│   ├── test_login.py                  # Login flow tests
│   ├── test_mouseEvents.py            # Mouse event tests
│   ├── test_productCheckOut.py        # Product checkout flow tests
│   └── test_usingMultipleCreds.py     # Multi-credential tests
├── utils/                             # Helper utilities and reusable functions
├── .env.dev                           # Dev environment settings
├── .env.preprod                       # Pre-production environment settings
├── .env.QAEnv                         # QA environment settings
├── requirements.txt                   # Python dependencies
├── pytest.ini                         # Pytest configuration
├── conftest.py                        # Pytest fixtures
└── README.md                          # Project documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/DemoProject_Python_Playwright_concepts.git
   cd DemoProject_Python_Playwright_concepts
   ```

2. **Create and activate a virtual environment** *(recommended)*
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

5. **Set up your environment file**  
   Copy one of the provided `.env` files or create your own:
   ```bash
   cp .env.dev .env
   ```
   Update the values inside as needed (base URL, credentials, etc.).

---

## ▶️ How to Run Tests

### Run all tests
```bash
pytest
```

### Run a specific test file
```bash
pytest tests/test_login.py
```

### Run tests by marker
```bash
pytest -m alert
pytest -m login
```

### Run tests with a specific environment
```bash
pytest --env=QAEnv
pytest --env=dev
pytest --env=preprod
```

### Run tests with visible browser (headed mode)
```bash
pytest --headed
```

### Run tests and generate an HTML report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run a specific test by name
```bash
pytest -k "test_login"
```

---

## 📝 Notes
- Screenshots are automatically saved to the `screenshots/` folder on test failure.
- Test reports are saved to the `reports/` folder.
- Environment variables (base URLs, credentials, etc.) are loaded from the active `.env` file via `conftest.py`.
- Test data files (CSV, JSON, XLSX) live in `testData/` and are referenced directly in tests.
- Make sure to update the username and password for your amazon accounts while running the login scenarios.
