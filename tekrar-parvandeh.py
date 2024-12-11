import pandas as pd
from collections import Counter
import re

# Replace 'your_file.csv' with the actual file path
csv_file_path = '43.csv'

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
top_words = word_counts.most_common(100)  # Change the number as needed

# Specify the output file path
output_file_path = 'Natijeh.txt'

# Open the output file for writing with RTL characters
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Write the results to the file in RTL format
    for word, count in top_words:
        # Add RTL embedding characters
        rtl_line = f"\u202B{count} :{word}\u202C"
        output_file.write(rtl_line + '\n')

print(f"Results written to {output_file_path}")
