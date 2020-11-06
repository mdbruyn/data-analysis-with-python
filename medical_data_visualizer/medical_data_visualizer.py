import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_data_visualizer/medical_examination.csv")

# Add 'overweight' column
bmi = df["weight"] / ((df["height"] / 100) ** 2)
overweight = bmi > 25
df["overweight"] = overweight.astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of
# 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more
# than 1, make the value 1.
df["cholesterol"] = np.where(df["cholesterol"] > 1, 1, 0)
df["gluc"] = np.where(df["gluc"] > 1, 1, 0)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values
    # from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and
    # 'overweight'.
    df_cat = pd.melt(
        frame=df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    # Group and reformat the data to split it by 'cardio'. Show the counts
    # of each feature. You will have to rename one of the collumns for the
    # catplot to work correctly.
    df_cat = (
        pd.DataFrame(df_cat.groupby(["variable", "value", "cardio"])["value"].count())
        .rename(columns={"value": "total"})
        .reset_index()
    )

    # Draw the catplot with 'sns.catplot()'
    cat_plot = sns.catplot(
        x="variable", y="total", hue="value", col="cardio", data=df_cat, kind="bar"
    )

    fig = cat_plot.fig

    # Do not modify the next two lines
    fig.savefig("medical_data_visualizer/catplot.png")
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        data=corr,
        annot=True,
        fmt=".1f",
        mask=mask,
        square=True,
        linewidths=0.5,
        center=0,
        cbar_kws={"shrink": 0.5},
    )

    # Do not modify the next two lines
    fig.savefig("medical_data_visualizer/heatmap.png")
    return fig
