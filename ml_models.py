import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from data_processor import StudentDataProcessor
import time

class PerformancePredictor:
    """Machine Learning models for student performance prediction"""
    
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.metrics = {}
        self.max_retries = 3
        self.retry_delay = 1
    
    def prepare_data(self):
        """Prepare and split data for training with retry logic"""
        for attempt in range(self.max_retries):
            try:
                processor = StudentDataProcessor()
                X, y = processor.prepare_ml_features()
                
                # Ensure we have enough data
                if len(X) < 10:
                    raise ValueError("Insufficient data for training")
                
                # Split data
                self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                    X, y, test_size=0.2, random_state=42
                )
                
                # Scale features
                self.X_train = self.scaler.fit_transform(self.X_train)
                self.X_test = self.scaler.transform(self.X_test)
                break
            except Exception as e:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    raise
    
    def train_random_forest(self, n_estimators=100):
        """Train Random Forest classifier with error handling"""
        for attempt in range(self.max_retries):
            try:
                if self.X_train is None:
                    self.prepare_data()
                
                self.model = RandomForestClassifier(
                    n_estimators=n_estimators,
                    max_depth=10,
                    min_samples_split=5,
                    random_state=42
                )
                
                self.model.fit(self.X_train, self.y_train)
                return self.model
            except Exception as e:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    raise
    
    def evaluate_model(self):
        """Evaluate model performance with error handling"""
        try:
            if self.model is None:
                self.train_random_forest()
            
            y_pred = self.model.predict(self.X_test)
            
            self.metrics = {
                'accuracy': accuracy_score(self.y_test, y_pred),
                'precision': precision_score(self.y_test, y_pred),
                'recall': recall_score(self.y_test, y_pred),
                'f1': f1_score(self.y_test, y_pred),
                'confusion_matrix': confusion_matrix(self.y_test, y_pred)
            }
            
            return self.metrics
        except Exception as e:
            # Return default metrics on error
            return {
                'accuracy': 0.0,
                'precision': 0.0,
                'recall': 0.0,
                'f1': 0.0,
                'confusion_matrix': None
            }
    
    def predict_performance(self, student_data):
        """Predict performance for a new student with error handling
        
        Args:
            student_data: list [attendance_rate, study_hours, participation_score, 
                               math, science, english, history]
        """
        try:
            if self.model is None:
                self.train_random_forest()
            
            # Scale input
            student_data = np.array(student_data).reshape(1, -1)
            student_data_scaled = self.scaler.transform(student_data)
            
            # Predict
            prediction = self.model.predict(student_data_scaled)[0]
            probability = self.model.predict_proba(student_data_scaled)[0]
            
            return {
                'prediction': 'High Performer' if prediction == 1 else 'Not High Performer',
                'confidence': max(probability) * 100,
                'probability': probability
            }
        except Exception as e:
            # Return default prediction on error
            return {
                'prediction': 'Unable to predict',
                'confidence': 0.0,
                'probability': [0.5, 0.5]
            }
    
    def get_feature_importance(self):
        """Get feature importance from the model with error handling"""
        try:
            if self.model is None:
                self.train_random_forest()
            
            feature_names = ['Attendance Rate', 'Study Hours', 'Participation Score',
                            'Math', 'Science', 'English', 'History']
            
            importances = self.model.feature_importances_
            indices = np.argsort(importances)[::-1]
            
            return {
                'features': [feature_names[i] for i in indices],
                'importances': importances[indices]
            }
        except Exception as e:
            # Return default feature importance on error
            feature_names = ['Attendance Rate', 'Study Hours', 'Participation Score',
                            'Math', 'Science', 'English', 'History']
            return {
                'features': feature_names,
                'importances': np.ones(len(feature_names)) / len(feature_names)
            }
    
    def predict_multiple_students(self, students_data_list):
        """Predict performance for multiple students"""
        results = []
        for student_data in students_data_list:
            result = self.predict_performance(student_data)
            results.append(result)
        return results


class PerformanceTrendAnalyzer:
    """Analyze trends in student performance"""
    
    @staticmethod
    def calculate_class_average_trend(df, subjects=['Math', 'Science', 'English', 'History']):
        """Calculate average scores by subject"""
        return df[subjects].mean()
    
    @staticmethod
    def identify_at_risk_students(df, threshold=50):
        """Identify students with scores below threshold"""
        subject_cols = ['Math', 'Science', 'English', 'History']
        at_risk = df[df[subject_cols].min(axis=1) < threshold]
        return at_risk[['StudentID', 'Name'] + subject_cols]
    
    @staticmethod
    def calculate_improvement_potential(df):
        """Analyze improvement potential based on study hours vs performance"""
        subject_cols = ['Math', 'Science', 'English', 'History']
        df['Avg_Score'] = df[subject_cols].mean(axis=1)
        
        # Students with high study hours but lower scores have improvement potential
        df['Improvement_Potential'] = df['StudyHours'] / (df['Avg_Score'] + 1)
        
        return df[['StudentID', 'Name', 'StudyHours', 'Avg_Score', 'Improvement_Potential']].sort_values(
            'Improvement_Potential', ascending=False
        )
