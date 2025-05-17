# ⚙️ CentOS Script Repository for UA-1378 TAQC Students

Repository of CentOS scripts created by students of the UA-1378 TAQC program.

---

## 📂 Project Overview

This project is dedicated to housing a collection of practical scripts designed to interact with CentOS environments. Our current focus includes:

- 📤 **File Transfer to CentOS:** Scripts that automate the process of securely sending files to a remote CentOS server.
- 📥 **File Retrieval from CentOS:** Tools for efficiently copying files back from the CentOS system to our local machines.
- 📧 **Email Interaction:** Scripts that enable us to send and read emails for specific users within the CentOS environment, facilitating testing and automation of email-related functionalities.

---

## 🌳 Project Structure

To maintain a clear and organized structure, the repository follows a specific convention:
```
📂 src
├── 📂 [Your GitHub Username]
│   ├── your_script_name.py (create subfolders if you need)
```

Under the `src` folder, each student creates a subfolder named after their GitHub username.

---

## 🛠️ Technologies & Tools

The scripts within this repository leverage a range of technologies to achieve their goals, including:

- 🐧 **CentOS:** The target operating system for our automation scripts.
- 🐍 **Python:** A versatile programming language used for scripting and automation tasks.
- 📜 **Bash:** The standard command-line interpreter for CentOS, used for various system operations.
- 🔑 **SSH (via `paramiko` in Python):** For secure remote connection and command execution on CentOS servers.
- 🔒 **SCP (via `scp` library in Python):** For secure file transfer between local and remote CentOS systems.
- ✉️ **SMTP/IMAP (via `smtplib` and `imaplib` in Python):** For sending and reading emails on CentOS.
- 📂 **`pathlib` (Python):** For working with file paths in a more object-oriented way.
- ⚙️ **Environment Variables (`os` module in Python):** For securely managing configuration details like hostnames, usernames, and passwords.

---

## ✅ Requirements

- 🐍 **Python 3.10+** — the main language for scripts  
- 🖥️ **CentOS VM / Server** — the target environment for execution  
- 🛠️ **Git** — for cloning the repository   

## 🚀 Getting Started (For Students)

1.  **Navigate to your designated directory:**
    ```bash
    cd src/[Your GitHub Username]/
    ```
2.  **Place your CentOS scripts here:** Ensure your scripts are well-documented and follow any project-specific guidelines provided by mentor.
3.  **Commit and push your work:** Regularly commit your changes and push them to the remote repository to share with your peers and mentor.

## 🤝 Collaboration & Learning

This repository is a collaborative learning environment. Feel free to explore the scripts created by your classmates, learn from their approaches, and offer constructive feedback through pull requests or discussions. Let's grow our CentOS automation skills together!

```
print("Happy scripting! 🚀")
```
