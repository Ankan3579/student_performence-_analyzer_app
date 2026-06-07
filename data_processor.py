import pandas as pd
import numpy as np
from pathlib import Path
import os
import time

class StudentDataProcessor:
    """Handle student data processing with Pandas and NumPy"""
    
    def __init__(self):
        self.df = None
        # Use absolute path to avoid connection issues after restart
        current_dir = Path(__file__).resolve().parent
        self.data_path = current_dir / 'student_data.csv'
        self.max_retries = 3
        self.retry_delay = 1
    
    def load_data(self):
        """Load student data from CSV with retry logic"""
        for attempt in range(self.max_retries):
            try:
                if self.data_path.exists():
                    self.df = pd.read_csv(self.data_path)
                    return self.df
                else:
                    # Create sample data if file doesn't exist
                    return self.create_sample_data()
            except (FileNotFoundError, pd.errors.ParserError) as e:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                    continue
                else:
                    # Fall back to sample data after all retries fail
                    return self.create_sample_data()
            except Exception as e:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                    continue
                else:
                    raise
    
    def create_sample_data(self):
        """Create sample student data"""
        np.random.seed(42)
        n_students = 100
        
        data = {
            'StudentID': range(1001, 1001 + n_students),
            'Name': [f'Student_{i}' for i in range(1, n_students + 1)],
            'Math': np.random.randint(40, 100, n_students),
            'Science': np.random.randint(40, 100, n_students),
            'English': np.random.randint(40, 100, n_students),
            'History': np.random.randint(40, 100, n_students),
            'AttendanceRate': np.random.uniform(60, 100, n_students),
            'StudyHours': np.random.uniform(2, 10, n_students),
            'ParticipationScore': np.random.uniform(40, 100, n_students)
        }
        
        self.df = pd.DataFrame(data)
        # Save sample data with retry logic
        for attempt in range(self.max_retries):
            try:
                self.df.to_csv(self.data_path, index=False)
                break
            except (IOError, OSError) as e:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    # Data in memory is still usable even if save fails
                    pass
        return self.df
    
    def calculate_overall_gpa(self):
        """Calculate overall GPA for each student"""
        if self.df is None:
            self.load_data()
        
        subject_cols = ['Math', 'Science', 'English', 'History']
        self.df['Overall_GPA'] = self.df[subject_cols].mean(axis=1)
        return self.df['Overall_GPA']
    
    def get_student_statistics(self):
        """Get statistical summary of student performance"""
        if self.df is None:
            self.load_data()
        
        subject_cols = ['Math', 'Science', 'English', 'History']
        stats = {
            'Mean': self.df[subject_cols].mean(),
            'Median': self.df[subject_cols].median(),
            'Std Dev': self.df[subject_cols].std(),
            'Min': self.df[subject_cols].min(),
            'Max': self.df[subject_cols].max()
        }
        return pd.DataFrame(stats)
    
    def categorize_performance(self):
        """Categorize students as High, Medium, or Low performers"""
        if self.df is None:
            self.load_data()
        
        self.calculate_overall_gpa()
        
        def categorize(gpa):
            if gpa >= 75:
                return 'High Performer'
            elif gpa >= 60:
                return 'Medium Performer'
            else:
                return 'Low Performer'
        
        self.df['Performance_Category'] = self.df['Overall_GPA'].apply(categorize)
        return self.df[['StudentID', 'Name', 'Overall_GPA', 'Performance_Category']]
    
    def get_top_performers(self, n=10):
        """Get top N performers"""
        if self.df is None:
            self.load_data()
        
        self.calculate_overall_gpa()
        return self.df.nlargest(n, 'Overall_GPA')[['StudentID', 'Name', 'Overall_GPA']]
    
    def get_subjects_analysis(self):
        """Analyze performance across subjects"""
        if self.df is None:
            self.load_data()
        
        subject_cols = ['Math', 'Science', 'English', 'History']
        return self.df[subject_cols].describe()
    
    def prepare_ml_features(self):
        """Prepare features for machine learning models"""
        if self.df is None:
            self.load_data()
        
        subject_cols = ['Math', 'Science', 'English', 'History']
        
        # Features
        X = self.df[['AttendanceRate', 'StudyHours', 'ParticipationScore'] + subject_cols].values
        
        # Target (Overall Performance Category)
        self.calculate_overall_gpa()
        y = (self.df['Overall_GPA'] >= 75).astype(int)  # 1 for high performer, 0 for others
        
        return X, y
