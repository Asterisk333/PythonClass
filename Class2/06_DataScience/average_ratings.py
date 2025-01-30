import pandas as pd
from clean_data import clean_data
import matplotlib.pyplot as plt

plt.figure()

ratings = clean_data(pd.read_csv('amazon.csv'))


def average_ratings(ratings):
    # average ratings
    avg10 = ratings['rating_count'].sort_values(ascending=False).head(10).mean(axis=0)
    avg100 = ratings['rating_count'].sort_values(ascending=False).head(100).mean(axis=0)
    avg250 = ratings['rating_count'].sort_values(ascending=False).head(250).mean(axis=0)

    # Return as a DataFrame for plotting
    return pd.DataFrame({
        'Category': ['Top 10', 'Top 100', 'Top 250'],
        'Average Rating': [avg10, avg100, avg250]
    })


# Get the average ratings
df = average_ratings(ratings)

# Plot the bar chart
df.plot(kind='bar', x='Category', y='Average Rating', legend=False)

# Save the plot as an image file (e.g., PNG)
plt.title('Average Ratings for Top 10, 100, and 250')
plt.ylabel('Average Rating')
plt.xlabel('Category')
plt.show()
plt.close()  # Close the plot after saving to free up memory
