# Faisal Security Core - Password Generator

A clean, modern Graphical User Interface (GUI) application built with Python using `CustomTkinter`. This application allows you to generate highly secure, random passwords instantly based on customizable length and character choices.

---

## 🚀 Features

* **Modern & Adaptive UI:** Built with a custom blueprint theme that automatically switches layout states to match your user system (Light or Dark mode).
* **Length Controller Slider:** Adjust your password length seamlessly using an interactive dragging slider.
* **Custom Character Pool:** Toggle distinct checkboxes to include or exclude:
  * Uppercase Letters (`A-Z`)
  * Lowercase Letters (`a-z`)
  * Numbers (`0-9`)
  * Special Characters/Symbols (`!@#$%^&*`)
* **One-Click Clipboard Copy:** Features a built-in "Copy" utility that saves your generated password directly to your system clipboard for instant use.

---

## 📂 File Structure

* `password_generator.py` — The primary standalone script containing the application layout setup, random selection math, and clipboard configuration.

---

## 🛠️ How to Setup and Run

### 1. Install Dependencies
Before running the application, make sure you have the modern UI component library installed via terminal:
```bash
pip install customtkinter
