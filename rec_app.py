import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import recco
import moods

books=pd.read_csv(r'books.csv',error_bad_lines = False)
books=books.dropna()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "26rem",
    "padding": "2rem 1rem",
    "background-color": "#1e2130",
    "color": '#FFFFFF',
	"overflow" :'scroll'
}

CONTENT_STYLE = {
    "margin-left": "26rem",
    "margin-right": "0rem",
    "padding": "2rem 1rem",
	"background-color": "#1e2130",
    "color": '#FFFFFF'
}
labels=['fiction', 'ebooks', 'contemporary', 'fantasy', 'romance', 'mystery', 'classics', 'thriller', 'suspense', 'history', 'crime', 'paranormal', 'nonfiction', 'horror', 'science', 'biography', 'philosophy', 'memoir', 'religion', 'psychology', 'spirituality', 'comics', 'travel', 'art', 'poetry', 'business', 'christian', 'music', 'manga', 'sports', 'cookbooks']
values=[9097, 7203, 5287, 4259, 4251, 3686, 2785, 2522, 2419, 2138, 2083, 1941, 1833, 1372, 1239, 1109, 1055, 905, 893, 810, 503, 469, 457, 436, 377, 377, 357, 226, 196, 196, 92]

fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo = "none" , title='Top Genres')])

fig2= px.line(books, y="books_count", x="average_rating", title='Book Count VS Average Rating')

def fig3(list_m):
	data={'Book_Recommendations' : list_m}
	df = pd.DataFrame(data)
	fig3 = go.Figure(data=[go.Table(
	  header=dict(
		values=["<b>Book Recommendations</b>"],
		line_color='white', fill_color='white',
		align='center', font=dict(color='black', size=12),height=30
	  ),
	  cells=dict(
		values=[df['Book_Recommendations']],
		line_color=['#000000'], fill_color=['#3b5998'],
		align='center', font=dict(color='white', size=11), height=30
	  ))
	])
	fig3.update_layout(margin=dict(
        l=10,
        r=10,
        b=10,
        t=10,
        pad=0
    ), paper_bgcolor='#6c757d')
	return fig3

def fig4(list_m):
	data={'Book_Recommendations' : list_m}
	df = pd.DataFrame(data)
	fig4 = go.Figure(data=[go.Table(
	  header=dict(
		values=["<b>Suggestions</b>"],
		line_color='white', fill_color='white',
		align='center', font=dict(color='black', size=12),height=50
	  ),
	  cells=dict(
		values=[df['Book_Recommendations']],
		line_color=['#000'], fill_color=['#3b5998'],
		align='center', font=dict(color='white', size=11), height=60
	  ))
	])
	fig4.update_layout(margin=dict(
        l=10,
        r=10,
        b=10,
        t=10,
        pad=0
    ), paper_bgcolor='#6c757d')
	return fig4

