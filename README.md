# 🔐 File Encryption Tool

A Python-based file encryption tool that uses **XOR byte-level encryption** to secure any file type. Simple interface, user-provided key — no extra dependencies needed.

---

## 📌 Features

- Encrypts any file (text, image, binary, etc.)
- XOR-based byte-level encryption
- User-friendly interface — no command line knowledge needed
- Custom key provided by the user at runtime
- Lightweight — built with Python standard library only

---

## 🚀 How to Run

1. Clone the repository
```bash
   git clone https://github.com/dmittal17/encryption.git
   cd your-repo-name
```

2. Run the script
```bash
   python encryption_tool.py
```

3. Follow the on-screen interface:
   - Enter the path of the file you want to encrypt
   - Enter your encryption key
   - The encrypted output file will be saved in the same directory

---

## 🛠️ How It Works

The tool reads the input file in **binary mode**, then applies **XOR encryption** byte by byte using the user-provided key. The key is cycled across the file length using Python's `itertools.cycle`, ensuring every byte is encrypted regardless of file size.

encrypted_byte = original_byte XOR key_byte

The result is written to a new binary output file.

---

├── encryption_tool.py   # Main script

└── README.md

---

## ⚠️ Note

XOR encryption is a foundational encryption technique, great for learning purposes. For production-level security, consider using libraries like `cryptography` or `PyCryptodome`.

---

## 👩‍💻 Author

**Dhruvi** — B.Tech Automation & Robotics, JSPM Rajarshi Shahu College of Engineering  
Built as part of my learning journey in Python and systems programming.

