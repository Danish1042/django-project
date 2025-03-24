# 🏗️ Django Project with TailwindCSS  

This Django project uses **TailwindCSS** for styling, an **SQLite3 database**, and the **Django admin panel** to manage data. The project includes **forms, templates, and pages** to display and manage data efficiently.

## 📦 Features
- 🎨 **TailwindCSS** for responsive & modern UI  
- 🗂️ **SQLite3 Database** for storing data  
- 📝 **Forms** for user input  
- 🏛️ **Default Django Admin Panel** for managing data  
- 📄 **Templates & Pages** for frontend views  
- 🔄 **GET & Display Data** from the database  
- ✅ **Admin Panel for Data Storage**  

## 🛠 Project Structure
```
📂 your_project/
 ├── 📁 your_app/         # Django App
 │   ├── 📁 migrations/   # Database Migrations
 │   ├── 📄 models.py     # Database Models
 │   ├── 📄 views.py      # Application Logic
 │   ├── 📄 forms.py      # Forms for Data Input
 │   ├── 📄 urls.py       # URL Routing
 │   ├── 📁 templates/    # HTML Templates
 ├── 📁 static/           # CSS, JS, Images
 ├── 📁 templates/        # Global Templates
 ├── 📄 db.sqlite3        # SQLite Database
 ├── 📄 manage.py         # Django Management Script
 ├── 📄 .gitignore        # Files to Ignore in Git
 ├── 📄 requirements.txt  # Python Dependencies
 ├── 📄 README.md         # Project Documentation
```

## 🎨 Using TailwindCSS
Tailwind is included via **CDN** or installed via **npm**.  

If using **CDN**, add this in `base.html`:
```html
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
```

For **npm-based installation**, install Tailwind and configure `tailwind.config.js`.  

## 🔧 Admin Panel Access
Visit:  
👉 `http://127.0.0.1:8000/admin/`  
Login with your **superuser credentials**.

## 📜 License
This project is open-source under the **MIT License**.

### 🚀 Happy Coding! 😊

