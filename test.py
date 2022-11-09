import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

# Read to DataFrame for Part II question 2
responses_csv = open("Responses.csv")
responses_df = pd.DataFrame(csv.DictReader(responses_csv))

# Get Body Ownership
bo = pd.DataFrame(responses_df.query('Measure == "Body Ownership"'))

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

# Median
bo_central_median = bo_df.groupby("PID").median()

bo_central_median.to_csv("bo_central_median.csv")

# Mode
bo_central_mode = bo_df.groupby("PID").agg(lambda x: x.value_counts().index[0])

bo_central_mode.to_csv("bo_central_mode.csv")

demographics_csv = open("Demographics.csv")
demographics_df = pd.DataFrame(csv.DictReader(demographics_csv))

column = demographics_df.columns[7]

PID_5_9 = []
PID_10_49 = []
PID_50_99 = []
PID_100_ = []

for i in range(len(demographics_df)):
    if demographics_df["VR Experience"].iloc[i] == "5-9 hours":
        PID_5_9.append(demographics_df["PID"].iloc[i])
    elif demographics_df["VR Experience"].iloc[i] == "100+ hours":
        PID_100_.append(demographics_df["PID"].iloc[i])
    elif demographics_df["VR Experience"].iloc[i] == "50-99 hours":
        PID_50_99.append(demographics_df["PID"].iloc[i])
    else:
        PID_10_49.append(demographics_df["PID"].iloc[i])

response_alien_hand_5_9 = []
response_alien_hand_10_49 = []
response_alien_hand_50_99 = []
response_alien_hand_100_ = []
response_matched_hand_5_9 = []
response_matched_hand_10_49 = []
response_matched_hand_50_99 = []
response_matched_hand_100_ = []
response_mismatched_hand_5_9 = []
response_mismatched_hand_10_49 = []
response_mismatched_hand_50_99 = []
response_mismatched_hand_100_ = []

for i in range(len(bo_df)):
    this_PID = bo_df["PID"].iloc[i]
    if this_PID in PID_5_9:
        response_alien_hand_5_9.append(bo_df["Alien_Hand"].iloc[i])
        response_matched_hand_5_9.append(bo_df["Matched_Hand"].iloc[i])
        response_mismatched_hand_5_9.append(bo_df["Mismatched_Hand"].iloc[i])
    elif this_PID in PID_10_49:
        response_alien_hand_10_49.append(bo_df["Alien_Hand"].iloc[i])
        response_matched_hand_10_49.append(bo_df["Matched_Hand"].iloc[i])
        response_mismatched_hand_10_49.append(bo_df["Mismatched_Hand"].iloc[i])
    elif this_PID in PID_50_99:
        response_alien_hand_50_99.append(bo_df["Alien_Hand"].iloc[i])
        response_matched_hand_50_99.append(bo_df["Matched_Hand"].iloc[i])
        response_mismatched_hand_50_99.append(bo_df["Mismatched_Hand"].iloc[i])
    else:
        response_alien_hand_100_.append(bo_df["Alien_Hand"].iloc[i])
        response_matched_hand_100_.append(bo_df["Matched_Hand"].iloc[i])
        response_mismatched_hand_100_.append(bo_df["Mismatched_Hand"].iloc[i])

res_ah_mean = [np.mean(response_alien_hand_5_9), np.mean(response_alien_hand_10_49), np.mean(response_alien_hand_50_99), np.mean(response_alien_hand_100_)]
res_mah_mean = [np.mean(response_matched_hand_5_9), np.mean(response_matched_hand_10_49), np.mean(response_matched_hand_50_99), np.mean(response_matched_hand_100_)]
res_mih_mean = [np.mean(response_mismatched_hand_5_9), np.mean(response_mismatched_hand_10_49), np.mean(response_mismatched_hand_50_99), np.mean(response_mismatched_hand_100_)]

res_ah_var = [np.std(response_alien_hand_5_9), np.std(response_alien_hand_10_49), np.std(response_alien_hand_50_99), np.std(response_alien_hand_100_)]
res_mah_var = [np.std(response_matched_hand_5_9), np.std(response_matched_hand_10_49), np.std(response_matched_hand_50_99), np.std(response_matched_hand_100_)]
res_mih_var = [np.std(response_mismatched_hand_5_9), np.std(response_mismatched_hand_10_49), np.std(response_mismatched_hand_50_99), np.std(response_mismatched_hand_100_)]

def plot(mean, std, name):
    plt.bar(["5-9", "10-49", "50-99", "100+"], mean)
    plt.errorbar(["5-9", "10-49", "50-99", "100+"], mean, std, fmt='.', ecolor='r')
    plt.savefig(name)

# plot(res_ah_mean, res_ah_var, "alien_hand.pdf")
# plot(res_mah_mean, res_mah_var, "mathed_hand.pdf")
# plot(res_mih_mean, res_mih_var, "mismatched_hand.pdf")

print(stats.kruskal(response_alien_hand_5_9, response_alien_hand_10_49, response_alien_hand_50_99, response_alien_hand_100_))
print(stats.kruskal(response_matched_hand_5_9, response_matched_hand_10_49, response_matched_hand_50_99, response_matched_hand_100_))
print(stats.kruskal(response_mismatched_hand_5_9, response_mismatched_hand_10_49, response_mismatched_hand_50_99, response_mismatched_hand_100_))