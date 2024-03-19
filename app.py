import streamlit as st

from demo_value import ST_VALUE_DEMOS
from demo_model import ST_MODEL_DEMOS
from demo_experiments import ST_EXPS_DEMOS
from demo_datasets import ST_DATASETS_DEMOS
from demo_examples import ST_EXAMPLES_DEMOS


def main():
    with st.sidebar:
        st.header("Configuration")
        api_options = ("Value", "Model", "Datasets", "Experiments", "Examples")
        selected_api = st.selectbox(
            label="Options",
            options=api_options,
        )

        api_to_demo_dict = {
            "Values": ST_VALUE_DEMOS,
            "Model": ST_MODEL_DEMOS,
            "Datasets": ST_DATASETS_DEMOS,
            "Experiments": ST_EXPS_DEMOS,
            "Examples": ST_EXAMPLES_DEMOS,
        }
        selected_demo_dict = api_to_demo_dict[selected_api]

        page_options = list(api_to_demo_dict.get(selected_api, {}).keys())

        selected_page = st.selectbox(
            label="Choose an example",
            options=page_options,
        )

        demo, url = selected_demo_dict[selected_page]

    if selected_api == "Value":
        st.title("Value")
    elif selected_api == "Model":
        st.title("Model")
    elif selected_api == "Datasets":
        st.title("Datasets")
    elif selected_api == "Experiments":
        st.title("Experiments")
    elif selected_api == "Examples":
        st.title("Examples")

    demo()

    st.markdown(f"{url}")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Debiasing Diffusion Model", page_icon=":chart_with_upwards_trend:"
    )
    main()