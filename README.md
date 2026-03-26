# 🧠 MedLedger: Blockchain-Based Medical Supply Chain

## 📌 Overview

MedLedger is a blockchain-based system designed to ensure **secure, transparent, and tamper-proof tracking** of medical products across the supply chain.

It enables tracking of medicines from:

* Pharma → Distributor → Retailer

---

## 🚀 Features

* 🔗 Blockchain-based transaction storage
* 🔐 Secure transfers using digital signatures
* 👥 Role-based supply chain validation
* 📊 Transparent product tracking
* 🛡️ Tamper-proof data using hashing

---

## 🏗️ Project Architecture

### 1. Blockchain Layer

* `block.py` → Defines block structure
* `blockchain.py` → Manages chain and validation

### 2. Security Layer

* `secure_transfer.py` → Digital signatures
* `key_gen.py` → RSA key generation

### 3. Business Logic

* `rule_engine.py` → Validates transfer rules

### 4. Storage

* `database.py` → Stores transaction data

### 5. Application Layer

* `app.py` → Main execution and integration

---

## 🔄 Workflow

1. Pharma creates product
2. Transfer initiated
3. Rule engine validates transaction
4. Transaction signed using private key
5. Verified using public key
6. Added to blockchain
7. Stored in database

---

## 🔐 Security

* Public/Private Key Cryptography
* Digital Signatures
* Hash-based Integrity

---

## 🧪 Tech Stack

* Python
* Cryptography (RSA)
* Blockchain Concepts

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
```

---

## 🎯 Use Case

* Prevent counterfeit medicines
* Improve supply chain transparency
* Ensure data integrity

---

## 👨‍💻 Author

Sagar Verma
B.Tech, NIT Srinagar

---

## 📌 Future Improvements

* Web interface (React + Flask)
* Smart contracts
* QR-based tracking
* Integration with IoT devices

---
