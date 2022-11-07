import csv
import pandas as pd
import parse

data = parse.load_json("data.json")

responses_csv = open("Responses.csv")
responses_df = pd.DataFrame(csv.DictReader(responses_csv))

bo = responses_df.query('Measure == "Body Ownership"')[["PID", "Condition", "Response"]]

bo["Response"] = bo["Response"].astype(float)

bo.to_csv("bo.csv")

bo_central = bo.groupby(["PID", "Condition"]).agg(lambda x: x.value_counts().index[0]).reset_index()
bo_central.to_csv("bo_central.csv")