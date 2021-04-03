# ASU_CSE_PROJECT_TEMPLATE
# ====
# Project #

__author__ = "Mike.Salzarulo"

from data import FILES
import pandas as pd

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
        if "adult.data" in path.stem:
            working_path = path

    # Generate headers
    headers = ["Age",
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
    df = pd.read_csv(working_path)

    return


if __name__ == "__main__":
    main()