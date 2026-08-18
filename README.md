# 💧 Hydration Reminder

A simple Windows hydration reminder built with Python. It sends a desktop notification and plays a custom sound at scheduled intervals.

## ✨ Features

- 🔔 Desktop notifications
- 🔊 Custom reminder sound
- 💧 Custom notification icon
- ⏰ Automatic reminders using Windows Task Scheduler
- 🖥️ Runs without keeping VS Code or a terminal open

## 🛠️ Built With

- Python
- Plyer
- Winsound
- Windows Task Scheduler

## 📁 Project Structure

```text
Hydration_Notification/
├── Main.py
├── requirements.txt
├── water drop.ico
├── water drop.png
└── water.wav
```

## ⚙️ Installation

1. Download and extract the project.
2. Open PowerShell in the project folder.
3. Install the required package:

```bash
pip install -r requirements.txt
```

4. Test the program:

```bash
python Main.py
```

The notification should appear and the reminder sound should play.

## ⏰ Automatic Reminders

`Main.py` sends **one notification and exits**.

Windows **Task Scheduler** is used to automatically run the script.

### Task Scheduler Setup

1. Open **Task Scheduler** → **Create Task**.
2. Name it `Hydration Reminder`.
3. Under **Triggers**, choose **At startup**.
4. Enable **Repeat task every: 2 hours** and set the duration to **Indefinitely**.
5. Under **Actions → New**, select **Start a program**.
6. Select your `pythonw.exe`.
7. In **Add arguments**, enter the path to `Main.py`.
8. In **Start in**, enter the project folder.
9. Under **Conditions**, disable **Start the task only if the computer is on AC power** if you want it to work on battery.
10. Save the task and use **Run** to test it.

> Use `pythonw.exe` instead of `python.exe` to prevent a terminal window from opening.

Once configured, Windows can run the reminder automatically without VS Code or a terminal running in the background.

## 📝 Notes

- Designed for **Windows**.
- `winsound` is included with Python.
- Keep `Main.py`, `water drop.ico`, and `water.wav` in the same folder.
- The reminder interval is controlled by **Task Scheduler**.

## 👨‍💻 Author

**Hemanth**

Built with Python 🐍

💧 Stay hydrated!