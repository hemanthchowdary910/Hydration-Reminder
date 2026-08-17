# 💧 Hydration Reminder

A simple Windows hydration reminder built with Python. It sends a desktop notification and plays a custom sound at scheduled intervals.

## ✨ Features

- 🔔 Desktop notifications
- 🔊 Custom reminder sound
- 💧 Custom notification icon
- ⏰ Automatic scheduling with Windows Task Scheduler
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
3. Install the dependency:

```bash
pip install -r requirements.txt
```

4. Test the program:

```bash
python Main.py
```

## ⏰ Automatic Reminders

The script sends one notification and exits.  
For recurring reminders, use **Windows Task Scheduler**.

### Quick Setup

1. Open **Task Scheduler** → **Create Task**.
2. Name it `Hydration Reminder`.
3. In **Triggers**, choose your desired schedule and enable **Repeat task every**.
4. In **Actions → New**, choose **Start a program**.
5. Select your `pythonw.exe`.
6. In **Add arguments**, enter the path to `Main.py`.
7. In **Start in**, enter the project folder.
8. Click **OK** and use **Run** to test it.

> Use `pythonw.exe` instead of `python.exe` to prevent a terminal window from opening.

## 📝 Notes

- Windows only.
- Keep `Main.py`, `water drop.ico`, and `water.wav` in the same folder.
- The reminder interval is controlled by Task Scheduler.

## 👨‍💻 Author

**Hemanth**

Built with Python 🐍