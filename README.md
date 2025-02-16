# 🚀 RESQ.AI - Emergency Help System  

RESQ.AI is an AI-powered emergency resource management system designed to optimize crisis response by collecting real-time data from hospitals, relief centers, and responders.

## 🌟 Features  
- 🔍 **Real-Time Data Collection** - Updates hospital capacity, medicine stocks, and emergency resources.  
- 🤖 **AI-Driven Logistics** - Detects shortages and reallocates resources dynamically.  
- 🔔 **Automated Alerts System** - Sends crisis warnings based on real-time data.  
- 📍 **Emergency Locator** - Finds nearby hospitals, shelters, and relief centers.  
- 📊 **Admin Dashboard** - Displays live crisis data, predictions, and reports.  
- 🗺 **Live Crisis Map** - Shows real-time crisis hotspots via Google Maps API.  
- ✅ **User Authentication** - Secure login for normal users and vendors.  

---

## 🛠️ Tech Stack  
### **Frontend:**  
- HTML, CSS, JavaScript (Vanilla JS)  

### **Backend:**  
- Django (Python)  
- Django REST Framework (DRF)  
- MySQL (Database)  
- Blockchain APIs (For trusted data validation)  

### **AI & Machine Learning:**  
- TensorFlow / PyTorch (For crisis predictions)  
- NumPy, SciPy, Pandas (For data processing)  

---

## 🚀 Getting Started  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/rishabh4jakhar/resq.ai.git
cd resqai
```

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Set Up MySQL Database**  
- Create a new MySQL database: `resqai_db`  
- Update **`settings.py`** with your MySQL credentials.  

### **4️⃣ Apply Migrations & Populate Data**  
```sh
python manage.py makemigrations api
python manage.py migrate api
python manage.py populate_db
```

### **5️⃣ Run the Django Server**  
```sh
python manage.py runserver
```
The backend will be available at:  
```
http://127.0.0.1:8000/
```

---

## 🌍 Usage Guide  

### **🏠 Homepage (`index.html`)**  
- Navigation buttons for **Emergency Locator, Live Crisis Map, Dashboard, Alerts**.  
- Login/Register dropdown for users and vendors.  

### **📍 Emergency Locator (`locator.html`)**  
- Allows users to **find hospitals & relief centers** nearby.  

### **🗺 Live Crisis Map (`crisis_map.html`)**  
- Displays **real-time crisis hotspots** using Google Maps API.  

### **📊 Dashboard (`dashboard.html`)**  
- Submit hospital data (name, beds, oxygen supply).  
- View and refresh submitted hospital data.  

### **🔔 Alerts System (`alerts.html`)**  
- Shows AI-generated **emergency alerts and crisis warnings**.  

---

## 📡 API Endpoints  

| Method | Endpoint                | Description |
|--------|-------------------------|-------------|
| **GET**  | `/api/hospitals/`       | Fetch all hospitals |
| **POST** | `/api/hospital/`        | Add a new hospital |
| **GET**  | `/api/alerts/`          | Get active crisis alerts |
| **GET**  | `/api/ai/shortages/`    | AI-predicted resource shortages |
| **GET**  | `/api/ai/suppliers/{resource}/` | Suggested alternative suppliers |
| **POST** | `/api/auth/register/`   | Register a new user/vendor |
| **POST** | `/api/auth/login/`      | User login with JWT authentication |

---

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

🚀 **Now you're ready to push this to GitHub!** Let me know if you need any modifications. 😊

