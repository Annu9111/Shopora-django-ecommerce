# 🛍️ Shopora – Django E-commerce Website

Shopora is a full-stack e-commerce web application built using Django. It allows users to browse products, add items to cart, manage orders, and more.

---

## 📸 Preview

![Shopora Screenshot](screenshot.png)

---

## 🚀 Features

* 🏠 Home page with categorized products
* 🔍 Search functionality
* 🛒 Add to Cart system
* ❤️ Wishlist feature
* 👤 User Authentication (Login/Register)
* 📦 Order management
* 🛠️ Admin panel to manage products
* ☁️ Image storage using Cloudinary

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (development) / PostgreSQL (production)
* **Media Storage:** Cloudinary
* **Deployment (planned):** Railway / Render

---

## 📂 Project Structure

```
shopora_project/
│
├── store/
├── shopora_project/
├── media/
├── staticfiles/
├── templates/
├── manage.py
├── requirements.txt
├── screenshot.png
└── .env
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/shopora.git
cd shopora
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```
SECRET_KEY=your_secret_key
DEBUG=True

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

---

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create superuser

```bash
python manage.py createsuperuser
```

---

### 7. Run server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 🖼️ Image Handling

* Images uploaded via Django Admin
* Stored using Cloudinary
* Served via CDN

---

## 🔐 Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

## ⚠️ Notes

* SQLite is for development only
* Use PostgreSQL for production
* Keep `.env` secure

---

## 👨‍💻 Author

**Annu Soni**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
