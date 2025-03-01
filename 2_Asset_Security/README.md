# 🛡️ CISSP Domain 2: Asset Security  

Asset Security focuses on **protecting data and information assets** throughout their lifecycle. This includes **data classification, ownership, security controls, retention, disposal, handling, and inventory tracking.**  

---

## 📌 1. Data Classification and Ownership

### 📂 **Data Classification**
Data classification helps categorize information based on **sensitivity and importance** to apply appropriate security controls.

#### **Government Classification Levels**
| Level          | Description |
|---------------|------------|
| **Top Secret** | Highest level, severe damage if disclosed (e.g., national security) |
| **Secret**     | Serious harm if leaked (e.g., military plans) |
| **Confidential** | Could cause harm (e.g., personnel files) |
| **Unclassified/Public** | No impact (e.g., press releases) |

#### **Commercial Classification Levels**
| Level          | Description |
|---------------|------------|
| **Confidential** | Most sensitive (e.g., trade secrets, financial data) |
| **Private**     | Internal use (e.g., employee records) |
| **Sensitive**   | Requires protection (e.g., project documents) |
| **Public**      | No security risk (e.g., website content) |

---

### 👤 **Data Ownership**
| Role            | Responsibility |
|----------------|---------------|
| **Data Owner**  | Defines classification & access policies |
| **Data Custodian** | Implements security controls |
| **Data Steward** | Ensures data integrity and compliance |
| **Data User**   | Uses data per policies |

---

## 🔐 2. Data Security Controls

### 🔒 **Encryption**
Encryption **protects data** by converting it into unreadable ciphertext.

#### **Types of Encryption:**
- **Symmetric (AES, DES, 3DES)** – Fast but uses the same key for encryption & decryption.
- **Asymmetric (RSA, ECC)** – Uses **public-private key pairs** for security.
- **Data-at-Rest Encryption** – Protects stored data (`BitLocker, VeraCrypt`).
- **Data-in-Transit Encryption** – Secures data being transmitted (`TLS, VPN, IPsec`).

---

### ✨ **Data Masking**
Data masking **hides sensitive information** by replacing it with fictitious data.

#### **Types of Data Masking:**
- **Static Masking** – Alters data permanently.
- **Dynamic Masking** – Masks data only when accessed.

---

### 🔑 **Tokenization**
Tokenization **replaces sensitive data** with non-sensitive placeholders.

```plaintext
Example:
Original: 4111 1111 1111 1111
Tokenized: X123ABC567XYZ

📌 Tool Ideas:
	•	AutoClassify → AI-based data classification & tagging system.
    •	Encryptify → Open-source encryption tool for file, disk, and database encryption.
    •	TokenShield → Secure data tokenization API for payment and identity security.
	•	MaskerX → Data masking engine for test environments and compliance.

    •	RetentionManager → Automates data retention policies based on regulations (GDPR, HIPAA, PCI-DSS).
	•	DataWiper → Secure file and disk wiping (DoD 5220.22-M, NIST 800-88).
	•	CryptoErase → Encrypts files and destroys keys for instant secure deletion.
	•	EOLTracker → Tracks data expiration and alerts for retention compliance.

	•	DLPShield → AI-driven real-time data leakage prevention.
	•	EmailDLP → Prevents email-based data leaks (sensitive data scanning).
	•	AssetMapper → Scans network & detects all connected assets (IoT, servers, endpoints).

+-----------------------------+
|      Data Sources           |  (Files, Emails, Databases, Cloud Storage)
+-----------------------------+
            │
            ▼
+-----------------------------+
|      Data Preprocessing     |  (File scanning, text extraction, NLP)
+-----------------------------+
            │
            ▼
+-----------------------------+
|      Classification Model   |  (AI/ML - NLP, Regex, TF-IDF, BERT)
+-----------------------------+
            │
            ▼
+-----------------------------+
|   Tagging & Labeling Engine |  (Confidential, Public, PII, PCI, etc.)
+-----------------------------+
            │
            ▼
+-----------------------------+
|    Reporting & Integration  |  (API, GUI, Database, Email Alerts)
+-----------------------------+

🔹 Phase 1: Basic File Classification
	•	Develop a File Scanner for text, PDF, Word, Excel, JSON, CSV.
	•	Implement Regex-based pattern matching (e.g., SSNs, emails, credit card numbers).
	•	Train Named Entity Recognition (NER) models to detect sensitive keywords.

🔹 Phase 2: AI/ML-Based Classification
	•	Build an AI model using NLP techniques (TF-IDF, BERT, GPT-4 API).
	•	Train the model with labeled datasets (financial, healthcare, personal data, etc.).
	•	Implement auto-labeling & risk scoring (High, Medium, Low sensitivity).
