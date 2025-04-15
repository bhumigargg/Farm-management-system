from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime, timedelta
import os
import pymysql
pymysql.install_as_MySQLdb()

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/farmers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define models
class Farmer(db.Model):
    __tablename__ = 'register'  # Match the table name in main.py
    rid = db.Column(db.Integer, primary_key=True)
    farmername = db.Column(db.String(50))
    adharnumber = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    phonenumber = db.Column(db.String(50))
    address = db.Column(db.String(50))
    farming = db.Column(db.String(50))

class Farming(db.Model):
    __tablename__ = 'farming'  # Match the table name in main.py
    fid = db.Column(db.Integer, primary_key=True)
    farmingtype = db.Column(db.String(100))

class AgroProduct(db.Model):
    __tablename__ = 'addagroproducts'  # Match the table name in main.py
    pid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    productname = db.Column(db.String(100))
    productdesc = db.Column(db.String(300))
    price = db.Column(db.Integer)

# Sample data lists
first_names = ['Raj', 'Amit', 'Priya', 'Suresh', 'Meera', 'Vijay', 'Anita', 'Rahul', 'Kavita', 'Deepak']
last_names = ['Sharma', 'Patel', 'Singh', 'Kumar', 'Verma', 'Gupta', 'Yadav', 'Mishra', 'Jain', 'Malik']
villages = ['Green Valley', 'Sunrise Farms', 'Harvest Hills', 'Golden Fields', 'River View']
crops = ['Wheat', 'Rice', 'Corn', 'Soybean', 'Cotton', 'Sugarcane', 'Potato', 'Tomato', 'Onion', 'Chili']
equipment = ['Tractor', 'Harvester', 'Plow', 'Seeder', 'Irrigation System', 'Sprayer']
products = ['Organic Fertilizer', 'Pesticide', 'Seeds', 'Farming Tools', 'Irrigation Equipment']

def generate_sample_data():
    with app.app_context():
        # Generate farmers
        for i in range(10):
            farmer = Farmer(
                farmername=f"{random.choice(first_names)} {random.choice(last_names)}",
                adharnumber=f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}",
                age=random.randint(25, 65),
                gender=random.choice(['Male', 'Female']),
                phonenumber=f"+91 {random.randint(70000, 99999)}{random.randint(10000, 99999)}",
                address=f"{random.randint(1, 100)}, {random.choice(villages)}, District {random.randint(1, 10)}",
                farming=random.choice(['Organic', 'Conventional', 'Mixed'])
            )
            db.session.add(farmer)

        db.session.commit()
        print("Farmers data generated successfully!")

        # Generate farming types
        farming_types = ['Organic', 'Conventional', 'Mixed', 'Hydroponic', 'Aquaponic']
        for farming_type in farming_types:
            farming = Farming(farmingtype=farming_type)
            db.session.add(farming)

        db.session.commit()
        print("Farming types generated successfully!")

        # Generate agro products
        for _ in range(20):
            product = AgroProduct(
                username="admin",
                email="admin@example.com",
                productname=random.choice(products),
                productdesc=f"High-quality {random.choice(products)} for {random.choice(['small', 'medium', 'large'])} scale farming",
                price=random.randint(100, 5000)
            )
            db.session.add(product)

        db.session.commit()
        print("Agro products generated successfully!")

        print("\nAll sample data generated successfully!")

if __name__ == "__main__":
    generate_sample_data() 