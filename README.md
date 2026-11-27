# 📊 Student Performance Analyzer — AI-Based Student Performance Evaluation & Prediction System

An interactive, machine learning-powered web application designed to analyze student academic performance, identify at-risk students, and predict future performance using academic scores, attendance, study hours, and participation data.

The system provides an analytical dashboard with visual insights, performance predictions, feature importance analysis, and student performance categorization through an interactive frontend built using HTML, CSS, and JavaScript.

## 📑 Table of Contents

- Project Overview
- Key Features
- System Architecture
- Dataset & Features
- Machine Learning Pipeline
- Data Processing & Analysis
- Model Training & Evaluation
- Performance Prediction
- Frontend Interface
- Project Structure
- Installation & Setup
- Future Enhancements

## 🔍 Project Overview

The objective of this project is to analyze student academic performance and understand how different academic and behavioral factors influence overall performance.

The system uses machine learning to classify students into performance categories based on their academic scores, attendance rate, weekly study hours, and participation score.

The complete workflow encompasses:

- Student dataset processing and exploratory data analysis.
- Academic performance analysis using statistical methods.
- Data preprocessing and feature engineering.
- Random Forest Classifier for student performance prediction.
- Identification of students who may be at academic risk.
- Feature importance analysis to understand important performance factors.
- Interactive web interface using HTML, CSS, and JavaScript.

## ✨ Key Features

**📊 Interactive Dashboard**

- Displays total students, average GPA, and attendance statistics.
- Shows top 10 performing students.
- Visualizes subject-wise academic performance.
- Displays GPA distribution and performance categories.

**📈 Academic Performance Analytics**

- Statistical summaries of student academic records.
- Attendance versus academic performance analysis.
- Study hours versus performance analysis.
- Feature correlation heatmap.
- Academic performance trend visualization.

**🤖 Machine Learning-Based Prediction**

- Random Forest Classifier for student performance classification.
- Supports individual student performance prediction.
- Supports bulk student performance prediction.
- Displays prediction confidence scores and probability visualizations.

**⚠️ At-Risk Student Identification**

- Identifies students performing below the defined performance threshold.
- Highlights students who may require additional academic support.
- Helps understand potential areas for improvement.

**🔎 Feature Importance & Explainability**

- Identifies important features influencing predictions.
- Visualizes feature importance.
- Helps understand the contribution of academic and behavioral factors.

## 🏗️ System Architecture

The application follows a frontend-to-Python-processing architecture.

```text
+-------------------------------------------------------------+
|                    Client Frontend                          |
|                                                             |
|  - HTML5 (Webpage Structure)                                |
|  - CSS3 (Responsive Styling and Dashboard UI)               |
|  - JavaScript (User Interaction and Dynamic Updates)       |
+------------------------------+------------------------------+
                               |
                               | User Input / Application Data
                               v
+-------------------------------------------------------------+
|                 Python Application Layer                    |
|                                                             |
|  - app.py                                                   |
|  - Application Logic                                        |
|  - Dashboard Data Integration                              |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    Data Processing Layer                    |
|                                                             |
|  - data_processor.py                                        |
|  - Pandas                                                   |
|  - NumPy                                                    |
|  - Data Cleaning and Feature Preparation                    |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                 Machine Learning Layer                      |
|                                                             |
|  - ml_models.py                                             |
|  - Scikit-Learn                                             |
|  - Random Forest Classifier                                 |
|  - Performance Prediction                                   |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                 Analytics & Visualization                   |
|                                                             |
|  - Student Performance Analysis                             |
|  - Feature Importance                                       |
|  - Performance Distribution                                 |
|  - At-Risk Student Identification                           |
+-------------------------------------------------------------+
```

## 📊 Dataset & Features

**Dataset File:** `student_data.csv`

The application uses student academic information to analyze and predict student performance.

If the dataset does not exist, the application can automatically generate sample student data.

### Dataset Attributes

| Feature Name | Type | Description |
|---|---|---|
| StudentID | Integer | Unique student identification |
| Name | Categorical | Student name |
| Math | Numerical | Mathematics examination score |
| Science | Numerical | Science examination score |
| English | Numerical | English examination score |
| History | Numerical | History examination score |
| AttendanceRate | Numerical | Student attendance percentage |
| StudyHours | Numerical | Weekly study hours |
| ParticipationScore | Numerical | Student participation score |

**Target Variable:** High Performer

The classification target is based on the academic performance threshold:

- High Performer: GPA ≥ 75
- Other students: GPA < 75

The model uses seven input features for classification.

## ⚙️ Machine Learning Pipeline

### 1. Data Processing

The data processing module handles student academic records before they are used for machine learning.

Main operations include:

