# 🚦 Traffic Chalan Management System

This is a student project I developed using **Python, Computer Vision, AI, and SQLite** to create a simple Traffic Chalan Management System.

The main idea of the project is to upload an image of a vehicle, detect its number plate, identify the traffic violation, and generate the corresponding chalan details.

## 🔄 How It Works

The basic workflow of my project is:

**Upload Vehicle Image → Number Plate Detection → Vehicle Details Retrieval → Violation Detection → Fine Calculation → WhatsApp-Ready Notification**

### 1. 📷 Upload Image

The user uploads an image of a vehicle through the Streamlit interface.

### 2. 🔍 Number Plate Detection

The project uses **OpenCV** and the **Haar Cascade Russian Number Plate** pretrained model to detect the vehicle's number plate.

### 3. 🚗 Retrieve Vehicle Details

After identifying the vehicle number, the project checks the **SQLite3 database** and retrieves the related details, such as:

* Vehicle number
* Owner name
* Phone number

### 4. 🚨 Detect Traffic Violation

The uploaded image is analyzed to identify the traffic violation that has been committed.

### 5. 💰 Calculate Fine

Based on the detected violation, the system determines the applicable fine.

The final chalan information includes:

* 👤 Owner name
* 🚗 Vehicle number
* 📱 Phone number
* 🚨 Violation
* 💰 Fine amount

### 6. 💬 WhatsApp-Ready Notification

The project also prepares a notification containing the chalan details, which can be used as a **WhatsApp-ready message** for the vehicle owner.

## 🛠️ Technologies Used

* **Python** – Main programming language
* **Streamlit** – User interface
* **OpenCV** – Image processing and computer vision
* **Haar Cascade Russian Number Plate** – Pretrained model for number plate detection
* **Groq** – AI-based processing
* **SQLite3** – Storing and retrieving vehicle/chalan information

## ✨ Main Features

* Upload vehicle images
* Detect vehicle number plates
* Recognize vehicle number information
* Retrieve owner details from SQLite database
* Detect traffic violations
* Determine the applicable fine
* Generate chalan information
* Prepare WhatsApp-ready notifications
* Simple Streamlit user interface

## 📂 Project Files

```text
traffic-chalan-project/
│
├── app.py
├── main.py
├── violation_detection.py
├── number_plate_detection.py
├── number_plate_reco.py
├── chalan_gen.py
├── database.py
├── requirements.txt
├── img/
└── .gitignore
```

## ▶️ How to Run

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Add your Groq API key

Create a `.env` file in the project folder:

```env
api_key=YOUR_GROQ_API_KEY
```

**Do not upload your `.env` file or your real API key to GitHub.**

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

## 📚 What I Learned

This project helped me get practical experience with:

* Python programming
* OpenCV and image processing
* Number plate detection
* Working with pretrained models
* Using APIs
* Working with Groq
* SQLite database operations
* Building a user interface using Streamlit
* Connecting different components together to create a complete project

## 🚀 Future Improvements

I would like to improve this project further by making the violation detection and number plate recognition more accurate, adding more types of traffic violations, and improving the notification and chalan management features.

---

### 👨‍💻 About the Project

This project was developed as a **student learning project** to gain practical experience in Python, computer vision, AI, databases, and application development.

