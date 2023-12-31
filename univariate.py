import pandas as pd
from textblob import TextBlob

# Load the CSV file into a DataFrame
df = pd.read_excel("filepath", engine='openpyxl')

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

# Apply sentiment analysis to the 'AQ' column
df['What have you gained from this course?'] = df['What have you gained from this course?'].astype(str)
print(df['What have you gained from this course?'].isna().sum())  # This will print the number of NaN or missing values in 'AQ' column
df = df.dropna(subset=['What have you gained from this course?'])
df['What have you gained from this course?'].fillna("", inplace=True)
df['Sentiment'] = df['What have you gained from this course?'].apply(get_sentiment)

# Splitting sentiment into polarity and subjectivity
df['Polarity'] = df['Sentiment'].apply(lambda x: x.polarity)
df['Subjectivity'] = df['Sentiment'].apply(lambda x: x.subjectivity)

# Displaying results
print(df[['What have you gained from this course?', 'Polarity', 'Subjectivity']])


# Save the results back to a new CSV file
df.to_csv('filepath.csv', index=False)
