#!/usr/bin/env python3
"""
Startup verification script to test application connection after computer restart
Run this script to verify everything is working correctly before starting the Streamlit app.
"""

import sys
import time
from pathlib import Path

def test_data_processor():
    """Test StudentDataProcessor initialization and data loading"""
    print("Testing StudentDataProcessor...")
    try:
        from data_processor import StudentDataProcessor
        
        processor = StudentDataProcessor()
        print(f"  ✓ StudentDataProcessor initialized")
        print(f"  ✓ Data path: {processor.data_path}")
        
        df = processor.load_data()
        print(f"  ✓ Data loaded successfully")
        print(f"  ✓ Data shape: {df.shape}")
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def test_ml_models():
    """Test PerformancePredictor initialization and training"""
    print("\nTesting PerformancePredictor...")
    try:
        from ml_models import PerformancePredictor
        
        predictor = PerformancePredictor()
        print(f"  ✓ PerformancePredictor initialized")
        
        predictor.prepare_data()
        print(f"  ✓ Data prepared for training")
        
        predictor.train_random_forest()
        print(f"  ✓ Model trained successfully")
        
        metrics = predictor.evaluate_model()
        print(f"  ✓ Model evaluated - Accuracy: {metrics['accuracy']:.2f}")
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def test_streamlit_connection():
    """Test Streamlit app initialization"""
    print("\nTesting Streamlit app initialization...")
    try:
        import streamlit as st
        print(f"  ✓ Streamlit imported successfully")
        
        # Try basic Streamlit operations
        st.write("✓ Streamlit connection successful!")
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("APPLICATION STARTUP VERIFICATION")
    print("=" * 60)
    
    results = []
    
    # Test 1: Data Processor
    results.append(test_data_processor())
    time.sleep(1)
    
    # Test 2: ML Models
    results.append(test_ml_models())
    time.sleep(1)
    
    # Test 3: Streamlit (optional, shows message)
    print("\nStreamlit test (for reference):")
    print("  Note: Streamlit tests are shown in the browser, not in terminal")
    
    print("\n" + "=" * 60)
    if all(results):
        print("✓ ALL TESTS PASSED!")
        print("Your application is ready to run.")
        print("\nTo start the app, run: streamlit run app.py")
        print("=" * 60)
        return 0
    else:
        print("✗ SOME TESTS FAILED")
        print("Please check the errors above and ensure all dependencies are installed.")
        print("\nTo install dependencies, run: pip install -r requirements.txt")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
