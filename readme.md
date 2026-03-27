# 🏫 SSSchool v5.0.2 – Comprehensive School ERP & LMS Platform

This is a **technical showcase** of the 5th generation of the **SSSchool** platform, a full-scale Enterprise Resource Planning (ERP) and Learning Management System (LMS) developed by **SASKE Company**.

It demonstrates a modular architecture designed to handle all aspects of educational institution management, from financial accounting to academic grading and parent communication.

> 🛡️ **Intellectual Property Notice:** The production source code is private. This repository contains the core architecture and UI demo for professional evaluation.

---

## 📌 Project Showcase

🟢 **project ad**: [SSSchool v5.0.2 Overview](https://www.facebook.com/share/v/1GecroeGow/)  
🟢 **video rev**: [SSSchool v5.0.2 Overview](https://youtu.be/1IVa3OVKIIY?si=Q7ZJ24mJSp5bIpBE)  
🟢 **project details**: [SSSchool v5.0.2 Overview](https://youtu.be/hob8HArDnoo?si=pmxOn7q3q_L2XdWL)  
📌 **Version**: 5.0.1 (Production Ready)

---

## 🎯 Key Modules & Features

### 1. 👥 Multi-Role User Management (RBAC)
- **Super Admin:** Full school control, branch management, and system logs.
- **Academic Staff:** Student registration, attendance, and grading.
- **Teachers:** Lesson planning, virtual classrooms, and assignment tracking.
- **Parents & Students:** Performance monitoring, financial status, and internal messaging.

### 2. 💰 Financial & Billing Engine
- Automated tuition fee generation and discount management.
- Detailed financial reports (Profit/Loss, Expense tracking).
- Integration with payment gateways for online fee collection.

### 3. 📚 Academic & LMS Core
- Dynamic timetable generation.
- Online exam engine with automated grading.
- Student performance analytics and behavioral tracking.

### 4. 📱 Communications & Notifications
- Centralized notification center for school-wide announcements.
- SMS/Email integration for attendance and emergency alerts.

---

## 🛠️ Technical Stack

| Category       | Technology                                             |
|----------------|--------------------------------------------------------|
| **Backend** | Python 3.13, Django 5.x (Enterprise Pattern)              |
| **Frontend** | Pug, SASS / Bootstrap 5, npm, gulp, figma                |
| **Database** | mysql (Optimized for complex relational data)            |
| **Real-Time** | WebSockets (Django Channels) for instant notifications  |
| **Deployment** | Docker, Nginx, Gunicorn on Ubuntu Server               |

---

## 📂 System Architecture (Core Demo)
```bash
ssschool-v5/
├── coaches/             # Management of instructors and training staff
├── home/                # Landing page and public-facing modules
├── live/                # Real-time virtual classrooms / Live streaming logic
├── media/               # User-uploaded content (Lessons, Assignments)
├── news/                # School announcements and news feed
├── pay/                 # Financial engine, billing, and payment gateways
├── reports/             # Academic and financial reporting modules
├── saskeproject/        # Core project settings and WSGI/ASGI config
├── staticfiles/         # Collected static assets for production
├── students/            # Student management, profiles, and attendance
├── tasks/               # Assignments and automated background tasks
├── templates/           # Global HTML layouts and UI components
├── db.sqlite3           # Local development database
├── manage.py            # Django administrative command-line utility
├── Procfile             # Deployment configuration (Heroku/PaaS)
└── requirements.txt     # Project dependencies and libraries
```

---

## 🔐 License & Usage

This project is released under a **Custom Proprietary License**. It is intended for technical evaluation and portfolio showcasing only. 

### ❌ Strict Prohibitions:
- **Commercial Deployment:** Unauthorized use for school management or educational services.
- **Reselling:** Redistributing or reselling the core ERP logic or design.
- **Replication:** Copying the unique financial engine or RBAC structure for commercial products.

### ✅ Permitted Actions:
- **Professional Review:** Code audit and architecture exploration for hiring/evaluation.
- **Educational Inspiration:** Understanding the integration between Django and React in ERP systems.

> 🛡️ **Business Inquiries:** > For licensing, full source code access, or commercial partnerships, please contact:  
> **📧 sultanelsultan4@gmail.com**

---

# 👤 Author

## Sultan Abdelkareem
### Lead Full-Stack Developer | Founder of SASKE Company
**Expertise:** Django, React, Enterprise ERP Systems, DevOps (8+ Yrs)

- 🔗 [LinkedIn](https://www.linkedin.com/in/sultan-abd-alkareem/)
- 🌐 [Portfolio](https://effulgent-shortbread-2bf423.netlify.app)
- 🏢 [SASKE Company](https://saske.pages.dev)
