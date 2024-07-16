import pandas as pd
import numpy as np

def load_and_process_data():
    # Load student details
    students_df = pd.read_csv('data/Student Details - Sheet1.csv')
    
    # Load feedback data
    feedback_df = pd.read_csv('data/Feedback data - Sheet1.csv', index_col=0)
    
    # Remove the 'Student Total' column
    feedback_df = feedback_df.drop('Student Total', axis=1)
    
    # Melt the dataframe
    feedback_long = feedback_df.reset_index().melt(id_vars='index', var_name='Name', value_name='Rating')
    feedback_long = feedback_long.rename(columns={'index': 'Item'})
    
    # Remove rows with '-' ratings and convert Rating to numeric
    feedback_long = feedback_long[feedback_long['Rating'] != '-']
    feedback_long['Rating'] = pd.to_numeric(feedback_long['Rating'], errors='coerce')
    feedback_long = feedback_long.dropna(subset=['Rating'])
    
    # Create a 'Category' column based on the 'Item'
    category_mapping = {
        'Scratch': 'Lessons', 'Robotics': 'Lessons', 'Python': 'Lessons', 
        'Design': 'Lessons', 'Roblox': 'Lessons', 'Board Games and LEGO': 'Lessons', 
        'Minecraft': 'Lessons', 'TGIF': 'Food', 'Shakey\'s': 'Food', 
        'Wraps': 'Food', 'Onigiri and Yakitori': 'Food', 'Dominos': 'Food', 
        'Disney Meal': 'Food', 'Snacks': 'Food', 'Ferris wheel': 'Activities', 
        'Disney': 'Activities', 'Boat Trip': 'Activities'
    }
    feedback_long['Category'] = feedback_long['Item'].map(category_mapping)
    
    # Merge student details with feedback data
    merged_df = pd.merge(feedback_long, students_df, on='Name', how='left')
    
    # Create lists of lessons, activities, and food items
    lessons = feedback_long[feedback_long['Category'] == 'Lessons']['Item'].unique().tolist()
    activities = feedback_long[feedback_long['Category'] == 'Activities']['Item'].unique().tolist()
    food_items = feedback_long[feedback_long['Category'] == 'Food']['Item'].unique().tolist()
    
    return merged_df, lessons, activities, food_items

# Load data
df, lessons, activities, food_items = load_and_process_data()

# Print some information about the loaded data
print("Data shape:", df.shape)
print("Lessons:", lessons)
print("Activities:", activities)
print("Food items:", food_items)