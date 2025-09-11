
import pandas as pd

# Load dataset
df = pd.read_csv("sample_grades.csv")

# Calculate average, highest, lowest per subject
print("Subject-wise Statistics:")
for subject in df.columns[1:]:
    print(f"\n{subject}:")
    print(f"  Average: {df[subject].mean():.2f}")
    print(f"  Highest: {df[subject].max()}")
    print(f"  Lowest : {df[subject].min()}")

# Calculate average score per student
df["Average"] = df.iloc[:, 1:].mean(axis=1)

# Add Pass/Fail column (threshold 40)
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Display top 3 students
top_students = df.sort_values(by="Average", ascending=False).head(3)

print("\nTop 3 Students by Average Score:")
print(top_students[["Name", "Average", "Result"]])

# Save updated results to file
df.to_csv("student_results.csv", index=False)
print("\nUpdated results saved to student_results.csv")
