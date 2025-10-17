# automationExercies

Automation Testing Framework for **automationexercise.com**, built with Python and Pytest.  
Supports both UI (Selenium) and API (Requests) test cases. Incorporates Page Object Model, data-driven tests, parallel execution, and reporting (Allure/HTML).  

---

## Table of Contents

- Features
- Prerequisites
- Installation
- Project Structure
- Configuration

---

## Features

- UI automation using **Selenium WebDriver**  
- API testing using **Requests**  
- Page Object Model (POM) design  
- Data-driven tests (JSON, CSV, Excel)  
- Parallel test execution  
- Rich test reports (Allure, HTML)  
- Shell scripts / automation helpers  

---

## Prerequisites

- Python 3.x  
- pip  
- Browser drivers (e.g., chromedriver, geckodriver) in your PATH  
- (Optional) Allure CLI, if you want to generate Allure reports  

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/PrasadHelaskar/automationExercies.git
cd automationExercies
```

2. Create a virtual environment (recommended):
Run the following command in your project directory:

```bash
python3 -m venv venv
```

3. Install Dependencies
Once your virtual environment is activated, install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Project Structure

automationExercies/ </br> 
├── .github/ workflows/ # GitHub Actions CI/CD workflows </br> 
├── apiScripts/ # API test cases, helper modules </br> 
├── seleniumScripts/ # UI automation / page objects / tests </br> 
├── shellFiles/ # Shell scripts for setup, execution </br> 
├── requirements.txt # Python dependencies </br> 
└── README.md # Project documentation (this file) </br>

 ## Configuration

Store project-specific settings in a configuration file (e.g., `config.json`) or a `.env` file. Typical configuration options include:

- `BASE_URL` – The base URL of the application under test.  
- `API_TOKEN` / credentials – Authentication details for API or services.  
- `DEFAULT_TIMEOUT` – Default timeout for requests or UI waits.  
- Browser settings – Options like headless mode, window size, etc.

