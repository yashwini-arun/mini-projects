
import os
import math
from collections import Counter

def read_scores(file_path):
    
    scores = []
    if not os.path.exists(file_path):
        print("File does not exist.")
        return scores

    with open(file_path, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            name, score = line.strip().split(",")
            scores.append((name, int(score)))  # Casting string to int
    return scores

def calculate_statistics(scores):
    
    score_values = [score for name, score in scores]
    score_values.sort()
    n = len(score_values)

    # Highest and lowest
    highest = max(score_values)
    lowest = min(score_values)

    # Average
    average = sum(score_values) / n

    # Median
    if n % 2 == 0:
        median = (score_values[n//2 - 1] + score_values[n//2]) / 2
    else:
        median = score_values[n//2]

    # Mode
    counter = Counter(score_values)
    max_count = max(counter.values())
    if max_count == 1:
        mode = "No mode"
    else:
        mode = [score for score, count in counter.items() if count == max_count]

    # Variance & Standard deviation
    variance = sum((x - average)**2 for x in score_values) / n
    std_dev = math.sqrt(variance)

    # Pass/fail count (assuming pass >= 40)
    pass_count = sum(1 for s in score_values if s >= 40)
    fail_count = n - pass_count

    # Grade distribution
    grade_dist = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for score in score_values:
        if score >= 90:
            grade_dist["A"] += 1
        elif score >= 80:
            grade_dist["B"] += 1
        elif score >= 70:
            grade_dist["C"] += 1
        elif score >= 60:
            grade_dist["D"] += 1
        else:
            grade_dist["F"] += 1

    # Top 3 students
    top_students = sorted(scores, key=lambda x: x[1], reverse=True)[:3]

    return {
        "highest": highest,
        "lowest": lowest,
        "average": average,
        "median": median,
        "mode": mode,
        "variance": variance,
        "std_dev": std_dev,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "grade_dist": grade_dist,
        "top_students": top_students
    }

def display_statistics(scores):
    """Display all statistics"""
    if not scores:
        print("No scores to display.")
        return
    stats = calculate_statistics(scores)

    print(f"\nTotal students: {len(scores)}")
    print(f"Highest score : {stats['highest']}")
    print(f"Lowest score  : {stats['lowest']}")
    print(f"Average score : {stats['average']:.2f}")
    print(f"Median score  : {stats['median']:.2f}")
    print(f"Mode score(s) : {stats['mode']}")
    print(f"Variance      : {stats['variance']:.2f}")
    print(f"Std. Deviation: {stats['std_dev']:.2f}")
    print(f"Pass count    : {stats['pass_count']}")
    print(f"Fail count    : {stats['fail_count']}\n")

    print("Grade Distribution:")
    for grade, count in stats['grade_dist'].items():
        print(f"{grade}: {count}")

    print("\nTop 3 Students:")
    for name, score in stats['top_students']:
        print(f"{name}: {score}")

def main():
    
    while True:
        print("\n--- Grade Analyzer ---")
        print("1. Analyze scores from file")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            file_path = input("Enter file name (e.g., scores.txt): ")
            scores = read_scores(file_path)
            display_statistics(scores)
        elif choice == "2":
            print("Exiting Grade Analyzer. Thankyou!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
