# ASU_CSE_PROJECT_TEMPLATE
# ====
# Project #

__author__ = "Mike.Salzarulo"

from data import FILES
from output import _this as output_fldr

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.RcParams.update({"figure.facecolor": "k", "axes.edgecolor": "w"})


# 14 stories
# 1  Mike   - age to income
# 2  Mike   - workclass
# 3  None   - fnlwgt
# 4  None   - education to income
# 5  None   - education-num
# 6  None   - marital status to income
# 7  None   - occupation
# 8  None   - relationship
# 9  Hannah - race
# 10 Hannah - sex to income
# 11 None   - copital gain
# 12 None   - copital loss
# 13 None   - hours per week
# 14 None   - native country

def main():
    # Reserve adult.test explusively for testing

    # Grab adult.data for visualizations
    for path in FILES:
        if "adult.data" in path.name:
            working_path = path

    # Generate headers
    headers = ["age",
               "workingclass",
               "fnlwgt",
               "education",
               "education_num",
               "marital_status",
               "occupation",
               "relationship",
               "race",
               "sex",
               "capital_gain",
               "capital_loss",
               "hours_per_week",
               "native_country",
               "income"]

    # Read in data
    df = pd.read_csv(working_path, names=headers)

    # Convert the income column to boolian values
    df.income = (df.income == " >50K") * 1

    # ====
    # single variable visualization
    # ====

    # show histograms of income and age
    # income
    fig, ax = plt.subplots()
    rects = df.hist(column="income", bins=2, ax=ax, grid=False, ec="k")
    rects[-1].set_fc("gainsboro")
    ax.patches[-1].set_fc("k")
    ax.patches[-1].set_ec("b")
    ax.annotate(">50K", xy=(ax.patches[-1].get_x() + ax.patches[-1].get_width()/2, ax.patches[-2].get_height()/2), xytext=(0, 0), textcoords="offset points",
                verticalalignment='center', color="k", clip_on=True, weight="bold")
    ax.patches[-2].set_fc("w")
    ax.patches[-2].set_ec("b")
    ax.annotate("<=50K", xy=(ax.patches[-2].get_x() + ax.patches[-2].get_width() / 2, ax.patches[-2].get_height() / 2),
                xytext=(0, 0), textcoords="offset points",
                verticalalignment='center', color="k", clip_on=True, weight="bold")
    ax.set_xticks(np.linspace(df.income.min(), df.income.max(), 3, dtype=np.uint8))
    ax.set_xlabel("Income Bin")
    ax.set_ylabel("Number in bin")
    ax.set_title("Distribution of Income")
    plt.show(block=False)
    plt.savefig(output_fldr / "Income.png")

    # age
    fig, ax = plt.subplots()
    rects = df.hist(column="age", ax=ax, grid=False, ec="k")
    ax.set_xticks(np.linspace(df.age.min(), df.age.max(), 11, dtype=np.uint8))
    ax.set_xlabel("Age Bin")
    ax.set_ylabel("Number in bin")
    ax.set_title("Distribution of Age")
    plt.show(block=False)
    plt.savefig(output_fldr / "Age distrobution.png")

    # This was tricky to view categorical data as a single variable
    # I needed to unpack the catagories and the count of each occurance
    labels = df.workingclass.value_counts().index.values
    heights = df.workingclass.value_counts().values

    # some fancy formatting and then basic plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.subplots_adjust(left=0.13, right=.99, top=.89, bottom=.05)
    rects = ax.barh(np.arange(len(heights)), heights, tick_label=labels)

    # Due to the skew of categories the visualization isn't very telling
    # so this next block generates annotations to the visualizations
    rect_labels = []
    for ind, rect in enumerate(rects):
        width = rect.get_width()
        value = heights[ind]
        # These values are heuristically determined based on the data
        xloc = 5
        color = "k"
        if width > 22000:
            xloc = -50
            color = "w"
        yloc = rect.get_y() + rect.get_height() / 2
        # plot the annotations with appropriate formatting
        label = ax.annotate(value, xy=(width, yloc), xytext=(xloc, 0), textcoords="offset points",
                            verticalalignment='center', color=color, clip_on=True, weight="bold")
        rect_labels.append(label)

    ax.set_title("Distribution of People by Workclass")
    plt.show(block=False)
    plt.savefig(output_fldr / "Workclass distrobution.png")

    # ====
    # End single variable visualization
    # ====

    # ====
    # multi-variable visualization
    # ====

    # age to income
    # working class to income
    # age to working class to income

    # todo: next steps here

    # ====
    # End multi-variable visualization
    # ====

    return


if __name__ == "__main__":
    main()