fig.show()
sidebar = html.Div(
    [
		html.Div([
                dcc.Graph(
                    id='example-graph-2',
                    figure=fig
                )
                ]),
		html.Hr(style={'border-top': '1px solid blue'}),
        html.P(
            "Select a book from the drop-down to get recommendations that you may like.", className="lead"
        ),
		html.Div([
				dcc.Dropdown(
				id='input-dropdown',
				options=[
					{'label': i, 'value': i} for i in list(books['original_title'])
				],
				value='Harry Potter and the Chamber of Secrets',
				style={'color':'#000000'})
				]),
		html.Hr(style={'border-top': '1px solid blue'}),
        html.Div([
                dcc.Graph(
                    id='example-graph3',
                    figure=fig2
                )
                ])
                
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(
		
		[html.H2("RECOMMENDATION ENGINE", className="display-7",id="page-content"),
		html.Hr(style={'border-top': '1px solid blue'}),
		html.H4("Popular Books", className="display-7",id="page-content1"),
		
		html.Img(src='https://upload.wikimedia.org/wikipedia/en/d/dc/The_Hunger_Games.jpg' ,title='The Hunger Games', style={'height':'6rem', 'width':'6rem' , 'padding':"1rem 1rem"}, className= 'column'),
		html.Img(src='https://hpmedia.bloomsbury.com/rep/s/9781526620293_311606.png', style={'height':'6rem', 'width':'6rem' , 'padding':"1rem 1rem"},className= 'column'),
		html.Img(src='https://upload.wikimedia.org/wikipedia/commons/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg', style={'height':'6rem', 'width':'6rem' , 'padding':"1rem 1rem"},className= 'column'),
		html.Img(src='https://upload.wikimedia.org/wikipedia/en/thumb/f/f7/TheGreatGatsby_1925jacket.jpeg/220px-TheGreatGatsby_1925jacket.jpeg', style={'height':'6rem', 'width':'6rem' , 'padding':"1rem 1rem"},className= 'column'),
		html.Img(src='https://booklistqueen.com/wp-content/uploads/the-fault-in-our-stars-john-green.jpg',className= 'column',  style={'height':'6rem', 'width':'6rem' , 'padding':"1rem 1rem"}),
		html.Img(src='https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Hobbit_cover.JPG/170px-Hobbit_cover.JPG', style={'height':'6rem', 'width':'6rem' , 'padding':"1rem 1rem"},className= 'column'),
		html.Img(src='https://upload.wikimedia.org/wikipedia/commons/8/89/The_Catcher_in_the_Rye_%281951%2C_first_edition_cover%29.jpg',className= 'column',  style={'height':'6rem', 'width':'6rem' , 'padding':"1rem 1rem"}),
		html.Img(src='https://upload.wikimedia.org/wikipedia/en/thumb/1/1d/Twilightbook.jpg/220px-Twilightbook.jpg', style={'height':'6rem', 'width':'6rem' , 'padding':"1rem 1rem"},className= 'column'),
		html.Img(src='https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Littleprince.JPG/220px-Littleprince.JPG', style={'height':'6rem', 'width':'6rem' , 'padding':"1rem 1rem"},className= 'column'),
		html.Img(src='https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/DaVinciCode.jpg/220px-DaVinciCode.jpg', style={'height':'6rem', 'width':'6rem' , 'padding':"1rem 1rem"},className= 'column'),
		dbc.Row(
            [
                dbc.Col(html.Div([
                dcc.Graph(
                    id='output-container'
                )
                ]), md=8),
                dbc.Col([
				dbc.Button(" ROMANTIC ", className="m-1", id="rbutton", style={"padding":"1rem 1rem", 'height':'3rem', 'width':'8rem', "bottom": 2}, n_clicks_timestamp=1),
				dbc.Button(" FICTION ", className="m-1",id="fbutton", style={"padding":"1rem 1rem",'height':'3rem', 'width':'8rem',"bottom": 2},n_clicks_timestamp=0),
				dbc.Button(" THRILLERS ", className="m-1",id="tbutton", style={"padding":"1rem 1rem", 'height':'3rem', 'width':'8rem', "bottom": 2},n_clicks_timestamp=0),
				dbc.Button(" MYSTERY ", className="m-1",id="mbutton", style={"padding":"1rem 1rem", 'height':'3rem', 'width':'8rem',"bottom": 2},n_clicks_timestamp=0),
				dcc.Graph(
                    id='output'
                )
				], md=4),
            ],
        ),
		],style=CONTENT_STYLE)
		
		
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    dash.dependencies.Output('output-container', 'figure'),
    [dash.dependencies.Input('input-dropdown', 'value')],
	)
def update_output(value):
	getl=recco.get_recommendations_new(value)
	return fig3(getl)
		

@app.callback(
	dash.dependencies.Output("output", "figure"), [dash.dependencies.Input("rbutton", "n_clicks_timestamp"), dash.dependencies.Input("mbutton", "n_clicks_timestamp"),dash.dependencies.Input("tbutton", "n_clicks_timestamp"), dash.dependencies.Input("fbutton", "n_clicks_timestamp")]
)
	
def click(rbutton,mbutton,tbutton,fbutton):
	if int(rbutton)> int(mbutton)  and int(rbutton)>int(tbutton) and int(rbutton)>int(fbutton):
		l=moods.get_r()
		return fig4(l)
	elif int(mbutton)>int(rbutton) and int(mbutton)>int(tbutton) and int(mbutton)>int(fbutton):
		l=moods.get_m()
		return fig4(l)
	elif int(tbutton)>int(rbutton) and int(tbutton)>int(mbutton) and int(tbutton)>int(fbutton):
		l=moods.get_t()
		return fig4(l)
	elif int(fbutton)>int(rbutton) and int(fbutton)>int(mbutton) and int(fbutton)>int(tbutton):
		l=moods.get_f()
		return fig4(l)

if __name__ == "__main__":
    app.run_server()