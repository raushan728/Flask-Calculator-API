# Flask Calculator API

A simple RESTful API built with Flask to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

---

## 📌 Features

- Add, subtract, multiply, and divide two numbers
- Handles input validation and error responses
- Returns result in JSON format
- Lightweight and beginner-friendly

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/raushan728/Flask-Calculator-API.git
cd Flask-Calculator-API
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run the Flask App
```
python app.py
```
App will start on: http://127.0.0.1:5000/

---

## 📮 API Endpoint
**POST /calculate**🔸 Request (JSON)
```
{
  "num1": 10,
  "num2": 5,
  "operation": "add"
}
```


