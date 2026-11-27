# 📊 Student Performance Analyzer
### AI-Based Student Performance Evaluation & Prediction System

An interactive, machine learning-powered web application designed to analyze, visualize, and predict student academic performance.

The **Student Performance Analyzer** is a comprehensive educational analytics system built using Python, Streamlit, Pandas, NumPy, and Scikit-learn. It provides meaningful insights into students' academic performance by analyzing factors such as subject scores, attendance, study hours, and classroom participation.

The application uses a **Random Forest Classifier** to predict student performance and identify students who may be at risk of poor academic outcomes.

It combines data analytics, machine learning, and interactive visualizations into a single platform to support data-driven educational decision-making.

---

## 🚀 Project Highlights

- 📊 Interactive academic performance dashboard.
- 🤖 Machine Learning-based performance prediction.
- 📈 Detailed statistical analysis and visualization.
- 🎯 Identification of at-risk students.
- 🔍 Feature importance and model explainability.
- 👨‍🎓 Individual and bulk student predictions.
- 📉 Attendance, study hours, and academic performance analysis.

---

## 🎯 Key Features

### 1. 📊 Interactive Dashboard

Provides an overall overview of student academic performance.

- Total number of students.
- Average GPA.
- Overall attendance metrics.
- Top 10 student performers.
- Subject-wise performance analysis.
- GPA distribution histogram.
- Performance category distribution using pie charts.

### 2. 📈 Academic Analytics

Provides detailed statistical analysis to understand academic performance patterns.

- Statistical summaries of student data.
- Attendance vs. performance correlation.
- Study hours vs. academic performance analysis.
- Feature correlation heatmap.
- Academic performance trend analysis.
- Identification of important performance patterns.

### 3. 🤖 Performance Prediction

Uses a trained Random Forest Classifier to predict student performance.

**Single Student Prediction**
- Predict an individual student's performance.
- Analyze academic and behavioral features.
- Display prediction results.
- Show prediction confidence and probability visualization.

**Bulk Student Prediction**
- Predict performance for multiple students simultaneously.
- Analyze the entire student dataset.
- Identify high-performing and potentially struggling students.

**Machine Learning Model**
- Random Forest Classifier.
- 80:20 train-test split.
- Performance evaluation using standard classification metrics.

### 4. ⚠️ At-Risk Student Identification

Helps identify students who may need additional academic support.

- Identify students below the defined performance threshold.
- Analyze academic weaknesses.
- Evaluate improvement potential.
- Visualize at-risk students.
- Support early academic intervention.

### 5. 🔍 Feature Importance & Model Explainability

Helps understand which factors influence student performance predictions.

- Feature importance analysis.
- Identify influential academic factors.
- Analyze the contribution of attendance, study hours, participation, and subject scores.
- Visualize feature importance using charts.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python 3.8+ |
| Frontend / Web Framework | Streamlit |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| ML Algorithm | Random Forest Classifier |
| Interactive Visualization | Plotly |
| Statistical Visualization | Seaborn, Matplotlib |
| Development Environment | VS Code |
| Version Control | Git, GitHub |

---

## 🏗️ System Architecture

The application follows a structured data processing and machine learning workflow.

```text
          Student Dataset
                 |
                 v
          Data Processing
           Pandas / NumPy
                 |
                 v
        Exploratory Data Analysis
                 |
                 v
         Feature Engineering
                 |
                 v
         Random Forest Model
                 |
          +------+------+
          |             |
          v             v
     Prediction     Evaluation
          |             |
          +------+------+
                 |
                 v
         Performance Analysis
                 |
                 v
        Interactive Dashboard
              Streamlit
                 |
                 v
             End User
```

---

## 📂 Project Structure

```text
student_performence-_analyzer_app/
│
├── app.py                  # Main Streamlit application
│
├── data_processor.py       # Data processing and analysis
│
├── ml_models.py            # Machine Learning model implementation
│
├── requirements.txt        # Project dependencies
│
├── student_data.csv        # Sample student dataset
│
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

Follow these instructions to run the project locally.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Ankan3579/student_performence-_analyzer_app.git
```

### 2. Navigate to the Project Directory

