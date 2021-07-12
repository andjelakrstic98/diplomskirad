import pandas as pd
import matplotlib
import seaborn as sns
from textblob import TextBlob

bloblist_desc = list()
df_comments = pd.read_csv (r'./all_comments.csv')
df=pd.DataFrame


for row in df_comments:
    blob = TextBlob(row)
    bloblist_desc.append((row,blob.sentiment.polarity, blob.sentiment.subjectivity))
    df_comments_polarity_desc = pd.DataFrame(bloblist_desc, columns = ['sentence','sentiment','polarity'])
 
def f(df_comments_polarity_desc):
    if df_comments_polarity_desc['sentiment'] > 0:
        val = "Pozitivni"
    elif df_comments_polarity_desc['sentiment'] == 0:
        val = "Neutralni"
    else:
        val = "Negativni"
    return val

df_comments_polarity_desc['Sentiment_Type'] = df_comments_polarity_desc.apply(f, axis=1)

plt.figure(figsize=(10,10))
sns.set_style("whitegrid")
ax = sns.countplot(x="Sentiment_Type", data=df_comments_polarity_desc)
