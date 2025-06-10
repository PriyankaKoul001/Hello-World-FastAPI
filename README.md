
---

```markdown
# 🚀 FastAPI Hello World App

This is a simple FastAPI application that returns a "Hello, World!" message along with an additional route displaying the owner's name.

---

## 📂 Project Structure

├── main.py
├── requirements.txt
└── README.md
└── render.yaml

````

---

## 🖥️ Endpoints

| Method | Endpoint     | Description                        |
|--------|--------------|------------------------------------|
| GET    | `/`          | Returns a simple Hello World text  |
| GET    | `/owner`     | Returns the name of the maintainer |

---

## 💡 Sample Responses

### `GET /`
```json
"Hello, World!"
````

### `GET /owner`

```json
"Build and Maintained by Priyanka Koul!!!"
```

---

## 🚀 Run Locally

### 📦 1. Install dependencies

```bash
pip install fastapi uvicorn
```

### ▶️ 2. Run the server

```bash
uvicorn main:app --reload
```

Visit:

* Root: [http://localhost:8000/](http://localhost:8000/)
* Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠️ Built With

* [FastAPI](https://fastapi.tiangolo.com/) - The modern web framework for building APIs with Python
* [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server

---

## 👩‍💻 Maintainer

**Priyanka Koul**
*“CSE Student from AIT PUNE”*

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

