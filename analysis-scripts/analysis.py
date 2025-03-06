import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

correct_answers = {
    "blue_1": 46,
    "blue_2": 5,
    "blue_3": 67,
    "blue_4": 41,
    "red_1": 31,
    "red_2": 47,
    "red_3": 44,
    "red_4": 25,
    "green_1": 12,
    "green_2": 42,
    "green_3": 25,
    "green_4": 31,
}

custom_palette = {
    "Blue 1": "#b2d3e8", "Blue 2": "#eff6fc", "Blue 3": "#6daed5", "Blue 4": "#9ac7e1",
    "Red 1": "#fcb196", "Red 2": "#fc8767", "Red 3": "#fcbaa1", "Red 4": "#fedccd",
    "Green 1": "#e4f5df", "Green 2": "#c6e8bf", "Green 3": "#c8e9c2", "Green 4": "#d7f0d2"
}
trialOrder = ['Blue 1', 'Blue 2', 'Blue 3', 'Blue 4', 'Green 1', 'Green 2', 'Green 3', 'Green 4', 'Red 1', 'Red 2', 'Red 3', 'Red 4'] # Just to order the output csv to look at

def getCorrectAnswer(trial_id):
    answer = correct_answers[trial_id.lower().replace(' ', '_')]
    return answer

def calcLog2Err(row):
    response = int(row['answer'])
    correct_answer = int(row['correct_answer'])
    if response - correct_answer == 0:
        return 0
    return (np.log2(abs(response - correct_answer) + (1/8)))

df = pd.read_csv('color-perception_all_tidy.csv')

df_responses = df[df['responseId'] == 'html-response']
df_responses['correct_answer'] = df_responses['trialId'].apply(getCorrectAnswer)
df_responses['error'] = df_responses.apply(calcLog2Err, axis=1)
df_responses['trialId'] = pd.Categorical(df_responses['trialId'], categories=trialOrder, ordered=True)
df_mean_error = df_responses.groupby('trialId', observed=False)["error"].agg(mean_error=np.mean)
df_responses = df_responses.merge(df_mean_error, on='trialId')
df_responses = df_responses.sort_values(by=['participantId', 'trialId'])
df_responses.to_csv('color-perception_log2_error.csv', index=False)
print(df_responses.head())

dataSummary = df_responses.groupby('trialId', observed=False)["error"].agg([np.mean, np.std, np.count_nonzero])
dataSummary.to_csv('color-perception_log2_error_summary.csv')

sns.barplot(
    data=df_responses, x='trialId', y='error', estimator=np.mean, errorbar=('ci'),capsize=0.25, palette=custom_palette, hue='trialId'
)

plt.xticks(rotation=45)
plt.ylabel("Mean Log2 Error")
plt.title("Visualization Performance")
plt.show() 

plt.figure()  

performance_order = df_mean_error.sort_values('mean_error').index.tolist()

df_responses['trialId_by_performance'] = pd.Categorical(df_responses['trialId'], categories=performance_order, ordered=True)

sns.barplot(
    data=df_responses, x='trialId_by_performance', y='error', estimator=np.mean, 
    errorbar=('ci'), capsize=0.25, palette=custom_palette, hue='trialId_by_performance'
)

plt.xticks(rotation=45)
plt.ylabel("Mean Log2 Error")
plt.title("Visualization Performance")
plt.show()