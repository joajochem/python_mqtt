#!/usr/bin/python3



#pandas dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1',
                                        database='test_db',
                                        user='db_user',
                                        password='mqttpassword')

mycursor = connection.cursor()

def get_data():
    mycursor.execute("""select Name,Status,ip_address from nodes
    """)
    result = mycursor.fetchall()
    connection.commit()
    return result


def generate_team_button(data):
    if data[1] == 'online':
        print("online")
        status = 'green'
    if data[1] == 'offline':
        print("offline")
        status = 'red'
    
    tooltip = str(data[0]) + 'tooltip'
    tip_text =  "ip_address: {} nodesname: {}".format(str(data[2]), str(data[0]))
    return html.Div([
        html.Div([
            html.Center([
                html.Img(src=app.get_asset_url('rpi.jpg'),
            style={'height':'150px', 'width':'150px'}, id=tooltip)
            ]),
            dbc.Tooltip(
            tip_text,
            target=tooltip,
            ),
            html.Center(children=str(data[0]),
            style={'font-size': '30px'}),
        ], style={'background-color':status, 'width': '220px', 'height': '200px', 
        'justify-content': 'center', 'padding': 
        '10px', 'margin': '10px' }, id=str(data[0]))])



app = dash.Dash(
    external_stylesheets=[dbc.themes.DARKLY],
)
app.config.suppress_callback_exceptions = False




app.layout = html.Div(children=[
    
    html.Div([
        html.Center(html.H1('test', style={'font-size': '30px',
        'align': 'center',
        'justify-content': 'space-between', 'backgroundColor':'grey'})),
        dbc.Tabs(id="tabs",
         active_tab="tab_0", children=[
            dbc.Tab(tab_id="tab_0", label="Overview", children=[
                dbc.Row(id='nodes_divs'),
                dcc.Interval(
                id='graph-update',
                interval=1*10000,
                n_intervals=0
                ),
            ])
        ])
    ])
])


@app.callback(
    Output("nodes_divs", "children"),
    [Input('graph-update', 'n_intervals')])

def update(n):
    
    data = get_data()
    print(data)

    print('going')
    return [generate_team_button(i) for i in data]

app.run_server(debug=False, host='0.0.0.0')
