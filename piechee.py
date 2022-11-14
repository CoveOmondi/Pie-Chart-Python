
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('movies.csv')
name_data = df["name"]
score_data = df["score"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0, 0)
plt.pie(score_data, labels=name_data, explode=explode, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("The top 5 rated movies\n"+"of all Time (Source - IMDB)")
plt.show()