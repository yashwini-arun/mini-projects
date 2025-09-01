import csv
import json
import logging
import time
import datetime
from collections import Counter
import random
import sys
import os

# ---------------- Logging Setup ----------------
logging.basicConfig(filename="twin_activity.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# ---------------- Decorator ----------------
def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"{func.__name__} executed in {end-start:.4f}s")
        print(f"⚡ {func.__name__} ran in {end-start:.4f}s")
        return result
    return wrapper

# ---------------- Utilities ----------------
def my_map(func, iterable):
    return [func(x) for x in iterable]

def my_filter(func, iterable):
    return [x for x in iterable if func(x)]

def flatten(nested):
    for i in nested:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i

# ---------------- OOP: DailyLog & Twin ----------------
class DailyLog:
    def __init__(self, date, mood, activity):
        self.date = date
        self.mood = mood
        self.activity = activity

class Twin:
    def __init__(self, name, csv_file="yashwini_twin.csv"):
        self.name = name
        self.logs = []
        self.csv_file = csv_file
        self.load_logs()

    def load_logs(self):
        if os.path.exists(self.csv_file):
            with open(self.csv_file, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.logs.append(DailyLog(row["date"], row["mood"], row["activity"]))
            if self.logs:
                last = self.logs[-1]
                print(f"👋 Welcome back {self.name}! "
                      f"Yesterday you felt '{last.mood}' and did '{last.activity}'.")
        else:
            print(f"✨ Hello {self.name}, I’m your new AI Twin. Let’s start logging your life!")

    def save_logs(self):
        with open(self.csv_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["date","mood","activity"])
            writer.writeheader()
            for log in self.logs:
                writer.writerow({"date": log.date, "mood": log.mood, "activity": log.activity})

    @timed
    def add_log(self, mood, activity):
        today = str(datetime.date.today())
        log = DailyLog(today, mood, activity)
        self.logs.append(log)
        self.save_logs()
        logging.info(f"Added log: mood={mood}, activity={activity}")
        print(f"✅ {self.name} saved your day!")

    def replay_week(self):
        print("\n📅 Your last 7 logs:")
        for log in self.logs[-7:]:
            yield f"{log.date} → Mood: {log.mood}, Activity: {log.activity}"

class SmartTwin(Twin):
    def analyze_patterns(self):
        if not self.logs:
            return "No data yet!"

        activities = [log.activity for log in self.logs]
        counts = Counter(activities).most_common()
        max_count = counts[0][1]
        top_acts = [act for act, c in counts if c == max_count]

        latest = self.logs[-1].activity

        if len(top_acts) == 1:
            return (f"🤖 You often do '{top_acts[0]}' ({max_count} times). "
                    f"But most recently, you did '{latest}'.")
        else:
            return (f"🤖 You often do {', '.join(top_acts)} ({max_count} times each). "
                    f"But most recently, you did '{latest}'.")

    def chat(self):
        if not self.logs:
            return "👋 Hey! Start logging so I can get to know you better."

        latest = self.logs[-1]
        moods = [log.mood for log in self.logs[-5:]]
        mood_summary = Counter(moods).most_common(1)[0][0]

        comments = [
            f"👯 I feel what you feel. Right now you’re '{latest.mood}', right?",
            f"📖 Last time you logged, you did '{latest.activity}'. Did you enjoy it?",
            f"📊 Recently, your most common mood is '{mood_summary}'. Interesting!",
            "✨ You’re building me as your twin. I’m becoming more like you every day.",
            "🔮 I think you’ll be coding late tonight!",
            "💡 Remember: consistency beats motivation. Keep going!",
            "🔥 Fun fact: you’ve logged {} days so far!".format(len(self.logs))
        ]

        return "\n".join(random.sample(comments, 3))

    def export_json(self, json_file="yashwini_twin.json"):
        data = [{"date": log.date, "mood": log.mood, "activity": log.activity} for log in self.logs]
        with open(json_file, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Exported twin’s memory to {json_file}")

# ---------------- Inline Tests ----------------
def run_tests():
    assert my_map(lambda x: x+1, [1,2]) == [2,3]
    assert my_filter(lambda x: x>2, [1,2,3]) == [3]
    flat = list(flatten([1,[2,[3]]]))
    assert flat == [1,2,3]
    print("✅ All inline tests passed!")

# ---------------- Main ----------------
if __name__ == "__main__":
    run_tests()
    my_twin = SmartTwin("Yashwini")

    while True:
        print("\n=== HoloDesk – Your AI Digital Twin 🪞 ===")
        print("1. Add Today’s Log")
        print("2. Replay Past Week")
        print("3. Analyze My Patterns")
        print("4. Mood Trends")
        print("5. Habit Streak Tracker")
        print("6. Search Past Logs")
        print("7. Activity Category Stats")
        print("8. Smart Reminder")
        print("9. Export My Memory to JSON")
        print("10. Demo Flatten/List Utils")
        print("11. Talk to Your Twin")
        print("12. Exit")

        choice = input("Choose: ")

        if choice == "1":
            mood = input("How are you feeling? ")
            activity = input("What did you do today? ")
            my_twin.add_log(mood, activity)

        elif choice == "2":
            for entry in my_twin.replay_week():
                print(entry)

        elif choice == "3":
            print(my_twin.analyze_patterns())

        elif choice == "4":
            moods = [log.mood for log in my_twin.logs[-7:]]
            print("📊 Mood Trends (last 7 days):", dict(Counter(moods)))

        elif choice == "5":
            if my_twin.logs:
                last_activity = my_twin.logs[-1].activity
                streak = 1
                for log in reversed(my_twin.logs[:-1]):
                    if log.activity == last_activity:
                        streak += 1
                    else:
                        break
                print(f"🔥 You’re on a {streak}-day streak of '{last_activity}'!")
            else:
                print("No logs yet!")

        elif choice == "6":
            keyword = input("Enter a keyword to search: ")
            results = [f"{log.date} → Mood: {log.mood}, Activity: {log.activity}" 
                       for log in my_twin.logs if keyword.lower() in log.activity.lower() or keyword.lower() in log.mood.lower()]
            print("\n".join(results) if results else "❌ No matches found.")

        elif choice == "7":
            categories = {"Health": ["gym","yoga","running"],
                          "Learning": ["study","coding","reading"],
                          "Fun": ["dance","music","movie"],
                          "Rest": ["sleep","nap","rest"]}
            stats = {cat:0 for cat in categories}
            for log in my_twin.logs:
                for cat, acts in categories.items():
                    if log.activity.lower() in acts:
                        stats[cat] += 1
            print("📌 Activity Categories:", stats)

        elif choice == "8":
            if my_twin.logs:
                suggestion = my_twin.logs[-1].activity
                print(f"⏰ Around this time, you often do '{suggestion}'. Want to do it today?")
            else:
                print("No data yet for reminders.")

        elif choice == "9":
            my_twin.export_json()

        elif choice == "10":
            print("Flatten Demo:", list(flatten([1,[2,[3,4]],5])))
            print("Custom Map Demo:", my_map(lambda x:x*2, [1,2,3]))
            print("Custom Filter Demo:", my_filter(lambda x:x%2==0, [1,2,3,4]))

        elif choice == "11":
            print("\n🤖 Your Twin says:\n")
            print(my_twin.chat())

        elif choice == "12":
            print("👋 Goodbye, I’ll remember you next time!")
            sys.exit()

        else:
            print("❌ Invalid choice, try again.")
