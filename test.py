import csv
import pandas as pd

# Read to DataFrame for Part II question 2
responses_csv = open("Responses.csv")
responses_df = pd.DataFrame(csv.DictReader(responses_csv))

# Get Body Ownership
bo = responses_df.query('Measure == "Body Ownership"')[["PID", "Condition", "Response"]].reindex()

bo["Response"] = bo["Response"].astype(float)

bo.to_csv("bo.csv")

# Apply central tendency to Body Ownership
# And reshape the data, the row names will be PID, the column names will be Condition

# Mean
# bo_central = bo.groupby(["PID", "Condition"]).mean("Response").unstack()

# Mode
bo_central = bo.groupby(["PID", "Condition"]).agg(lambda x: x.value_counts().index[0])

bo_central = bo_central.reset_index().pivot(index="PID", columns="Condition", values="Response")

bo_central.to_csv("bo_central.csv")
