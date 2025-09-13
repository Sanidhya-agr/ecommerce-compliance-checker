# 🛒 E-Commerce Compliance Checker  
**Smart India Hackathon 2025 Project**

An **AI-powered Legal Metrology Compliance Checker** that automatically verifies product listings on e-commerce platforms against the **Legal Metrology (Packaged Commodities) Rules, 2011**.  

This tool helps regulators and marketplaces ensure that product listings display accurate and legally required declarations, protecting consumers and promoting fair trade.  

---

## 📌 Problem Statement  
With the exponential growth of e-commerce in India, regulatory authorities face challenges in **ensuring compliance** with Legal Metrology guidelines. Many listings miss mandatory information such as:  

- Manufacturer/Importer details  
- Net quantity (weight/volume/number)  
- Maximum Retail Price (MRP) inclusive of all taxes  
- Date of manufacture/import  
- Country of origin  
- Consumer care details  

Manual verification is inefficient. Hence, an **automated, scalable solution** is required.  

---

## 🎯 Proposed Solution  
We propose a **smart compliance engine** that:  
1. **Crawls e-commerce websites** (Amazon, Flipkart, etc.) to extract product data.  
2. **Applies OCR** on product images to read labels in multiple languages.  
3. **Validates fields** against Legal Metrology rules via a **configurable Rule Engine**.  
4. **Flags non-compliance** (missing MRP, wrong units, etc.) in real-time.  
5. Provides a **regulator dashboard** for monitoring compliance trends.  

---

## 🏗️ System Architecture  

- **Crawler Module**: Scrapes product metadata and images  
- **OCR & CV Module**: Extracts declarations from product packaging images  
- **Rule Engine**: Validates extracted data against configurable rules  
- **Dashboard**: Displays compliance score, violations, analytics  

---

## ⚙️ Tech Stack  

### 🔹 Member 1 – Data Acquisition (Crawler)  
- Python, Requests, BeautifulSoup, Selenium/Playwright, Pandas  

### 🔹 Member 2 – OCR & Computer Vision  
- Python, OpenCV, EasyOCR, Tesseract, Pillow  

### 🔹 Member 3 – Rule Validation Engine  
- Python, Regex, JSON Config, Pydantic, (Optional NLP: spaCy/Transformers)  

### 🔹 Member 4 – Dashboard & Reporting  
- Streamlit, Plotly, Pandas, FPDF/ReportLab  

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Sanidhya-agr/ecommerce-compliance-checker
cd ecommerce-compliance-checker
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

### 2️⃣ Setup Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac


3️⃣Install Dependencies
pip install -r requirements.txt
