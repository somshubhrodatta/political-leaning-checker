import pandas as pd
import numpy as np

# Define question indices (0-based)
left_leaning = [0, 1, 4, 5, 6, 9, 11, 13, 14, 15, 17, 19]  # Q1, Q2, Q5, Q6, Q7, Q10, Q12, Q14, Q15, Q16, Q18, Q20
right_leaning = [2, 3, 7, 8, 10, 12, 16, 18]  # Q3, Q4, Q8, Q9, Q11, Q13, Q17, Q19
labels = ['Far Left', 'Left', 'Center', 'Right', 'Far Right']
rows_per_label = 40

# Initialize data
data = []

# Generate responses
for label in labels:
    for _ in range(rows_per_label):
        answers = [3] * 20  # Start with neutral
        if label == 'Far Left':
            for i in left_leaning:
                answers[i] = np.random.choice([4, 5], p=[0.3, 0.7])
            for i in right_leaning:
                answers[i] = np.random.choice([1, 2], p=[0.7, 0.3])
        elif label == 'Left':
            for i in left_leaning:
                answers[i] = np.random.choice([3, 4, 5], p=[0.2, 0.4, 0.4])
            for i in right_leaning:
                answers[i] = np.random.choice([1, 2, 3], p=[0.4, 0.4, 0.2])
        elif label == 'Center':
            answers = [np.random.choice([2, 3, 4], p=[0.3, 0.4, 0.3]) for _ in range(20)]
        elif label == 'Right':
            for i in left_leaning:
                answers[i] = np.random.choice([1, 2, 3], p=[0.4, 0.4, 0.2])
            for i in right_leaning:
                answers[i] = np.random.choice([3, 4, 5], p=[0.2, 0.4, 0.4])
        elif label == 'Far Right':
            for i in left_leaning:
                answers[i] = np.random.choice([1, 2], p=[0.7, 0.3])
            for i in right_leaning:
                answers[i] = np.random.choice([4, 5], p=[0.3, 0.7])
        data.append(answers + [label])

# Create DataFrame
columns = [f'q{i+1}' for i in range(20)] + ['label']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('dataset.csv', index=False)
print("Dataset saved to dataset.csv")