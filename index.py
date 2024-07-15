from dash import html, dcc
from dash.dependencies import Input, Output

from app import app
from layouts import create_layout
import callbacks

app.layout = create_layout()

if __name__ == '__main__':
    app.run_server(debug=True)