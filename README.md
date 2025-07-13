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
📁 CENTOS
├── 📁 .venv/             # Local virtual environment (not tracked by Git)
├── 📁 logs/              # Output logs (auto-generated, ignored by Git)
├── 📁 legacy/            # Deprecated or archived code/data
├── 📁 resources/         # Static files, environment configs, etc.
├── 📁 src/               # Source code
│   ├── 📁 config/        # Configuration files (e.g. logger setup)
│   ├── 📁 libraries/     # Custom Python libraries (e.g. env loader, SMTP client)
│   ├── 📁 resources/     # Robot Framework resource files
│   └── 📁 tests/         # Robot Framework test cases
├── .env                 # Environment variables file
├── .gitignore
├── README.md
├── requirements.txt     # Python dependencies
├── log.html             # Robot Framework log (auto-generated)
├── output.xml           # Robot Framework output (auto-generated)
└── report.html          # Robot Framework report (auto-generated)
```


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

- 🐍 **Python 2.7.18** — the main language for scripts  
- 🖥️ **CentOS VM / Server** — the target environment for execution  
- 🛠️ **Git** — for cloning the repository   

---

## 🚀 Getting Started (For Students)

1.  **Navigate to your designated directory:**
    ```bash
    cd src/[Your GitHub Username]/
    ```
2.  **Place your CentOS scripts here:** Ensure your scripts are well-documented and follow any project-specific guidelines provided by mentor.
3.  **Commit and push your work:** Regularly commit your changes and push them to the remote repository to share with your peers and mentor.

---

## 📦 Install & Setup

### ✅ 1. Install Postfix and Dovecot

Follow this guide to install and configure Postfix and Dovecot on CentOS 9:  
🔗 [Postfix + Dovecot Setup Guide](https://reintech.io/blog/setup-mail-server-postfix-dovecot-centos9)

---

### 🐍 2. Install Python 2.7.18

Download and install Python 2.7.18:  
🔗 [Python 2.7.18 Download](https://www.python.org/downloads/release/python-2718/)

Add it to your system PATH.

---

### 📥 3. Install OpenSSL (Windows Only)

Download and install the latest full version of OpenSSL for Windows:  
🔗 [Win32/Win64 OpenSSL Installer](https://slproweb.com/products/Win32OpenSSL.html)

Choose the appropriate installer (usually **Win64 OpenSSL v1.1.x** for 64-bit systems).  
✅ During installation, check **"Copy OpenSSL DLLs to the Windows system directory"**.

After installation, verify OpenSSL is working by running in terminal:

```bash
openssl version
```
Expected output close to that:
```bash
OpenSSL 3.5.1 1 Jul 2025 (Library: OpenSSL 3.5.1 1 Jul 2025)
```

---

### 🧪 4. Install `virtualenv`

Install `virtualenv` (version 16.7.12):
```bash
pip install virtualenv==16.7.12
```

---

### 📁 5. Clone the Repository

Clone the repo:
```bash
git clone https://github.com/UA-1378-TAQC/centOS.git
```

Switch to the project folder:
```bash
cd centOS
```

If working on the `smtp_testing` branch:
```bash
git checkout smtp_testing
```

---

### 🌱 6. Create a Virtual Environment

On Windows:
```bash
virtualenv .venv -p C:\Python27\python.exe
.\.venv\Scripts\activate
```

On Linux/macOS:
```bash
virtualenv .venv -p /usr/bin/python2.7
source .venv/bin/activate
```

---

### 📦 7. Install Dependencies

Install Python packages:
```bash
pip install -r requirements.txt
```

If win-init-pton==1.1.0 triggered error, then:
```cmd
cd legacy\offline_packages
```
and
```cmd
python -m pip install --no-index --no-deps --find-links=. win_inet_pton-1.1.0-py2.py3-none-any.whl
```

---

### ⚙️ 8. Configure `.env`

Create a `.env` file in the project root folder:

```properties
HOSTNAME='your_server_ip'
TCP_TIMEOUT=5

SSH_PORT='your_ssh_port'
SSH_USERNAME='your_ssh_username'
SSH_PASSWORD='your_ssh_password'

DOMAIN='@example.com'
SMTP_PORT='25'
EMAIL_DIR='/var/spool/mail/your_email_username'

LOCAL_SENDER='user1@example.com'
REMOTE_RECIPIENT='user2@example.com'
```

#### 🧪 Example `.env`:
```properties
HOSTNAME="127.0.0.1"
TCP_TIMEOUT=5

SSH_PORT=22
SSH_USERNAME="dms"
SSH_PASSWORD="root"

DOMAIN='@example.com'
SMTP_PORT=25
EMAIL_DIR='/home/dms/Maildir/smtp_test'

LOCAL_SENDER='user1@example.com'
REMOTE_RECIPIENT='user2@example.com'
```

---

## ✅ Ready to go

Once the setup is complete, you can start testing your scripts.

---

## 🤝 Collaboration & Learning

This repository is a collaborative learning environment. Feel free to explore the scripts created by your classmates, learn from their approaches, and offer constructive feedback through pull requests or discussions. Let's grow our CentOS automation skills together!

```
print("Happy scripting! 🚀")
```