import plotly.express as px
import random as rd
from numpy import size
from patsy import origin

x = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l"]
y = []
for i in range(0, 12):
    m = rd.random()
    y.append(m)

fig = px.bar(y=x, x=y, color=x, animation_frame=x, orientation='h',range_color='continent')
# fig.write_html('first_figure.html', auto_open=True)
fig.show()
