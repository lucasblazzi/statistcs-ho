import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


colors = ["#05445e", "#75e6da", "#189ab4", "#00938e", "#d4f1f4", "#006b7f", "#626897",
          "#3bba8a", "#35577c", "#c189ba", "#98dd7a", "#f9f871", "#ef9bc1"]

default_color = ["#004c6d", "#005f82", "#007396", "#0087aa", "#009cbd", "#00b1cf", "#00c7e1", "#00ddf0", "#00f4ff"]

def plot_scatter(data, x, y):
    fig = px.scatter(data, x=x, y=y, color="O trabalho remoto afetou os estudos?")
    fig.update_layout(
        title=dict(text=f"<b>Avaliação - Por que o Home Office afeta os estudos?</b>",
                   y=0.95, x=0.45,
                   xanchor='center', yanchor='top'
                   ),
        width=1000,
        height=500
    )
    return fig


def plot_pie(data, x, y, title, width=500, height=500):
    fig = px.pie(data, values=x, names=y, color_discrete_sequence=colors)
    fig.update_layout(
        title=dict(text=f"<b>{title}</b>",
                   y=0.95, x=0.48,
                   xanchor='center', yanchor='top'
                   ),
        yaxis=dict(
            title='',
            titlefont_size=16,
            tickfont_size=14,
        ),
        width=width,
        height=height
    )
    return fig


def plot_bar(data, x, y, title, color, width=700, height=400):
    fig = px.bar(data, x=x, y=y, color=y, color_continuous_scale=default_color)
    fig.update_layout(
        title=dict(text=f"<b>{title}</b>",
                   y=0.95, x=0.48,
                   xanchor='center', yanchor='top'
                   ),
        yaxis=dict(
            title='',
            titlefont_size=16,
            tickfont_size=14,
        ),
        showlegend=False,
        width=width,
        height=height
    )
    return fig


def plot_multi_bar(visualizations, visualization):
    fig = go.Figure()
    home_office = visualizations.loc[visualizations["Categoria"] == "Remoto"]
    not_home_office = visualizations.loc[visualizations["Categoria"] == "Não Remoto"]

    not_office_count = not_home_office[visualization].value_counts()
    fig.add_trace(go.Bar(
        x=not_office_count.index,
        y=(not_office_count/not_office_count.sum())*100,
        name=f'Não Home Office',
        marker_color=colors[0]
    ))

    home_count = home_office[visualization].value_counts()
    fig.add_trace(go.Bar(
        x=home_count.index,
        y=(home_count/home_count.sum())*100,
        name=f'Home Office',
        marker_color=colors[1]
    ))

    fig.update_layout(
        barmode='group', xaxis_tickangle=-45,
        title=dict(text=f"<b>Comparativo de Perspectiva - {visualization}</b>",
                   y=0.9, x=0.48,
                   xanchor='center', yanchor='top'
                   ),
        yaxis=dict(
            title='%',
            titlefont_size=16,
            tickfont_size=14,
        ),
        width=900,
        height=500
    )

    return fig


def plot_histogram(df, title):
    fig = go.Figure(data=[go.Histogram(x=df["Vontade x Satisfação"], xbins=dict(start=1, end=10, size=1))])
    fig.update_layout(
        title = dict(text=f"<b>{title}</b>",
                     y=0.90, x=0.5,
                     xanchor='center', yanchor='top'
                     ),
        yaxis=dict(
            title="Contagem",
            titlefont_size=16,
            tickfont_size=14,
        ),
    )
    return fig


def plot_table(data, col, title, width=500, height=500):
    df = data[col].describe().reset_index()
    _table = go.Figure(go.Table(
        columnwidth=[1, 1],
        header=dict(
            values=[f"<b>{name}<b>" for name in df.columns],
            font=dict(size=12, color="white"),
            line_color='darkslategray',
            fill_color='#404040',
            align="center"
        ),
        cells=dict(
            values=[df[name] for name in df.columns],
            line_color='darkslategray',
            fill_color='#f0f2f6',
            align = "center"
        ))
    )
    _table.update_layout(
        title=dict(text=f"<b>{title}</b>",
                   y=0.9 ,x=0.5,
                   xanchor='center' ,yanchor='top'
                   ),
        width=width,
        height=height
    )
    return _table


def plot_box(data, title, name, col):
    box = go.Figure()
    box.add_trace(go.Box(x=data[col], quartilemethod="linear", name=name))
    box.update_layout(
        title=dict(text=f"<b>{title}</b>",
                   y=0.9,x=0.5,
                   xanchor='center',yanchor='top'
                   ),
        width=600,
        height=400
    )
    return box