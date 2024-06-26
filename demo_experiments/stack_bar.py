import streamlit as st
import pyecharts.options as opts

from pyecharts.charts import Bar, Grid
from streamlit_echarts import st_pyecharts
from pyecharts.commons.utils import JsCode

# Male : Female = 1 : 4
def dataset1():
    b = (
        Bar()
        .add_xaxis(["0", "0.01", "0.05", "0.1"])  # Alpha values as categories
        .add_yaxis("Male", [0.36, 0.39, 0.58, 0.6], stack="stack1", color='blue')  # Male proportions, stacked
        .add_yaxis("Female", [0.64, 0.61, 0.42, 0.4], stack="stack1", color='pink')  # Female proportions, stacked
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Male and Female Proportions at Different Alpha Values",
                subtitle="male : female = 1 : 4 (training dataset)",
            ),
            legend_opts=opts.LegendOpts(
                pos_top="15%",
            ),
            yaxis_opts=opts.AxisOpts(
                name="Proportion(%)",
                name_gap=25,  # Adjust this to move the y-axis label to the left
                axislabel_opts=opts.LabelOpts(
                    font_size=12,  # Adjust label font size if necessary
                    formatter=JsCode("function(value){return value * 100;}")  # Convert proportion to percentage
                ),
            ),
            xaxis_opts=opts.AxisOpts(
                name="α",  # Here we're setting the x-axis label
                name_location="middle",
                name_gap=30
            ),
        )
    )

    grid = (
        Grid()
        .add(
            chart=b, 
            grid_opts=opts.GridOpts(
                pos_bottom="15%",
                pos_top="30%"
            )
        )
    )

    st_pyecharts(
        grid, key="echarts"
    )  # Add key argument to not remount component at every Streamlit run

# Male : Female = 4 : 1
def dataset2():
    b = (
        Bar()
        .add_xaxis(["0", "0.01", "0.05", "0.1"])  # Alpha values as categories
        .add_yaxis("Male", [0.8, 0.89, 0.64, 0.9], stack="stack2", color='blue')  # Male proportions, stacked
        .add_yaxis("Female", [0.2, 0.11, 0.36, 0.1], stack="stack2", color='pink')  # Female proportions, stacked
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Male and Female Proportions at Different Alpha Values",
                subtitle="male : female = 4 : 1 (training dataset)",
            ),
            legend_opts=opts.LegendOpts(
                pos_top="15%",
            ),
            yaxis_opts=opts.AxisOpts(
                name="Proportion(%)",
                name_gap=25,  # Adjust this to move the y-axis label to the left
                axislabel_opts=opts.LabelOpts(
                    font_size=12,  # Adjust label font size if necessary
                    formatter=JsCode("function(value){return value * 100;}")  # Convert proportion to percentage
                ),
            ),
            xaxis_opts=opts.AxisOpts(
                name="α",  # Here we're setting the x-axis label
                name_location="middle",
                name_gap=30
            ),
        )
    )
    grid = (
        Grid()
        .add(
            chart=b, 
            grid_opts=opts.GridOpts(
                pos_bottom="15%",
                pos_top="30%"
            )
        )
    )

    st_pyecharts(
        grid, key="echarts"
    )  # Add key argument to not remount component at every Streamlit run

# Male : Female = 1 : 1
def dataset3():
    b = (
        Bar()
        .add_xaxis(["0", "0.01", "0.05", "0.1"])  # Alpha values as categories
        .add_yaxis("Male", [0.58, 0.52, 0.45, 0.53], stack="stack3", color='blue')  # Male proportions, stacked
        .add_yaxis("Female", [0.42, 0.48, 0.55, 0.47], stack="stack3", color='pink')  # Female proportions, stacked
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Male and Female Proportions at Different Alpha Values",
                subtitle="male : female = 1 : 1 (training dataset)",
            ),
            legend_opts=opts.LegendOpts(
                pos_top="15%",
            ),
            yaxis_opts=opts.AxisOpts(
                name="Proportion(%)",
                name_gap=25,  # Adjust this to move the y-axis label to the left
                axislabel_opts=opts.LabelOpts(
                    font_size=12,  # Adjust label font size if necessary
                    formatter=JsCode("function(value){return value * 100;}")  # Convert proportion to percentage
                ),
            ),
            xaxis_opts=opts.AxisOpts(
                name="α",  # Here we're setting the x-axis label
                name_location="middle",
                name_gap=30
            ),
        )
    )
    grid = (
        Grid()
        .add(
            chart=b, 
            grid_opts=opts.GridOpts(
                pos_bottom="15%",
                pos_top="30%"
            )
        )
    )

    st_pyecharts(
        grid, key="echarts"
    )  # Add key argument to not remount component at every Streamlit run

def example():
    st.session_state['example'] = './demo_experiments/images/example.jpg'
    st.image(st.session_state['example'])

def stat():
    st.session_state['example'] = './demo_experiments/images/table.jpg'
    st.image(st.session_state['example'])

ST_STACKBAR_DEMOS = {
    "Example": (
        example,
        " ",
    ),
    "Statistical Results": (
        stat,
        "This table showcases the debiasing effects of the method. The best results are highlighted in bold.",
    ),
    "Experiment 1": (
        dataset1,
        " ",
    ),
    "Experiment 2": (
        dataset2,
        " ",
    ),
    "Experiment 3": (
        dataset3,
        " ",
    ),
}
