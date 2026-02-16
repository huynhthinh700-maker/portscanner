# portscanner
PORTSCANNER
🔎 Python Port Scanner

A simple TCP port scanner written in Python for learning networking and basic cybersecurity concepts.

📌 Features

Scan ports from 1 → 65535

Detect open ports on a target

Shows scan start time

Handles errors (invalid host, connection error, keyboard interrupt)

Lightweight and beginner-friendly

⚙️ Requirements

Python 3.x

Linux / Windows / macOS

No external libraries required.

🚀 Usage

Run from terminal:

python3 portscanner.py <target>


Example:

python3 portscanner.py scanme.nmap.org


Output example:

This is target's ip: 45.33.32.156
--------------------------------------------------
Scanning target.....
Time started: 2026-02-16 06:50:59
--------------------------------------------------
[OPEN] Port 22
[OPEN] Port 80

🧠 How it works

Uses Python socket module

Attempts TCP connection to each port

If connection succeeds → port is open

Uses timeout to speed up scanning

Core function used:

socket.connect_ex()


Returns:

0 → port open

other value → closed

📂 Project Structure
portscanner/
│
├── portscanner.py
└── README.md

🎯 Learning Purpose

This project was built to practice:

Python networking

Socket programming

Basic cybersecurity tools

Understanding how port scanning works

⚠️ Disclaimer

This tool is for educational purposes only.
Do not scan targets without permission.

👨‍💻 Author

YourNameHere
