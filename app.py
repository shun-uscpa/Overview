import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import *
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Use the following function when accessing the value of 'my-range-slider'
# in callbacks to transform the output value to logarithmic
def transform_value(value):
    return 10 ** value


app.layout = html.Div([
    dcc.RangeSlider(
        id='non-linear-range-slider',
        marks={i: '{}'.format(10 ** i) for i in range(4)},
        max=3,
        value=[0.1, 2],
        dots=False,
        step=0.01,
        updatemode='drag'
    ),
    dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL',
    labelStyle={'display': 'inline-block'}
    ),  
    dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['NYC', 'MTL'],
    labelStyle={'display': 'inline-block'}
    ),  

    html.Div(id='output-container-range-slider-non-linear', style={'margin-top': 20})
])


@app.callback(
    Output('output-container-range-slider-non-linear', 'children'),
    Input('non-linear-range-slider', 'value'))
def update_output(value):
    transformed_value = [transform_value(v) for v in value]
    return 'Linear Value: {}, Log Value: [{:0.2f}, {:0.2f}]'.format(
        str(value),
        transformed_value[0],
        transformed_value[1]
    )


if __name__ == '__main__':
    app.run_server(debug=True)