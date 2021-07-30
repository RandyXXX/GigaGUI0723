import plotly.graph_objects as go

labels=['台北','新竹','台中','高雄']
values=[1000,10002,104,999]

fig=go.Figure(data=[go.Pie(labels=labels,values=values)])
fig.show()