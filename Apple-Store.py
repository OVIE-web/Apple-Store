# Import necessary libraries for data analysis and visualization

# Pandas: Used for handling and analyzing structured data efficiently
import pandas as pd
# OS: Provides functions to interact with the operating system (file paths, directory handling, etc.)
import os
# Matplotlib: A fundamental plotting library for creating static, animated, and interactive visualizations
import matplotlib.pyplot as plt
# Seaborn: Built on top of Matplotlib, enhances visualization aesthetics and statistical plots
import seaborn as sns
# Langdetect: Detects language from text; useful for filtering non-English apps or data
from langdetect import detect
# Set Seaborn style for enhanced visualization aesthetics
sns.set(style="whitegrid")




# Define the file path to the AppleStore CSV data
file_path = r"C:\Users\oviem\OneDrive\Desktop\CSV_FiLES\AppleStore.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first five rows
print("First five rows:")
print(df.head())

# Display the last five rows
print("\nLast five rows:")
print(df.tail())

# Display the data types of the DataFrame columns
print("\nData Types:")
print(df.dtypes)

# List all column names
print("\nColumns:")
print(df.columns)

# Display unique values for 'prime_genre' and 'currency'
print("\nUnique Genres:")
print(df['prime_genre'].unique())
print("\nUnique Currencies:")
print(df['currency'].unique())



# Plot histogram for the distribution of user ratings
sns.histplot(df['user_rating'], bins=10)
plt.xlabel('User Rating')
plt.ylabel('Frequency')
plt.title('Distribution of User Ratings')
plt.show()

# Identify the apps with the highest user ratings
top_rated_apps = df[df['user_rating'] == df['user_rating'].max()]
print("\nTop Rated Apps:")
print(top_rated_apps[['track_name', 'user_rating', 'prime_genre']])


# Function to detect if a string is in English
def is_english(name):
    try:
        return detect(name) == 'en'
    except:
        return False

# Filter out non-English apps by iterating through each row
english_apps = []
for index, row in df.iterrows():
    if is_english(row['track_name']):
        english_apps.append(row)

# Create a new DataFrame with only English apps
df_english = pd.DataFrame(english_apps)

# Display the first few rows of the cleaned English apps DataFrame
print("Filtered English Apps:")
print(df_english.head())
print(df_english.tail())
print(df_english.info())




# Load Path to Visualize
try:
    def load_data():
        df = pd.read_csv(file_path)
        return df
    df = load_data()  # Calling the function to assign df
except Exception as e:
    print(F"Error: {e}")
    
# Identify the top 5 genres by the count of apps
top_genres = df['prime_genre'].value_counts().head(5).index

# Calculate the average user rating for apps in these top genres
average_ratings = df[df['prime_genre'].isin(top_genres)].groupby('prime_genre')['user_rating'].mean()
print("Average User Ratings by Top Genres:")
print(average_ratings)

# Plot distribution of app sizes for each top genre
for genre in top_genres:
    sns.histplot(df[df['prime_genre'] == genre]['size_bytes'] / (1024 * 1024), bins=20, label=genre)
plt.xlabel('Size (MB)')
plt.ylabel('Frequency')
plt.title('Distribution of App Sizes by Genre')
plt.legend()
plt.show()

# Scatter plot: Total Ratings vs. User Rating for each top genre
for genre in top_genres:
    sns.scatterplot(data=df[df['prime_genre'] == genre], x='rating_count_tot', y='user_rating', label=genre)
plt.xlabel('Total Ratings')
plt.ylabel('User Rating')
plt.title('User Ratings vs. Total Ratings for Top Genres')
plt.xscale('log')
plt.legend()
plt.show()

# For each top genre, display a pie chart comparing the proportion of Free vs. Paid apps
for genre in top_genres:
    free_vs_paid = df[df['prime_genre'] == genre]['price'].apply(lambda x: 'Free' if x == 0 else 'Paid').value_counts()
    free_vs_paid.plot(kind='pie', autopct='%1.1f%%', startangle=90, title=genre)
    plt.ylabel('')
    plt.show()