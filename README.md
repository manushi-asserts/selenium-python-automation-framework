# Selenium Python Automation Framework

## 📌 Overview
This repository contains a scalable and maintainable test automation framework
built using **Selenium WebDriver with Python**.  
The framework follows **Page Object Model (POM)** design principles and is
designed to support real-world web application testing.

---

## 🛠 Tech Stack
- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- GitHub Actions (CI/CD)
- YAML / Config-driven execution

---

## 🏗 Framework Design
- Page Object Model for better readability and maintenance
- Explicit waits for stable test execution
- Reusable utilities and base classes
- Config-based environment and browser selection
- Screenshot capture on test failure

---

## 📁 Project Structure

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


---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Google Chrome / Firefox
- pip

### Installation
```bash
pip install -r requirements.txt

Run Tests
pytest -m smoke

🔁 CI/CD

This project uses GitHub Actions to automatically execute tests on every
push to the repository.

📌 Sample Application

Tests are written against publicly available demo applications for learning
and demonstration purposes.

📈 Future Enhancements

Parallel execution

Docker support

Advanced reporting (Allure)

👩‍💻 Author

Manushi
Automation Test Engineer | Selenium + Python

API + UI hybrid framework

