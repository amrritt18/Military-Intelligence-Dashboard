import plotly.express as px

from utils.constants import DEFAULT_TEMPLATE


# ==========================================
# Line Chart
# ==========================================

def create_line_chart(df, x, y, title):

    fig = px.line(df, x=x, y=y, markers=True, title=title)

    fig.update_layout(template=DEFAULT_TEMPLATE)

    return fig


# ==========================================
# Bar Chart
# ==========================================

def create_bar_chart(df, x, y, title, color=None):

    fig = px.bar(df, x=x, y=y, color=color, title=title)

    fig.update_layout(template=DEFAULT_TEMPLATE)

    return fig


# ==========================================
# Horizontal Bar Chart
# ==========================================

def create_horizontal_bar_chart(df, x, y, title, color=None):

    fig = px.bar(df, x=x, y=y, color=color, orientation="h", title=title)

    fig.update_layout(template=DEFAULT_TEMPLATE)

    return fig


# ==========================================
# Pie Chart
# ==========================================

def create_pie_chart(df, names, values, title):

    fig = px.pie(df, names=names, values=values, title=title)

    fig.update_layout(template=DEFAULT_TEMPLATE)

    return fig


# ==========================================
# Scatter Chart
# ==========================================

def create_scatter_chart(df, x, y, title, color=None):

    fig = px.scatter(df, x=x, y=y, color=color, title=title)

    fig.update_layout(template=DEFAULT_TEMPLATE)

    return fig


# ==========================================
# Histogram
# ==========================================

def create_histogram(df, x, title, color=None):

    fig = px.histogram(df, x=x, color=color, title=title)

    fig.update_layout(template=DEFAULT_TEMPLATE)

    return fig


# ==========================================
# Box Plot
# ==========================================

def create_box_plot(df, x, y, title, color=None):

    fig = px.box(df, x=x, y=y, color=color, title=title)

    fig.update_layout(template=DEFAULT_TEMPLATE)

    return fig


# ==========================================
# World Map
# ==========================================

def create_world_map(df, title, color="attacktype1_txt", hover_name="city", hover_data=None):

    fig = px.scatter_geo(
        df,
        lat="latitude",
        lon="longitude",
        color=color,
        hover_name=hover_name,
        hover_data=hover_data,
        projection="natural earth",
        title=title
    )

    fig.update_layout(
        template=DEFAULT_TEMPLATE,
        height=600
    )

    return fig