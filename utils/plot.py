import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

color_list = px.colors.qualitative.Safe


def get_line(data, x, y, ref):
    fig = px.line(data, x=x, y=y, color=ref)
    fig.update_layout(
                plot_bgcolor="rgba(0, 0, 0, 0)",
                width=1000, height=500,
                xaxis=dict(tickformat="%b %d %Y"))

    return fig


def get_box(data, x, y):
    fig = go.Figure()
    fig.add_trace(go.Box(
        y=data[y], x=data[x],
        boxpoints='outliers',
        marker_color='rgb(107,174,214)',
        line_color='rgb(107,174,214)'
    ))
    return fig


def get_scatter(data, x, y):
    fig = px.scatter(data, x=x, y=y, color="O trabalho remoto afetou os estudos?")
    return fig


def get_bar(data, x, y, title, width=700, height=400):
    fig = px.bar(data, x=x, y=y, color=y)
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


def get_multi_bar(visualizations, visualization):
    fig = go.Figure()
    home_office = visualizations.loc[visualizations["Categoria"] == "Remoto"]
    not_home_office = visualizations.loc[visualizations["Categoria"] == "Não Remoto"]

    not_office_count = not_home_office[visualization].value_counts()
    fig.add_trace(go.Bar(
        x=not_office_count.index,
        y=(not_office_count/not_office_count.sum())*100,
        name=f'Não Home Office',
        marker_color='indianred'
    ))

    home_count = home_office[visualization].value_counts()
    fig.add_trace(go.Bar(
        x=home_count.index,
        y=(home_count/home_count.sum())*100,
        name=f'Home Office',
        marker_color='lightsalmon'
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
        )
    )

    return fig