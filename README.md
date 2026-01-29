# 🧩 Custom Payload Encoder & Obfuscation Framework

A modular, ethical **payload encoding and obfuscation framework** built in Python to demonstrate how simple encoding and string obfuscation techniques can bypass **basic signature-based detection**.

> ⚠️ This project is **educational and lab-only**. No payloads are executed, and no real systems are attacked.

---

## 📌 Project Overview

Modern security tools often rely on **static signatures** to detect malicious content.  
Attackers modify payloads using **encoding and obfuscation** to evade such detection.

This framework simulates that behavior in a **controlled environment** by:
- Encoding payloads (Base64, XOR, ROT13)
- Applying string obfuscation techniques
- Testing detection using simple signature matching
- Comparing detection results
- Generating analysis reports

---

## 🎯 Project Goals

- Understand how payload transformation affects detection
- Demonstrate limitations of signature-based security
- Learn encoding and obfuscation techniques
- Build a modular, extensible security research tool
- Produce audit-style reports for analysis

---

## ⚙️ Features

- ✅ Multiple encoding methods  
  - Base64  
  - XOR (user-defined key)  
  - ROT13  

- ✅ String obfuscation techniques  
  - Random character insertion  
  - String splitting & concatenation  
  - Hex escape sequence obfuscation  

- ✅ Multi-layer encoding support  
- ✅ Signature-based detection simulation  
- ✅ Automatic report generation (saved to file)




