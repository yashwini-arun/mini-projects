# 🪞 HoloDesk – Your AI Digital Twin  

**HoloDesk** is a Python-based **AI Digital Twin** that logs your daily life, analyzes patterns, and interacts with you like a personal assistant.  
It combines **OOP, decorators, logging, CSV/JSON storage, and smart insights** to build a memory of your habits, moods, and activities.  

---

## ✨ Features  

### 📝 Logging & Memory
- Saves daily **mood** and **activity** with timestamp.  
- Persists memory in **CSV** (structured logs).  
- Can export memory to **JSON** for portability.  
- **Smart welcome back**: Reminds you of yesterday’s mood & activity.  

### 🧩 Core Utilities
- `my_map`, `my_filter`, and `flatten` – custom functional utilities.  
- `@timed` decorator logs & prints function runtime ⏱️.  
- Built-in inline **tests** ✅ for reliability.  

### 📊 Analytics & Insights
- 📅 **Replay last 7 days** of logs.  
- 📈 **Mood trends** (last 7 days).  
- 🔥 **Habit streak tracker** (track repeating activities).  
- 📌 **Activity categories** (Health, Learning, Fun, Rest).  
- ⏰ **Smart reminders**: Suggests what you usually do around this time.  
- 🤖 **Pattern analysis**: Finds most frequent activities.  

### 💬 Interactive AI Twin
- Engages in small talk based on your logs.  
- Comments on moods, activities, and consistency.  
- Offers motivational nudges & fun insights.  

---

## 💻 Menu Options  

When you run the program, you get an interactive menu:  

1. **Add Today’s Log**  
2. **Replay Past Week**  
3. **Analyze My Patterns**  
4. **Mood Trends**  
5. **Habit Streak Tracker**  
6. **Search Past Logs**  
7. **Activity Category Stats**  
8. **Smart Reminder**  
9. **Export My Memory to JSON**  
10. **Demo Flatten/List Utils**  
11. **Talk to Your Twin**  
12. **Exit**

  
---

## ⚙️ How It Works  

1. Run the program → Interactive menu appears.  
2. Start logging your **daily mood & activity**.  
3. Data is saved to `yashwini_twin.csv`.  
4. Over time, your **AI Twin learns your habits**.  
5. Use analytics features to get insights into your behavior.  

---

## 📂 File Outputs  

- `yashwini_twin.csv` → stores logs (date, mood, activity).  
- `yashwini_twin.json` → exported memory in JSON.  
- `twin_activity.log` → logs execution times & important events.  

---

## 🚀 Getting Started  

### 🔧 Requirements
- Python 3.x  
- Standard libraries only (`csv`, `json`, `logging`, `datetime`, etc.)  

### ▶️ Run
```bash
python AI_Twin.py

