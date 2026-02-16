# 🔎 Python Port Scanner

A simple TCP port scanner written in Python for learning networking and basic cybersecurity concepts.

## 📌 Features
- Scan ports from **1 → 65535**
- Detect open ports on a target
- Displays scan start time
- Handles errors (invalid host, connection failure, keyboard interrupt)
- Lightweight and beginner-friendly
- No external libraries required

## ⚙️ Requirements
- Python 3.x  
- Linux / Windows / macOS  

## 🚀 Usage

Run from terminal:

```bash
python3 portscanner.py <target>
Example:

python3 portscanner.py scanme.nmap.org


Example output:

This is target's ip: 45.33.32.156
--------------------------------------------------
Scanning target.....
Time started : 2026-02-16 06:50:59
--------------------------------------------------
[OPEN] Port 22
[OPEN] Port 80

```

## 🧠 How It Works

This tool uses Python's built-in socket module to perform TCP connections to each port on a target.

**Core logic:**

-Attempts connection to each port

-If connection succeeds → port is open

-Uses timeout to avoid long waiting

-Handles common network errors safely

### Important function used:

socket.connect_ex()
Return values:

0 → port open

other value → port closed

## 📂 Project Structure
portscanner/

│

├── portscanner.py

└── README.md

## 🎯 Learning Purpose

-This project was built to practice:

-Python socket programming

-Networking fundamentals

-Cybersecurity basics

-How port scanning tools work

## ⚠️ Disclaimer

This tool is created for educational and ethical testing purposes only.
Please don't scan systems without proper authorization.

## 👨‍💻 Author
# THXY
Cybersecurity Student | Python Learner
