import csv
import pandas as pd

# Read to DataFrame for Part II question 2
responses_csv = open("Responses.csv")
responses_df = pd.DataFrame(csv.DictReader(responses_csv))

# Get Body Ownership
bo = responses_df.query('Measure == "Body Ownership"')

bo.to_csv("a.csv")

PID_ = bo["PID"].to_list()
responses = bo["Response"].astype(float).to_list()

PID = []
Alien_Hand = []
Matched_Hand = []
Mismatched_Hand = []

i = 0

while i < len(bo["PID"]):
    PID.append(PID_[i])
    Mismatched_Hand.append(responses[i])
    i += 1
    Alien_Hand.append(responses[i])
    i += 1    
    Matched_Hand.append(responses[i])
    i += 1

bo_dic = dict()
bo_dic["PID"] = PID
bo_dic["Mismatched_Hand"] = Mismatched_Hand
bo_dic["Alien_Hand"] = Alien_Hand
bo_dic["Matched_Hand"] = Matched_Hand

bo_df = pd.DataFrame(bo_dic)
bo_df.to_csv("bo.csv")

# Apply central tendency to Body Ownership
# And reshape the data, the row names will be PID, the column names will be Condition

# Mean
bo_central_mean = bo_df.groupby("PID").mean()

bo_central_mean.to_csv("bo_central_mean.csv")

# Mode
bo_central_mode = bo_df.groupby("PID").agg(lambda x: x.value_counts().index[0])

bo_central_mode.to_csv("bo_central_mode.csv")