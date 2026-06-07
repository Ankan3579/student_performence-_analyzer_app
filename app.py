import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from data_processor import StudentDataProcessor
from ml_models import PerformancePredictor, PerformanceTrendAnalyzer

# Page configuration
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better visibility
st.markdown("""
    <style>
    /* Main content area */
    .main {
        padding: 1rem;
    }
    
    /* Improve visibility of headers */
    h1, h2, h3 {
        color: #1f77b4;
        margin-top: 1.5rem;
    }
    
    /* Metric styling */
    [data-testid="metric-container"] {
        background-color: #ffffff;
        border: 2px solid #e0e0e0;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Dataframe styling */
    [data-testid="stDataFrame"] {
        font-size: 14px;
    }
    
    /* Improve button visibility */
    .stButton > button {
        width: 100%;
        padding: 0.5rem 1rem;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state with error handling
try:
    if 'processor' not in st.session_state:
        st.session_state.processor = StudentDataProcessor()
        st.session_state.processor.load_data()
    if 'last_refresh' not in st.session_state:
        st.session_state.last_refresh = pd.Timestamp.now()

    if 'predictor' not in st.session_state:
        st.session_state.predictor = PerformancePredictor()
        st.session_state.predictor.prepare_data()
        st.session_state.predictor.train_random_forest()
except Exception as e:
    st.error(f"⚠️ Connection Error: {str(e)}")
    st.info("The application is recovering. Please wait or refresh the page.")
    # Create minimal processor with sample data as fallback
    st.session_state.processor = StudentDataProcessor()
    st.session_state.processor.load_data()
    st.session_state.last_refresh = pd.Timestamp.now()

# Auto-refresh data every 30 seconds with error handling
try:
    if pd.Timestamp.now() - st.session_state.last_refresh > pd.Timedelta(seconds=30):
        st.session_state.processor.load_data()
        st.session_state.last_refresh = pd.Timestamp.now()
except Exception as e:
    pass  # Silently skip refresh on error

# Add refresh button in sidebar
if st.sidebar.button("🔄 Refresh Data"):
    try:
        st.session_state.processor.load_data()
        st.session_state.last_refresh = pd.Timestamp.now()
        st.rerun()
    except Exception as e:
        st.error(f"Failed to refresh data: {str(e)}")

# Sidebar navigation
st.sidebar.title("🎓 Student Performance System")
page = st.sidebar.radio("Select Page:", [
    "Dashboard",
    "Analytics",
    "Performance Prediction",
    "At-Risk Students",
    "Feature Importance"
])

# Main title
st.title("📊 Student Performance Dashboard")

# ==================== DASHBOARD PAGE ====================
if page == "Dashboard":
    st.header("Overall Performance Overview")
    
    # Load data
    df = st.session_state.processor.df
    st.session_state.processor.calculate_overall_gpa()
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📚 Total Students", len(df))
    
    with col2:
        avg_gpa = df['Overall_GPA'].mean()
        st.metric("📊 Average GPA", f"{avg_gpa:.2f}")
    
    with col3:
        high_performers = len(df[df['Overall_GPA'] >= 75])
        st.metric("⭐ High Performers", high_performers)
    
    with col4:
        attendance_avg = df['AttendanceRate'].mean()
        st.metric("✓ Avg Attendance", f"{attendance_avg:.1f}%")
    
    st.divider()
    
    # Top performers
    st.subheader("🏆 Top 10 Performers")
    top_performers = st.session_state.processor.get_top_performers(10)
    st.dataframe(top_performers, width='stretch', hide_index=True)
    
    # Subject-wise performance
    st.subheader("📈 Performance by Subject")
    subject_cols = ['Math', 'Science', 'English', 'History']
    
    # Create subject averages
    subject_data = {
        'Subject': subject_cols,
        'Average': [df[col].mean() for col in subject_cols],
        'Min': [df[col].min() for col in subject_cols],
        'Max': [df[col].max() for col in subject_cols]
    }
    subject_df = pd.DataFrame(subject_data)
    
    fig = go.Figure(data=[
        go.Bar(x=subject_data['Subject'], y=subject_data['Average'], name='Average', marker_color='#3498db'),
        go.Bar(x=subject_data['Subject'], y=subject_data['Min'], name='Minimum', marker_color='#e74c3c'),
        go.Bar(x=subject_data['Subject'], y=subject_data['Max'], name='Maximum', marker_color='#2ecc71')
    ])
    
    fig.update_layout(
        title="Subject-wise Performance Statistics",
        xaxis_title="Subjects",
        yaxis_title="Scores",
        barmode="group",
        height=400,
        hovermode='x unified'
    )
    st.plotly_chart(fig, width='stretch')
    
    # Performance distribution
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("GPA Distribution")
        fig_gpa = go.Figure(data=[go.Histogram(
            x=df['Overall_GPA'],
            nbinsx=20,
            marker_color='#3498db'
        )])
        fig_gpa.update_layout(
            xaxis_title="GPA",
            yaxis_title="Number of Students",
            height=400
        )
        st.plotly_chart(fig_gpa, width='stretch')
    
    with col2:
        st.subheader("Performance Categories")
        categories = st.session_state.processor.categorize_performance()['Performance_Category'].value_counts()
        fig_pie = go.Figure(data=[go.Pie(
            labels=categories.index,
            values=categories.values,
            hole=0.3
        )])
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, width='stretch')


# ==================== ANALYTICS PAGE ====================
elif page == "Analytics":
    st.header("📊 Detailed Analytics")
    
    df = st.session_state.processor.df
    
    # Statistics table
    st.subheader("Statistical Summary")
    stats = st.session_state.processor.get_student_statistics()
    st.dataframe(stats.T, width='stretch', hide_index=True)
    
    st.divider()
    
    # Attendance vs Performance
    st.subheader("Attendance vs Performance Analysis")
    st.session_state.processor.calculate_overall_gpa()
    
    fig_scatter = px.scatter(
        df,
        x='AttendanceRate',
        y='Overall_GPA',
        size='StudyHours',
        hover_data=['Name'],
        title='Attendance Rate vs Overall GPA',
        labels={'AttendanceRate': 'Attendance Rate (%)', 'Overall_GPA': 'Overall GPA'},
        height=450
    )
    fig_scatter.update_traces(marker=dict(size=10, opacity=0.7))
    st.plotly_chart(fig_scatter, width='stretch')
    
    st.divider()
    
    # Study hours vs performance
    st.subheader("Study Hours vs Performance Analysis")
    fig_study = px.scatter(
        df,
        x='StudyHours',
        y='Overall_GPA',
        color='ParticipationScore',
        title='Study Hours vs Overall GPA',
        labels={'StudyHours': 'Study Hours', 'Overall_GPA': 'Overall GPA', 'ParticipationScore': 'Participation'},
        height=450
    )
    fig_study.update_traces(marker=dict(size=10, opacity=0.7))
    st.plotly_chart(fig_study, width='stretch')
    
    st.divider()
    
    # Correlation heatmap
    st.subheader("Feature Correlation Analysis")
    correlation_cols = ['Math', 'Science', 'English', 'History', 'AttendanceRate', 'StudyHours', 'ParticipationScore']
    corr_matrix = df[correlation_cols].corr()
    
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=correlation_cols,
        y=correlation_cols,
        colorscale='RdBu',
        zmid=0,
        text=corr_matrix.values.round(2),
        texttemplate='%{text}',
        textfont={"size": 10}
    ))
    fig_heatmap.update_layout(height=600, width=800)
    st.plotly_chart(fig_heatmap, width='stretch')
    
    with st.expander("📖 About This Analysis", expanded=False):
        st.markdown("""
        - **Scatter plots** show relationships between variables
        - **Bubble size** represents study hours
        - **Color intensity** shows participation scores
        - **Heatmap** shows correlations between all features
        """)


# ==================== PERFORMANCE PREDICTION PAGE ====================
elif page == "Performance Prediction":
    st.header("🤖 Predict Student Performance")
    
    tab1, tab2 = st.tabs(["📝 Single Student", "📊 Bulk Prediction"])
    
    with tab1:
        st.subheader("Predict Performance for a New Student")
        
        with st.form("prediction_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**📋 Student Metrics:**")
                attendance = st.slider("Attendance Rate (%)", 0.0, 100.0, 75.0, step=1.0)
                study_hours = st.slider("Study Hours per week", 0.0, 20.0, 5.0, step=0.5)
                participation = st.slider("Participation Score", 0.0, 100.0, 70.0, step=1.0)
            
            with col2:
                st.write("**📚 Subject Scores:**")
                math = st.slider("Math Score", 0, 100, 75, step=1)
                science = st.slider("Science Score", 0, 100, 75, step=1)
                english = st.slider("English Score", 0, 100, 75, step=1)
                history = st.slider("History Score", 0, 100, 75, step=1)
            
            submitted = st.form_submit_button("🔮 Predict Performance", use_container_width=True)
        
        if submitted:
            student_data = [attendance, study_hours, participation, math, science, english, history]
            predictor = st.session_state.predictor
            
            result = predictor.predict_performance(student_data)
            
            st.divider()
            
            # Display prediction results
            col1, col2, col3 = st.columns(3)
            with col1:
                if result['prediction'] == 'High Performer':
                    st.success(f"✅ {result['prediction']}")
                else:
                    st.warning(f"⚠️ {result['prediction']}")
            
            with col2:
                st.info(f"📊 Confidence: {result['confidence']:.1f}%")
            
            with col3:
                prob_high = result['probability'][1] * 100
                st.metric("Success Rate", f"{prob_high:.1f}%")
            
            st.divider()
            
            # Probability visualization
            fig_prob = go.Figure(data=[
                go.Bar(
                    x=['Not High\nPerformer', 'High\nPerformer'],
                    y=result['probability'] * 100,
                    marker_color=['#e74c3c', '#2ecc71'],
                    text=[f"{p:.1f}%" for p in result['probability'] * 100],
                    textposition='outside'
                )
            ])
            fig_prob.update_layout(
                title="Prediction Probability Distribution",
                yaxis_title="Probability (%)",
                xaxis_title="Prediction Category",
                height=400,
                showlegend=False
            )
            st.plotly_chart(fig_prob, width='stretch')
    
    with tab2:
        st.subheader("Bulk Prediction for All Students")
        st.write("Run predictions for all students in the database at once.")
        
        df = st.session_state.processor.df
        st.session_state.processor.calculate_overall_gpa()
        
        # Prepare data for all students
        subject_cols = ['Math', 'Science', 'English', 'History']
        students_data = df[['AttendanceRate', 'StudyHours', 'ParticipationScore'] + subject_cols].values.tolist()
        
        if st.button("🔮 Predict for All Students", use_container_width=True):
            with st.spinner("🔄 Running predictions..."):
                predictions = st.session_state.predictor.predict_multiple_students(students_data)
                
                # Add predictions to dataframe
                df['ML_Prediction'] = [p['prediction'] for p in predictions]
                df['ML_Confidence'] = [p['confidence'] for p in predictions]
                
                # Display results
                display_df = df[['StudentID', 'Name', 'Overall_GPA', 'ML_Prediction', 'ML_Confidence']].copy()
                display_df['ML_Confidence'] = display_df['ML_Confidence'].apply(lambda x: f"{x:.1f}%")
                display_df.columns = ['ID', 'Name', 'GPA', 'Prediction', 'Confidence']
                
                st.dataframe(display_df, width='stretch', hide_index=True)
                
                st.divider()
                
                # Model metrics
                st.subheader("🎯 Model Performance Metrics")
                metrics = st.session_state.predictor.evaluate_model()
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Accuracy", f"{metrics['accuracy']:.2%}")
            with col2:
                st.metric("Precision", f"{metrics['precision']:.2%}")
            with col3:
                st.metric("Recall", f"{metrics['recall']:.2%}")
            with col4:
                st.metric("F1-Score", f"{metrics['f1']:.2%}")


# ==================== AT-RISK STUDENTS PAGE ====================
elif page == "At-Risk Students":
    st.header("⚠️ At-Risk Students Analysis")
    
    df = st.session_state.processor.df
    
    # Select risk threshold
    col1, col2 = st.columns([2, 1])
    with col1:
        threshold = st.slider("Performance Threshold", 30, 70, 50, help="Students below this score in any subject are flagged as at-risk")
    with col2:
        st.metric("Threshold", f"{threshold}/100")
    
    st.divider()
    
    # Identify at-risk students
    analyzer = PerformanceTrendAnalyzer()
    at_risk = analyzer.identify_at_risk_students(df, threshold)
    
    # At-risk summary
    if len(at_risk) > 0:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("At-Risk Students", len(at_risk))
        with col2:
            pct = (len(at_risk) / len(df)) * 100
            st.metric("Percentage", f"{pct:.1f}%")
        with col3:
            st.metric("Total Students", len(df))
        
        st.divider()
        
        st.subheader(f"📋 Students Below {threshold} in Any Subject")
        at_risk_display = at_risk.reset_index(drop=True)
        st.dataframe(at_risk_display, width='stretch', hide_index=True)
        
        st.divider()
        
        # Visualization
        at_risk_melted = at_risk.melt(
            id_vars=['StudentID', 'Name'],
            value_vars=['Math', 'Science', 'English', 'History'],
            var_name='Subject',
            value_name='Score'
        )
        
        fig = px.bar(
            at_risk_melted,
            x='Name',
            y='Score',
            color='Subject',
            title=f"At-Risk Students Performance (Below {threshold})",
            barmode='group',
            height=450,
            color_discrete_sequence=['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
        )
        fig.add_hline(y=threshold, line_dash="dash", line_color="red", annotation_text=f"Threshold: {threshold}")
        st.plotly_chart(fig, width='stretch')
    else:
        st.success("✅ No at-risk students found!")
    
    st.divider()
    
    # Improvement potential
    st.subheader("🚀 Students with Improvement Potential")
    st.write("Students who study a lot but have lower scores - they may need different learning strategies")
    improvement = analyzer.calculate_improvement_potential(df)
    improvement_top = improvement.head(10).reset_index(drop=True)
    
    st.dataframe(improvement_top, width='stretch', hide_index=True)


# ==================== FEATURE IMPORTANCE PAGE ====================
elif page == "Feature Importance":
    st.header("🔍 Model Feature Importance Analysis")
    
    st.write("This shows which factors most influence the prediction of high-performing students.")
    
    st.divider()
    
    predictor = st.session_state.predictor
    feature_importance = predictor.get_feature_importance()
    
    fig = go.Figure(data=[
        go.Bar(
            y=feature_importance['features'],
            x=feature_importance['importances'],
            orientation='h',
            marker=dict(
                color=feature_importance['importances'],
                colorscale='Viridis',
                showscale=True
            ),
            text=[f"{imp:.4f}" for imp in feature_importance['importances']],
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title="Feature Importance in Performance Prediction Model",
        xaxis_title="Importance Score",
        yaxis_title="Features",
        height=500,
        showlegend=False,
        margin=dict(l=200)
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.divider()
    
    # Detailed explanation
    st.subheader("📖 What This Means")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        **Feature Importance Explained:**
        - **Higher scores** = More influential factor
        - Shows which variables the ML model relies on most
        - Based on Random Forest algorithm
        - Helps identify key success factors
        """)
    
    with col2:
        st.markdown("""
        **Top Influencing Factors:**
        - Subject scores (Math, Science, English, History)
        - Attendance rate
        - Study hours per week
        - Class participation score
        """)

# Footer
st.divider()
st.markdown("""
    <div style="text-align: center; color: #666666; margin-top: 3rem; padding: 2rem;">
        <h4>Student Performance Dashboard</h4>
        <p>📊 Powered by Python | Streamlit | Pandas | NumPy | Scikit-learn</p>
        <p style="font-size: 12px; margin-top: 1rem;">Machine Learning Algorithm: Random Forest Classifier</p>
    </div>
""", unsafe_allow_html=True)
