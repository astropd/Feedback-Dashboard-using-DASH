import pandas as pd
import numpy as np

def load_and_process_data():
    # Load student details
    students_df = pd.read_csv('data/Student Details - Sheet1.csv')
    
    # Load feedback data
    feedback_df = pd.read_csv('data/Summer 2024 Camps Feedback - TCC - Tokyo 2.csv', header=1)
    
    # Melt the feedback dataframe to long format
    feedback_long = pd.melt(feedback_df, id_vars=['Unnamed: 0', 'Unnamed: 1'], 
                            var_name='Name', value_name='Rating')
    
    # Rename columns
    feedback_long = feedback_long.rename(columns={'Unnamed: 0': 'Category', 'Unnamed: 1': 'Item'})
    
    # Remove rows with NaN ratings
    feedback_long = feedback_long.dropna(subset=['Rating'])
    
    # Merge student details with feedback data
    merged_df = pd.merge(feedback_long, students_df, on='Name', how='left')
    
    # Create lists of lessons, activities, and food items
    lessons = feedback_long[feedback_long['Category'] == 'Lessons']['Item'].unique().tolist()
    activities = feedback_long[feedback_long['Category'] == 'Activities']['Item'].unique().tolist()
    food_items = feedback_long[feedback_long['Category'] == 'Food']['Item'].unique().tolist()
    
    return merged_df, lessons, activities, food_items

# Load data
df, lessons, activities, food_items = load_and_process_data()