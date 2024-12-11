import pandas as pd
from collections import Counter
import re

# Replace 'your_file.csv' with the actual file path
csv_file_path = 'Keyword1.csv'

# Specify the correct encoding
csv_encoding = 'utf-8'  # Replace with the appropriate encoding if needed

# Read the CSV file with the specified encoding
df = pd.read_csv(csv_file_path, encoding=csv_encoding)

# Combine text data from the 'text_column'
text_data = ' '.join(df['Keyword'])

# Preprocess the text data
text_data = text_data.lower()
text_data = re.sub(r'[^\w\s]', '', text_data)
words = text_data.split()

# Count recurring words
word_counts = Counter(words)

# Find most common words
top_words = word_counts.most_common(10)  # Change the number as needed

# Display results
for word, count in top_words:
    print(f"{word}: {count} occurrences")
