import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df=pd.DataFrame({"station":["台北","新竹","台中","台南"],
                 "provider":["Uber","Uber","熊貓","Uber"],
                 "passenger":[1,4,6,1]})
fig=px.bar(df,x='station',y='provider',color='passenger',barmode='group')
fig=go.Figure()
description = "Provider=%s<br>Station=%%{x}<br>Passenger=%%{y}"
for provider ,group in df.groupby("provider"):
    fig.add_trace(go.Bar(x=group["station"],y=group["passenger"],name=provider,
                         hovertemplate=description%provider))

fig.update_layout(legend_title_text="Provider")
fig.update_xaxes(title_text="station")
fig.update_yaxes(title_text="passger k/times")
fig.show()
