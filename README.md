# Selenium Python Automation Framework

## 📌 Overview

This repository contains a scalable, maintainable, and production-ready test automation framework built using **Selenium WebDriver with Python and Pytest**.
The framework follows **Page Object Model (POM)** design principles and supports real-world testing scenarios including parallel execution, multi-browser testing, reporting, and environment configuration.

---

## 🛠 Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* HTML Reports
* Logging System
* GitHub Actions (CI/CD)
* YAML / Config-driven execution

---

## 🚀 Key Features

* Parallel test execution using pytest-xdist
* Cross-browser testing (Chrome, Firefox, Edge)
* Environment switching (QA / Stage / Prod)
* Screenshot capture on test failure
* HTML test reports with embedded screenshots
* Centralized logging system
* Modular and reusable framework architecture
* CLI-based execution configuration

---

## 🏗 Framework Design

* Page Object Model for maintainable test design
* Explicit waits for stable execution
* Reusable utilities and fixtures
* Config-driven browser and environment setup
* Failure debugging support (logs + screenshots)

---

## 📁 Project Structure

```
selenium-python-automation-framework/
│
├── config/
├── pages/
├── tests/
├── utils/
├── drivers/
├── reports/
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* Chrome / Firefox / Edge
* pip

### Installation

```
pip install -r requirements.txt
```

### Run Tests

```
pytest
```

Run smoke tests:

```
pytest -m smoke
```

Run specific browser:

```
pytest --browser firefox
```

Run specific environment:

```
pytest --env stage
```

---

## 🔁 CI/CD

This framework integrates with **GitHub Actions** to automatically execute tests on every push.

---

## 📌 Sample Application

Tests are written against publicly available demo applications for demonstration and learning purposes.

---

## 📈 Future Enhancements

* Docker execution support
* Allure reporting integration
* Cloud execution (BrowserStack / Selenium Grid)

---

## 👩‍💻 Author

**Manushi**
Automation Test Engineer | Selenium + Python

---

### ⭐ Project Summary

A scalable and production-ready Selenium automation framework supporting parallel execution, cross-browser testing, environment configuration, reporting, and reusable architecture.
