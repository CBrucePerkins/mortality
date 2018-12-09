import pandas as pd
import plotly.offline as ply
import plotly.graph_objs as go
ply.init_notebook_mode()
ply.offline.init_notebook_mode(connected=True)

dat = pd.read_csv("https://www.dropbox.com/s/8oryfplagvboumq/mort.csv?dl=0",encoding = "ISO-8859-1")

dat.gdppercap = dat.gdppercap/max(dat.gdppercap)
dat.moralityrates = dat.moralityrates/max(dat.moralityrates)

trace1 = go.Bar(
                    x = dat.CountryName,
                    y = dat.moralityrates,
                    name = "Infant Mortality"
                    )
trace2 = go.Bar(
                    x = dat.CountryName,
                    y = dat.gdppercap,
                    name = "GDP per Capita",
)

data = [trace1, trace2]

layout = dict(title = 'Infant Mortality vs GDP per Capita',
    yaxis= dict(title= 'Relative Proportions'),
)              
layout.update(dict(annotations=[go.Annotation(text="119225.38 GDP per Capita (Luxembourg)", x="Luxembourg", y=1,ax=132,ay=-20),
                                go.Annotation(text="9.39 % mortality rate (CentralAfricanRepublic)", x="CentralAfricanRepublic", y=1,ax=-140,ay=-20)]))

fig = go.Figure(data=data, layout=layout)
ply.iplot(fig)