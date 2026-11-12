🎓 ViharaTech – Student Performance Prediction System

A Machine Learning-based web application designed to predict student academic performance based on study habits, previous academic scores, sleep duration, extracurricular activities, and sample question papers practiced.

The system provides an interactive web dashboard where students can enter their academic details and receive an estimated performance index out of 100.

🚀 Project Overview

The Student Performance Prediction System uses Machine Learning techniques to estimate student academic performance based on various academic and lifestyle factors.

The application is developed using Python and Flask, with a modern, responsive frontend built using HTML and CSS.

The main objective of this project is to demonstrate how Machine Learning can be applied in the education sector to analyze student-related data and generate performance predictions.

✨ Key Features
Predicts student academic performance using Machine Learning.
User-friendly and responsive web dashboard.
Accepts multiple academic and lifestyle input features.
Displays predicted performance on a scale of 0–100.
Input validation and error handling.
Flask-based backend integration.
Modern dashboard interface.
Easy-to-use prediction system.
🛠️ Technologies Used
Technology	Purpose
Python	Programming language
Flask	Web application framework
Scikit-learn	Machine Learning
Pandas	Data processing
NumPy	Numerical operations
HTML5	Webpage structure
CSS3	Frontend styling
Pickle	Model serialization (if used)
📊 Input Features

The model considers the following features:

Feature	Description
Hours Studied	Number of hours spent studying
Previous Scores	Student's previous academic scores
Extracurricular Activities	Participation in extracurricular activities (Yes/No)
Sleep Hours	Average daily sleeping hours
Sample Question Papers	Number of practice question papers completed
🎯 Prediction Output

The system generates a Predicted Performance Index, represented as a numerical value out of 100.

This value provides an estimate of the student's academic performance based on the information provided.

📁 Project Structure
text
Student-Performance-Prediction/
│
├── app.py
│
├── model/
│   └── model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── dataset/
│   └── Student_Performance.csv
│
├── requirements.txt
│
└── README.md


Note: Update the structure according to your actual project files.

⚙️ Installation and Setup
1. Clone the Repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the Project Directory
bash
cd Student-Performance-Prediction

3. Create a Virtual Environment
bash
python -m venv venv


Activate the environment:

Windows:

bash
venv\Scripts\activate


Mac/Linux:

bash
source venv/bin/activate

4. Install Dependencies
bash
pip install -r requirements.txt

5. Run the Application
bash
python app.py

6. Open the Application

Visit the following URL in your browser:

text
http://127.0.0.1:5000/

🔍 How It Works
The student opens the ViharaTech web application.
The student enters the required academic and lifestyle information.
The submitted information is sent to the Flask backend.
The backend processes the input according to the trained model's requirements.
The Machine Learning model analyzes the input features.
The system generates the predicted performance index.
The prediction is displayed on the dashboard.
🧠 Machine Learning Workflow

The project follows these general Machine Learning stages:

Dataset Collection
Data Preprocessing
Feature Selection
Model Training
Model Evaluation
Model Saving
Flask Integration
Performance Prediction

The specific algorithm and evaluation metrics should be added based on the actual trained model.

🔮 Future Enhancements
Student performance history and tracking.
Graphical representation of academic performance.
Personalized study recommendations.
Downloadable prediction reports.
Integration of additional academic features.
Comparison of multiple Machine Learning algorithms.
Deployment on a cloud platform.
👨‍💻 Developer Information

Developed By: Vineeth Nihal K

Project Name: ViharaTech – Student Performance Prediction System

Domain: Machine Learning / Artificial Intelligence

Application Type: Web-Based Machine Learning Application

📝 Conclusion

The ViharaTech Student Performance Prediction System demonstrates the practical application of Machine Learning in the field of education. By analyzing important factors such as study hours, previous academic scores, sleep duration, extracurricular participation, and practice question papers, the system generates an estimated student performance index.

This project provides an interactive and user-friendly platform that demonstrates how data-driven technologies can support academic performance analysis. It also highlights the integration of Machine Learning models with web technologies using Python and Flask.

Through this project, we gain practical experience in data preprocessing, Machine Learning model integration, backend development, and frontend design. The system can be further enhanced by incorporating additional student-related parameters, advanced prediction algorithms, personalized recommendations, and performance visualization features.

In conclusion, ViharaTech aims to demonstrate how Machine Learning can contribute to smarter academic analysis and support students in understanding the factors associated with their academic performance. The predictions are estimates and should be used as supportive insights rather than definitive measures of a student's abilities or future academic results.

🙏 Acknowledgements

We acknowledge the developers and contributors of the open-source technologies and libraries used in this project, including Python, Flask, Pandas, NumPy, and Scikit-learn.

⭐ If you find this project useful or interesting, please consider giving the repository a star!
