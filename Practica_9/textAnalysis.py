import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

##I tried with word clouds, but I've been having trouble installing libraries:
## Installing backend dependencies: started
## Installing backend dependencies: finished with status 'error'
## So I just did the most common tags, which would seem bigger the more times its found

df = pd.read_csv("normalized_steam.csv").dropna(subset=["steamspy_tags"])

tags_list = []
for tags in df["steamspy_tags"].astype(str):
    split_tags = re.split(r"[,;]", tags)
    tags_list.extend([tag.strip() for tag in split_tags if tag.strip()])

tags_list = [re.sub(r"[^a-zA-Z\s]", "", tag.lower().strip()) for tag in tags_list]

stopwords = {"to", "early", "access", "the", "and", "of", "for", "in", "on", "with", "free", "play"}

filtered_tags = [tag for tag in tags_list if tag not in stopwords and len(tag) > 2]

tag_counts = Counter(filtered_tags)
top_tags = dict(tag_counts.most_common(30))

plt.figure(figsize=(12, 6))
plt.barh(list(top_tags.keys()), list(top_tags.values()), color="blue")
plt.xlabel("Frequency")
plt.ylabel("Steam Tags")
plt.title("Top Steam Game Tags")
plt.gca().invert_yaxis()
plt.savefig("wordcloud_tags.png")
plt.show()