- Loading student records.
- Checking dataset structure.
- Preparing numerical features.
- Processing academic performance attributes.
- Preparing data for model training and analysis.

### 2. Feature Selection

The model uses seven input features:

- Math
- Science
- English
- History
- AttendanceRate
- StudyHours
- ParticipationScore

These features represent academic achievement, attendance behavior, study habits, and classroom participation.

### 3. Model Training

The project uses the **Random Forest Classifier** for student performance classification.

Random Forest combines multiple decision trees to generate a classification result.

The model training process includes:

- Preparing input features (X).
- Preparing the target variable (y).
- Splitting the dataset into training and testing sets.
- Training the Random Forest Classifier.
- Evaluating model performance.

**Train-Test Split:**

- Training data: 80%
- Testing data: 20%

### 4. Model Evaluation

The classification model can be evaluated using the following metrics:

| Evaluation Metric | Purpose |
|---|---|
| Accuracy | Measures overall prediction correctness |
| Precision | Measures the correctness of positive predictions |
| Recall | Measures how many actual positive cases are identified |
| F1-Score | Balances precision and recall |

These metrics help evaluate how effectively the model classifies student performance.

### 5. Performance Prediction

The trained model predicts whether a student belongs to the High Performer category.

Example input:

```python
student_data = {
    "Math": 85,
    "Science": 88,
    "English": 82,
    "History": 80,
    "AttendanceRate": 85,
    "StudyHours": 6,
    "ParticipationScore": 80
}
```

Example output:

```text
Predicted Category: High Performer
Prediction Confidence: 92.5%
```

*Note: The confidence value is illustrative and not a guaranteed model result.*

## 📉 Data Analytics & Visualization

The application provides visual insights into student academic performance.

**Dashboard Analytics:**

- Total number of students.
- Average GPA.
- Average attendance.
- Top 10 student performers.
- Subject-wise performance distribution.
- GPA histogram.
- Performance category distribution.

**Performance Analysis:**

- Attendance versus performance.
- Study hours versus performance.
- Correlation heatmap.
- Statistical summaries.
- Academic performance patterns.

These visualizations help users understand relationships between student behavior and academic outcomes.

## 💻 Frontend Interface

The frontend is developed using **vanilla HTML5, CSS3, and JavaScript**.

### Technologies Used

| Technology | Purpose |
|---|---|
| HTML5 | Webpage structure and dashboard components |
| CSS3 | Styling, layouts, responsiveness, and visual design |
| JavaScript | User interactions and dynamic frontend behavior |

### Frontend Responsibilities

**Dashboard Interface**

Displays student statistics and academic performance information.

**Performance Analytics**

Presents charts and visual insights for understanding student performance.

**Prediction Interface**

Allows users to provide student academic information and view prediction results.

**At-Risk Student Section**

Displays students who may require additional academic attention.

**Feature Importance Visualization**

Helps users understand which academic factors influence model predictions.

## 📁 Project Structure

```text
student_performence-_analyzer_app/
│
├── frontend/
│   ├── index.html              # Main frontend webpage
│   ├── style.css               # Frontend styling
│   └── script.js               # JavaScript functionality
│
├── app.py                      # Main Python application
├── data_processor.py           # Data processing and preparation
├── ml_models.py                # Machine learning model implementation
│
├── student_data.csv            # Student dataset (auto-generated if absent)
├── requirements.txt             # Python dependencies
│
└── README.md                    # Project documentation
```

*Adjust the folder names above to match your actual repository structure.*

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8+
- Node.js is not required for vanilla HTML, CSS, and JavaScript.
- VS Code or another code editor.
- Modern web browser.

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd student_performence-_analyzer_app
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Python Application

```bash
python app.py
```

Use the appropriate command for your Python application's actual backend framework or server configuration.

### 5. Run the Frontend

Open the frontend folder in VS Code and launch `index.html` using the Live Server extension.

Alternatively, use Python's local HTTP server:

```bash
python -m http.server 5500
```

Open the following address in your browser:

```text
http://127.0.0.1:5500
```

*The frontend and Python application must be configured to communicate through the integration method used in your project.*

## 🔮 Future Enhancements

- Student performance prediction using additional machine learning algorithms.
- Personalized improvement recommendations.
- Advanced student progress tracking.
- Student-wise performance reports.
- Integration with a database for persistent student records.
- Improved frontend dashboard and interactive visualizations.
- Deployment as a complete web application.

## 🎯 Project Objective

The main objective of this project is to demonstrate how Machine Learning and web technologies can be combined to analyze student academic performance, predict performance categories, and identify students who may need additional academic support.

**Built with Python, Pandas, NumPy, Scikit-Learn, HTML, CSS, and JavaScript.**


 
