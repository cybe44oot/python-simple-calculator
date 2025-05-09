# 🧮 Jenkins-Pipeline-Calculator

A basic command-line calculator written in Python that performs simple arithmetic operations — addition, subtraction, multiplication, and division.

This project is CI-integrated using **Jenkins** to demonstrate automated testing and deployment pipelines for Python applications.

---

## 📦 Features

- Simple command-line interface
- Basic arithmetic operations: `+`, `-`, `*`, `/`
- Modular code design
- Unit tests included
- Jenkinsfile for CI/CD pipeline

---

## 🛠️ Requirements

- Python 3.6+
- `pip` (Python package manager)

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/cybe44oot/python-simple-calculator.git
cd python-simple-calculator

---

##
Run The calculater

python calculator.py


🧪 Running Tests
This project uses unittest for testing.

To run tests manually

python -m unittest test_calculator.py




## ⚙️ Jenkins Integration
This project includes a Jenkinsfile for automating:

Installing dependencies

Running unit tests

Reporting build status

Steps to test in Jenkins:

Install Jenkins (locally or on a server)

Create a new pipeline job

Point it to this GitHub repo

Jenkins will automatically detect the Jenkinsfile and execute the pipeline



## 📂 File Structure
bash
Copy
Edit
.
├── calculator.py         # Main calculator logic
├── test_calculator.py    # Unit tests
└── Jenkinsfile           # Jenkins pipeline config



🙌 Author
Made with ❤️ by cybe44oot


