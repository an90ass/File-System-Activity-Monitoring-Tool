# File System Monitoring Tool

## 📌 Overview
This Python script monitors file system activity in a specified directory, detecting and logging file creation, deletion, modification, and movement events. It enhances security by sending real-time notifications to a Telegram bot, ensuring users stay informed about critical file changes.

## 🚀 Features
- **Real-Time Monitoring**: Tracks changes in directories and subdirectories.
- **Comprehensive Logging**: Records all detected events for audit and review.
- **Instant Telegram Alerts**: Sends immediate notifications to your Telegram chat, keeping you informed of suspicious activity.
- **File Movement Detection**: Identifies file renames and movements by correlating related events.

## 📋 Requirements
- **Python 3.x**
- **Watchdog Library**: `pip install watchdog`
- **Requests Library**: `pip install requests`

## ⚙️ Setup
1. **Clone the Repository**
      ```bash
      git clone https://github.com/an90ass/File-System-Activity-Monitoring-Tool.git
      cd File-System-Activity-Monitoring-Tool

2. **Install the required dependencies**
    ```bash
    pip install -r requirements.txt

3. **Configure the Script**
Edit the following fields in the script to specify paths and Telegram credentials:
    ```bash
    path = "your_directory_path"
    TK = 'your_telegram_bot_token'
    ID = your_chat_id
    log_file_path = "path_to_log_file"

  ## ▶️ Usage
  Run the script to continuously monitor the directory:
  
        python anasAlmaqtari_cyber security_term_project.py
  
  ## 🔧 Configuration Options

- path: Directory to be monitored.

- log_file_path: Path to store log entries.

- TK: Telegram bot token.

- ID: Telegram chat ID to receive alerts.



<sub>Feel free to customize the paths and credentials to suit your environment. This tool provides an efficient way to safeguard sensitive files and monitor unexpected changes.
Happy Monitoring! 🛡️</sub>

