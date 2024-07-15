import pandas as pd
import numpy as np

def generate_dummy_data(n_students=200):
    np.random.seed(42)

    lessons = ['Math', 'Science', 'English', 'Art', 'Music']
    activities = ['Sports', 'Crafts', 'Games', 'Dance', 'Excursion']
    food_items = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']

    data = {
        'Age': np.random.randint(8, 18, n_students),
        'Gender': np.random.choice(['Male', 'Female'], n_students),
        'Nationality': np.random.choice(['USA', 'UK', 'Canada', 'Australia', 'Germany'], n_students)
    }

    for item in lessons + activities + food_items:
        data[item] = np.random.randint(1, 6, n_students)

    df = pd.DataFrame(data)
    return df, lessons, activities, food_items

# Generate data
df, lessons, activities, food_items = generate_dummy_data()