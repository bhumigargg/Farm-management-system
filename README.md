# **Farmer Management System**

The **Farmer Management System** is a web-based platform designed to empower farmers by providing tools for crop management, equipment tracking and access to agricultural products. The system aims to modernize farming practices and improve efficiency through technology.

---

## **Features**
- **Crop Management**: Track and manage crops efficiently.
- **Equipment Tracking**: Keep track of farming equipment and maintenance schedules.
- **Product Marketplace**: Access a wide range of agricultural products, including organic vegetables and farming equipment.
- **User Management**: Farmers can register, log in, and manage their profiles.
- **Responsive Design**: Fully responsive layout for seamless use on desktops, tablets, and mobile devices.

---

## **Key Pages**

### **Home Page**
- Displays a hero section with key features and call-to-action buttons.

### **Farming Page**
- Allows farmers to add and manage farming-related data.

### **Products Page**
- Showcases agricultural products available for purchase.

### **Farmer Details Page**
- Displays detailed information about registered farmers.


## **Technologies Used**
- **Frontend**:
  - HTML5, CSS3, JavaScript
  - [Bootstrap](https://getbootstrap.com/) for responsive design
  - Font Awesome for icons
- **Backend**:
  - [Flask](https://flask.palletsprojects.com/) (Python)
  - Flask extensions: `Flask-SQLAlchemy`, `Flask-Login`
- **Database**:
  - MySQL (via `pymysql`)
- **Other Tools**:
  - Google Fonts for typography
  - Jinja2 templating engine

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/bhumigargg/Farmer-management-system
cd Farmer-management-system
```
### **2. Install Dependencies**
Make sure you have Python installed. Then, install the required Python packages:
```bash
pip install -r requirements.txt
```
### **3. Configure the Database**
  -Create a MySQL database (e.g., farmer_management).  
  -Update the database connection string in main.py:
```bash
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/farmer_management'
```
### **4. Run the Application**
```bash
python [main.py](http://_vscodecontentref_/1)
```

