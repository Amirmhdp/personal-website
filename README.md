# Personal Portfolio Website

A modern, responsive, and dynamic personal portfolio website built with **Django, PostgreSQL, Tailwind CSS, and JavaScript**.

This project is designed to showcase my skills, experience, projects, and services while providing a simple and professional way for potential clients to get in touch and submit website development requests.

---

## ✨ Features

* 🎨 Modern and responsive dark UI
* 📱 Fully responsive design for desktop, tablet, and mobile
* 🌐 RTL support for Persian content
* ⚡ Dynamic content management with Django
* 📂 Dynamic projects and project details
* 🛠️ Dynamic skills and services
* 👤 Dynamic personal and website information
* 📩 Contact form with AJAX submission
* 📝 Website order/request form with AJAX
* 🔄 Loading and success states for forms
* 🗃️ PostgreSQL database
* 🐳 Docker and Docker Compose support
* 🔐 Environment-based configuration
* 🎯 Active navigation state
* 📊 Animated statistics and counters
* 🎠 Responsive skills carousel with Swiper
* ✨ Smooth UI interactions and visual effects
* 🧩 Lucide icons
* 📱 Mobile navigation menu

---

## 🛠️ Technologies

### Backend

* Python
* Django
* Django ORM

### Frontend

* HTML5
* CSS3
* JavaScript
* Tailwind CSS
* Swiper.js
* Lucide Icons

### Database

* PostgreSQL

### DevOps & Tools

* Docker
* Docker Compose
* Git
* GitHub

---

## 📄 Pages

The website includes the following main sections:

* **Home** — Introduction, statistics, skills, services, and featured projects
* **About Me** — Personal introduction, journey, skills, approach, and current learning
* **Projects** — List of completed projects
* **Project Details** — Detailed information about each project
* **Services** — Available web development services
* **Skills** — Technical skills and technologies
* **Order** — Website development request form
* **Contact** — Contact form for inquiries and consultation

---

## 🚀 Main Projects

### Doctor Appointment System

A complete appointment and booking platform developed with Django.

**Technologies:**

* Django
* PostgreSQL
* Tailwind CSS
* JavaScript
* AJAX
* Celery
* Redis
* Docker

**Features:**

* Patient and doctor accounts
* Doctor panel
* Appointment scheduling
* Online booking
* OTP authentication
* Search and filtering
* Payment integration
* Automated tasks with Celery
* Redis integration

---

### NEWKALA

A dynamic e-commerce website built with Django.

**Technologies:**

* Django
* PostgreSQL
* Tailwind CSS
* JavaScript
* AJAX

**Features:**

* Product management
* Categories and brands
* Product filtering
* Price filtering
* Color filtering
* Product search
* Sorting
* Wishlist
* Reviews
* Shopping cart
* Authentication
* Discount system
* Pagination

---

## 🏗️ Project Structure

```text
personal-website/
│
├── home_module/
├── projects_module/
├── order_module/
├── contact_module/
│
├── personal_website/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── media/
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env
├── .gitignore
├── manage.py
├── package.json
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Amirmhdp/personal-website.git
cd personal-website
```

### 2. Create environment variables

Create a `.env` file in the root directory:

```env
DB_NAME=personal_website
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432
```

> Never commit your `.env` file to GitHub.

---

## 🐳 Run with Docker

Make sure Docker Desktop is installed and running.

Build and start the containers:

```bash
docker compose up --build
```

The website will be available at:

```text
http://localhost:8000/
```

### Run migrations

```bash
docker compose exec django python manage.py migrate
```

### Create a superuser

```bash
docker compose exec django python manage.py createsuperuser
```

### View Django logs

```bash
docker compose logs -f django
```

### Stop containers

```bash
docker compose down
```

---

## 💻 Local Development Without Docker

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

---

## 🎨 Tailwind CSS

The project uses Tailwind CSS for styling.

Install the Node dependencies:

```bash
npm install
```

Run Tailwind in development mode:

```bash
npm run dev
```

The Tailwind configuration watches the input file and generates the compiled CSS automatically.

---

## 🔐 Environment Variables

Sensitive configuration is stored in environment variables instead of being hardcoded in the project.

Example:

```env
DB_NAME=personal_website
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432
```

The `.env` file is excluded from Git using `.gitignore`.

---

## 📱 Responsive Design

The interface is designed to work across different screen sizes:

* 📱 Mobile
* 📱 Tablet
* 💻 Laptop
* 🖥️ Desktop

The layout uses responsive Tailwind CSS utilities to adapt the interface to different viewport sizes.

---

## 🎯 Development Goals

The main goals of this project are:

* Building a professional personal brand
* Showcasing real-world web development projects
* Demonstrating Django backend development skills
* Creating a responsive and modern frontend
* Providing an easy way for clients to request projects
* Practicing scalable and maintainable Django development
* Applying Docker and PostgreSQL in a real project

---

## 📚 Currently Learning

I'm continuously improving my development skills and currently focusing on:

* Advanced Django
* Django REST Framework
* React
* Nginx
* Deployment
* REST APIs
* Advanced backend development
* Docker and production workflows

---

## 🔮 Future Improvements

Planned improvements for the project include:

* [ ] Advanced admin dashboard
* [ ] Django REST API
* [ ] Blog system
* [ ] SEO improvements
* [ ] Production deployment
* [ ] Nginx configuration
* [ ] Automated deployment
* [ ] Improved project analytics
* [ ] More advanced animations
* [ ] Performance optimization

---

## 📬 Contact

If you are looking for a developer to build a modern website or web application, feel free to get in touch through the contact section of the website.

**Developer:** Amir
**Role:** Web Developer
**Main Focus:** Python & Django

---

## ⭐ About This Project

This project is continuously evolving as I learn new technologies and improve my development workflow.

It represents my approach to building modern web applications with a focus on:

**Clean Code • Performance • Security • User Experience • Scalability**

---

## 📄 License

This project is a personal portfolio website.

The source code is publicly available for educational and portfolio purposes. Please do not reuse the personal content, images, branding, or project assets without permission.