```bash
cd student_performence-_analyzer_app
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📊 Dataset Description

The application uses student academic records containing the following features:

| Feature | Description |
|---|---|
| StudentID | Unique student identifier |
| Name | Student name |
| Math | Mathematics score (0–100) |
| Science | Science score (0–100) |
| English | English score (0–100) |
| History | History score (0–100) |
| AttendanceRate | Student attendance percentage |
| StudyHours | Weekly study hours |
| ParticipationScore | Classroom participation score |

**Automatic Dataset Generation:**

If `student_data.csv` is not available, the system automatically generates sample student data.

Users can also customize the dataset to analyze different student records.

---

## 🧠 Machine Learning Implementation

### Algorithm: Random Forest Classifier

The project uses the Random Forest Classification algorithm to predict whether a student belongs to the High Performer category.

**Prediction Objective:**

```text
High Performer: GPA >= 75
```

### Features Used

The model considers seven input features:

1. Mathematics Score
2. Science Score
3. English Score
4. History Score
5. Attendance Rate
6. Study Hours
7. Participation Score

### Model Training

- Algorithm: Random Forest Classifier.
- Training Data: 80%.
- Testing Data: 20%.
- Task: Binary Classification.
- Target: High Performer / Not High Performer.

### Model Evaluation Metrics

The model is evaluated using the following metrics:

| Metric | Description |
|---|---|
| Accuracy | Measures the overall correctness of predictions. |
| Precision | Measures how many predicted high performers are actually high performers. |
| Recall | Measures how many actual high performers are correctly identified. |
| F1-Score | Harmonic mean of precision and recall. |

---

## 📉 Data Analytics & Visualization

The application provides several interactive visualizations:

| Visualization | Purpose |
|---|---|
| Bar Chart | Subject-wise performance comparison |
| Histogram | GPA distribution analysis |
| Pie Chart | Student performance category distribution |
| Scatter Plot | Attendance and study hours correlation analysis |
| Heatmap | Feature correlation analysis |
| Feature Importance Chart | Identifies important prediction features |

These visualizations help users understand academic patterns and relationships between different performance factors.

---

## 💡 Real-World Use Cases

1. **Educational Institutions:** Monitor overall academic performance.
2. **Teachers:** Identify students who require additional academic support.
3. **Students:** Understand academic strengths and weaknesses.
4. **Parents:** Monitor student academic progress.
5. **Educational Researchers:** Analyze relationships between academic and behavioral factors.
6. **Academic Administrators:** Support data-driven educational decisions.

---

## 🔄 Application Workflow

1. **Data Input:** Load existing student data or generate sample records.
2. **Data Processing:** Clean, transform, and process data using Pandas and NumPy.
3. **Data Analysis:** Generate statistical insights and visualizations.
4. **Model Training:** Train the Random Forest Classifier.
5. **Model Evaluation:** Evaluate performance using classification metrics.
6. **Prediction:** Generate individual or bulk student performance predictions.
7. **Visualization:** Display analytical results through the Streamlit dashboard.
8. **At-Risk Identification:** Identify students who may need academic intervention.

---

## 📝 Example Prediction

**Sample Input:**

| Feature | Value |
|---|---:|
| Attendance | 85% |
| Study Hours | 6 hours/week |
| Participation Score | 80 |
| Mathematics | 85 |
| Science | 88 |
| English | 82 |
| History | 80 |

**Illustrative Output:**

```text
Prediction: High Performer

Confidence: 92.5%
```

*Note: This is an illustrative example. Actual prediction results and confidence scores depend on the trained model and dataset.*

---

## 🔧 Customization

The application can be extended or modified through its modular structure.

**Adding New Features**

Modify `data_processor.py` to introduce additional calculated fields or data processing operations.

**Modifying the ML Model**

Update the `train_random_forest()` method in `ml_models.py` to modify the Random Forest model configuration.

**Changing Performance Thresholds**

Modify the performance classification thresholds and at-risk student identification logic.

**Updating the Dataset**

Replace or modify `student_data.csv` with your own student academic records using the supported data format.

---

## 🐛 Troubleshooting

**Issue: Module Not Found**

Solution:

```bash
pip install -r requirements.txt
```

**Issue: Port Already in Use**

Solution:

```bash
streamlit run app.py --server.port 8502
```

**Issue: Dataset Not Found**

Solution:

The application automatically generates sample data if `student_data.csv` is unavailable. Check project directory permissions if generation fails.

---

## 📚 Dependencies

| Package | Version | Purpose |
|---|---|---|
| Streamlit | 1.28.1 | Web application framework |
| Pandas | 2.0.3 | Data processing |
| NumPy | 1.24.3 | Numerical computing |
| Scikit-learn | 1.3.1 | Machine Learning |
| Plotly | 5.17.0 | Interactive visualization |
| Matplotlib | 3.7.2 | Data visualization |
| Seaborn | 0.12.2 | Statistical visualization |

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Data manipulation using Pandas and NumPy.
- Exploratory Data Analysis (EDA).
- Machine Learning model development.
- Random Forest Classification.
- Feature engineering.
- Model evaluation and performance metrics.
- Interactive dashboard development using Streamlit.
- Data visualization using Plotly, Matplotlib, and Seaborn.
- Building an end-to-end Machine Learning application.

---

## 🔮 Future Enhancements

- Integration of additional Machine Learning algorithms.
- Advanced student performance forecasting.
- Personalized academic improvement recommendations.
- Automated academic report generation.
- Improved model explainability using SHAP.
- Historical performance tracking.
- Database integration for persistent student records.
- Deployment with improved scalability.

---

## 👨‍💻 Author

**Ankan Paramanik**

AI Product Engineer | Machine Learning Enthusiast | Full Stack Developer

- GitHub: [Ankan3579](https://github.com/Ankan3579)

---

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

Feel free to fork the repository and submit pull requests.

---

⭐ If you find this project useful, consider giving it a star!

**Building intelligent solutions through Data Science and Machine Learning. 🚀**
 
