from dash import dcc, html
from data_generator import lessons, activities, food_items

def create_layout():
    return html.Div([
        html.H1("Student Feedback Dashboard"),
        
        dcc.Tabs([
            dcc.Tab(label="Overview", children=[
                html.Div([
                    html.H3("Average Ratings"),
                    dcc.Graph(id='average-ratings-chart')
                ])
            ]),
            dcc.Tab(label="Demographic Analysis", children=[
                html.Div([
                    html.H3("Ratings by Demographic"),
                    dcc.Dropdown(
                        id='demographic-dropdown',
                        options=[
                            {'label': 'Age', 'value': 'Age'},
                            {'label': 'Gender', 'value': 'Gender'},
                            {'label': 'Nationality', 'value': 'Nationality'}
                        ],
                        value='Age'
                    ),
                    dcc.Graph(id='demographic-chart')
                ])
            ]),
            dcc.Tab(label="Correlation Analysis", children=[
                html.Div([
                    html.H3("Correlation Heatmap"),
                    dcc.Graph(id='correlation-heatmap')
                ])
            ]),
            dcc.Tab(label="Distribution Analysis", children=[
                html.Div([
                    html.H3("Rating Distribution"),
                    dcc.Dropdown(
                        id='distribution-dropdown',
                        options=[{'label': col, 'value': col} for col in lessons + activities + food_items],
                        value=lessons[0]
                    ),
                    dcc.Graph(id='distribution-chart')
                ])
            ])
        ])
    ])