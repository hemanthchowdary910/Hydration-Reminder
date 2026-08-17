\# 💧 Hydration Reminder



A simple Windows-based hydration reminder built with Python.  

It sends a desktop notification and plays a custom sound at scheduled intervals.



\## ✨ Features



\- 🔔 Desktop hydration notifications

\- 🔊 Custom reminder sound

\- 💧 Custom notification icon

\- ⏰ Automatic scheduling with Windows Task Scheduler

\- 🖥️ Runs without keeping VS Code or a terminal open



\## 🛠️ Built With



\- Python

\- \[Plyer](https://pypi.org/project/plyer/)

\- `winsound`

\- Windows Task Scheduler



\## 📁 Project Structure



```text

Hydration\_Notification/

│

├── Main.py

├── requirements.txt

├── water drop.ico

├── water drop.png

└── water.wav

```



\## ⚙️ Installation



\### 1. Clone or download the repository



```bash

git clone <repository-url>

cd Hydration\_Notification

```



\### 2. Install the required package



```bash

pip install -r requirements.txt

```



\### 3. Run the program



```bash

python Main.py

```



You should receive a notification and hear the reminder sound.



\## ⏰ Automatic Reminders



The Python script sends \*\*one notification and exits\*\*.



For recurring reminders, Windows \*\*Task Scheduler\*\* is used to run `Main.py` at a chosen interval.



Example:



```text

Task Scheduler

&#x20;     ↓

Every 2 hours

&#x20;     ↓

Main.py

&#x20;     ↓

🔔 Notification + 🔊 Sound

&#x20;     ↓

Program exits

```



Using Task Scheduler means the Python program does not need to continuously run in the background.



\## 📝 Notes



\- Designed for \*\*Windows\*\*.

\- `winsound` is included with Python and does not need to be installed separately.

\- Keep `Main.py`, `water drop.ico`, and `water.wav` in the same folder.

\- The reminder interval can be changed through Windows Task Scheduler.



\## 👨‍💻 Author



\*\*Hemanth\*\*



Built with Python 🐍

