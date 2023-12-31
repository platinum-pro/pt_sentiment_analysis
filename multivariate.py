import pandas as pd
from textblob import TextBlob

# Load the file into a DataFrame
df = pd.read_excel("filepath", engine='openpyxl')

def compute_sentiment(column):
    # Convert all entries to strings
    column = column.astype(str)

    # Apply sentiment analysis
    sentiment = column.apply(lambda x: TextBlob(x).sentiment)

    # Extract polarity and subjectivity
    polarity = sentiment.apply(lambda x: x.polarity)
    subjectivity = sentiment.apply(lambda x: x.subjectivity)

    return polarity, subjectivity


for col in ['What have you gained from this course?', 
            'What activity did you most enjoy in this course?', 
            'If you could change an aspect of the course, what would you change and how would you change it?', 
            'Are there any activities you would like to see added to the course?']:
    df[f'{col}_Polarity'], df[f'{col}_Subjectivity'] = compute_sentiment(df[col])


# Filter columns to retain only sentiment analysis results
columns_to_keep = [f'{col}_{metric}' for col in ['What have you gained from this course?', 'What activity did you most enjoy in this course?', 
                                                 'If you could change an aspect of the course, what would you change and how would you change it?', 
                                                 'Are there any activities you would like to see added to the course?'] for metric in ['Polarity', 'Subjectivity']]
results_df = df[columns_to_keep]

# Save the results to a new CSV
results_df.to_csv('filepath.csv', index=False)

