from dash import Input, Output
import plotly.express as px
import pandas as pd
from app import app
from data import df, lessons, activities, food_items

@app.callback(
    Output('average-ratings-chart', 'figure'),
    Input('average-ratings-chart', 'id')
)
def update_average_ratings_chart(_):
    avg_ratings = df[lessons + activities + food_items].mean().sort_values(ascending=False)
    fig = px.bar(x=avg_ratings.index, y=avg_ratings.values, 
                 labels={'x': 'Category', 'y': 'Average Rating'},
                 title='Average Ratings by Category')
    return fig

@app.callback(
    Output('demographic-chart', 'figure'),
    Input('demographic-dropdown', 'value')
)
def update_demographic_chart(demographic):
    if demographic == 'Age':
        age_groups = pd.cut(df['Age'], bins=[7, 10, 13, 16, 18], labels=['8-10', '11-13', '14-16', '17-18'])
        grouped_data = df.groupby(age_groups)[lessons + activities + food_items].mean().T
        fig = px.bar(grouped_data, barmode='group', 
                     labels={'value': 'Average Rating', 'variable': 'Age Group'},
                     title=f'Average Ratings by {demographic}')
    else:
        grouped_data = df.groupby(demographic)[lessons + activities + food_items].mean().T
        fig = px.bar(grouped_data, barmode='group', 
                     labels={'value': 'Average Rating', 'variable': demographic},
                     title=f'Average Ratings by {demographic}')
    return fig

@app.callback(
    Output('correlation-heatmap', 'figure'),
    Input('correlation-heatmap', 'id')
)
def update_correlation_heatmap(_):
    corr_matrix = df[lessons + activities + food_items].corr()
    fig = px.imshow(corr_matrix, text_auto=True, aspect="auto",
                    title='Correlation Heatmap of Ratings')
    return fig

@app.callback(
    Output('distribution-chart', 'figure'),
    Input('distribution-dropdown', 'value')
)
def update_distribution_chart(category):
    fig = px.histogram(df, x=category, nbins=5, 
                       labels={'count': 'Number of Students', category: 'Rating'},
                       title=f'Distribution of Ratings for {category}')
    return fig