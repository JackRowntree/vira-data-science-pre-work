import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash import dash_table,Dash
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@db:5432/postgres')

def read_table(table):
    return pd.read_sql_query(f'select * from {table}', con = engine)
    
df_cohort_funnel = read_table('cohort_funnel_stats')
df_baseline_null_stats = read_table('baseline_dfnulls_stats')
df_visit1_null_stats = read_table('visit1_dfnulls_stats')
df_visit2_null_stats = read_table('visit2_dfnulls_stats')

app = Dash(__name__)
fig_present_in_all = px.bar(df_cohort_funnel, x= "stage", y="subjects")

app.layout = html.Div(children=[
    html.H1(children='SWAN Data Quality Dashboard'),

    html.H2(children='''
        Cohort represented in all studies - total at each stage
    '''),
    dcc.Graph(
        id='cohort_fig',
        figure=fig_present_in_all
    ),
    html.H2(children='''
        Columns with >95% Null from baseline data
    '''),

    dash_table.DataTable(df_baseline_null_stats.to_dict('records'), [{"name": i, "id": i} for i in df_baseline_null_stats.columns],page_action='none',
    style_table={'height': '300px', 'overflowY': 'auto'}),
    
        html.H2(children='''
        Columns with >95% Null from first visit data
    '''),

    dash_table.DataTable(df_visit1_null_stats.to_dict('records'), [{"name": i, "id": i} for i in df_visit1_null_stats.columns],page_action='none',
    style_table={'height': '300px', 'overflowY': 'auto'}),
        html.H2(children='''
        Columns with >95% Null from 2nd visit data
    '''),

    dash_table.DataTable(df_visit2_null_stats.to_dict('records'), [{"name": i, "id": i} for i in df_visit2_null_stats.columns],page_action='none',
    style_table={'height': '300px', 'overflowY': 'auto'}),
    
])
app.run_server(host='0.0.0.0', debug=True, port=8000)