import logging

import pandas as pd
import seaborn as sns


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def load_data(path):
    """Load data from path"""
    data = pd.read_csv(path)
    # for demonstration
    data = data.sample(5000)
    return data


def transform_data(data):
    """Transform data"""
    colors = sns.color_palette("coolwarm").as_hex()
    n_colors = len(colors)

    data = data.reset_index(drop=True)
    data["norm_price"] = data["price"] / data["area"]

    data["label_colors"] = pd.qcut(data["norm_price"], n_colors, labels=colors)
    data["label_colors"] = data["label_colors"].astype("str")
    return data
