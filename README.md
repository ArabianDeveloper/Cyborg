# 🎮 Cyborg

**Cyborg** is a dynamic, Django-based web application tailored for the gaming community. It serves as a centralized platform for managing games, showcasing streams, and sharing gaming clips, backed by a robust user account system.

## 📂 Project Structure

This project is built using the Django framework and is divided into several feature-specific applications:

- **`project/`**: The core Django configuration directory (settings, main URLs, WSGI).
- **`games/`**: Manages the catalog of games, including details, categories, and availability.
- **`streams/`**: Handles live stream integrations, scheduling, and stream displays.
- **`clips/`**: Manages short-form video content and user-uploaded gaming highlights.
- **`accounts/`**: Handles user authentication, registration, profiles, and permissions.
- **`templates/`**: Contains the HTML templates used to render the frontend UI.
- **`static/`**: Houses the heavy JavaScript (83%), CSS, and images used for the highly interactive frontend.
- **`media/`**: Stores user-uploaded files, such as game covers, user avatars, and video clips.
- **`outline.md`**: Contains project notes, roadmaps, and structural planning.

## ✨ Features

- **Gaming Hub:** Browse and manage a library of games.
- **Stream Integration:** Dedicated sections for viewing and managing gaming streams.
- **Clip Sharing:** Upload and watch gaming highlights and short clips.
- **User Authentication:** Secure user registration, login, and personalized profiles.
- **Interactive UI:** A highly responsive frontend heavily powered by JavaScript for a smooth, app-like experience.
- **Local Database:** Pre-configured with SQLite (`db.sqlite3`) for immediate local development.

## 🚀 Prerequisites

To run this project on your local machine, you will need:
- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)

## 🛠️ Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/ArabianDeveloper/Cyborg.git](https://github.com/ArabianDeveloper/Cyborg.git)
cd Cyborg
