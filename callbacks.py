from dash import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from app import app
from data import df, lessons, activities, food_items

@app.callback(
    Output('average-ratings-chart', 'figure'),
    Input('average-ratings-chart', 'id')
)
def update_average_ratings_chart(_):
    avg_ratings = df.groupby('Item')['Rating'].mean().sort_values(ascending=False)
    fig = px.bar(x=avg_ratings.index, y=avg_ratings.values, 
                 labels={'x': 'Item', 'y': 'Average Rating'},
                 title='Average Ratings by Item')
    return fig

@app.callback(
    Output('demographic-chart', 'figure'),
    Input('demographic-dropdown', 'value')
)
def update_demographic_chart(demographic):
    if demographic == 'Age':
        df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 8, 10, 12, 14], labels=['5-8', '9-10', '11-12', '13+'])
        grouped_data = df.groupby(['AgeGroup', 'Item'])['Rating'].mean().reset_index()
        fig = px.bar(grouped_data, x='Item', y='Rating', color='AgeGroup', barmode='group',
                     labels={'Rating': 'Average Rating'},
                     title=f'Average Ratings by Age Group')
    else:
        grouped_data = df.groupby([demographic, 'Item'])['Rating'].mean().reset_index()
        fig = px.bar(grouped_data, x='Item', y='Rating', color=demographic, barmode='group',
                     labels={'Rating': 'Average Rating'},
                     title=f'Average Ratings by {demographic}')
    return fig

@app.callback(
    Output('correlation-heatmap', 'figure'),
    Input('correlation-heatmap', 'id')
)
def update_correlation_heatmap(_):
    pivot_df = df.pivot_table(values='Rating', index='Name', columns='Item')
    corr_matrix = pivot_df.corr()
    fig = px.imshow(corr_matrix, text_auto=True, aspect="auto",
                    title='Correlation Heatmap of Ratings')
    return fig

@app.callback(
    Output('distribution-chart', 'figure'),
    Input('distribution-dropdown', 'value')
)
def update_distribution_chart(item):
    item_data = df[df['Item'] == item]
    fig = px.histogram(item_data, x='Rating', nbins=5, 
                       labels={'count': 'Number of Ratings', 'Rating': 'Rating'},
                       title=f'Distribution of Ratings for {item}')
    return fig