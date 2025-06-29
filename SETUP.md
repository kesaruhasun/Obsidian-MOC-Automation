# Automated Obsidian MOC Generation Setup

This document will guide you through setting up an automated system to generate Maps of Content (MOCs) for your Obsidian vault. This script will create `_MOC.md` files in each of your folders, linking to all Markdown files and subfolders within them.

## What is this script?

The `generate_mocs.py` script is a Python program that scans your Obsidian vault. For every folder that contains Markdown files or other subfolders, it creates a special Markdown file (an MOC) that lists and links to all the content within that folder. This helps you navigate your notes and visualize connections in Obsidian's graph view.

## Why automate it?

As you add new notes and folders, manually updating MOCs can be tedious. Automating this process ensures your MOCs are always up-to-date, keeping your vault organized effortlessly.

## Setup Instructions

### Step 1: Ensure Python is Installed

This script requires Python 3. Most modern operating systems (macOS, Linux) come with Python pre-installed. For Windows, you might need to install it.

*   **How to check:** Open your terminal or command prompt and type:
    ```bash
    python3 --version
    ```
    or
    ```bash
    python --version
    ```
    If you see a version number (e.g., `Python 3.x.x`), you're good to go! If not, follow the instructions below for your operating system.

*   **Installing Python (if needed):**
    *   **macOS:** Python is usually pre-installed. If you need a newer version, consider using Homebrew: `brew install python3`
    *   **Linux:** Python is usually pre-installed. If not, use your distribution's package manager (e.g., `sudo apt install python3` on Ubuntu/Debian, `sudo yum install python3` on Fedora/RHEL).
    *   **Windows:** Download the installer from the official Python website: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
        *   **IMPORTANT:** During installation, make sure to check the box that says "Add Python to PATH". This is crucial for running Python commands from any directory.

### Step 2: Place the Script

The `generate_mocs.py` script is already located in:
`/Users/kesaru/Documents/Obsidian Vault/obsidian-vault/Journal/Projects/MOC_Automation/generate_mocs.py`

**Important Note on Portability:**
The script is designed to be portable. It automatically detects the root of your Obsidian vault by looking at its own location. This means if you move or clone your entire Obsidian vault to a different location or a new computer, the script should still work without needing manual path adjustments.

### Step 3: Test the Script (Manual Run)

Before automating, let's make sure the script runs correctly.

1.  Open your terminal or command prompt.
2.  Navigate to the `MOC_Automation` directory:
    ```bash
    cd "/Users/kesaru/Documents/Obsidian Vault/obsidian-vault/Journal/Projects/MOC_Automation"
    ```
3.  Run the script:
    ```bash
    python3 "/Users/kesaru/Documents/Obsidian Vault/obsidian-vault/Journal/Projects/MOC_Automation/generate_mocs.py"
    ```
    (If `python3` doesn't work, try `python` instead).

After running, check some of your folders in Obsidian. You should see new `_MOC.md` files appearing (e.g., `Journal_MOC.md`, `Projects_MOC.md`, etc.).

### Step 4: Automate Daily MOC Generation

Now, let's set up the script to run automatically every day.

#### For macOS and Linux (using Cron)

Cron is a time-based job scheduler in Unix-like operating systems.

1.  **Open your crontab for editing:**
    ```bash
    crontab -e
    ```
    If it's your first time, it might ask you to choose an editor (e.g., `nano`, `vim`). `nano` is generally easier for beginners.

2.  **Add the cron job:**
    Add the following line to the end of the file. This command will run the script every day at 3:00 AM.

    ```cron
    0 3 * * * /usr/bin/python3 "/Users/kesaru/Documents/Obsidian Vault/obsidian-vault/Journal/Projects/MOC_Automation/generate_mocs.py" >> "/Users/kesaru/Documents/Obsidian Vault/obsidian-vault/Journal/Projects/MOC_Automation/moc_log.log" 2>&1
    ```
    *   `0 3 * * *`: This means "at 0 minutes past 3 AM, every day of every month, every day of the week."
    *   `/usr/bin/python3`: This is the full path to your Python 3 executable. You can find this by typing `which python3` (or `which python`) in your terminal. Replace this path if yours is different.
    *   `"/Users/kesaru/Documents/Obsidian Vault/obsidian-vault/Journal/Projects/MOC_Automation/generate_mocs.py"`: The full path to your script.
    *   `>> "/Users/kesaru/Documents/Obsidian Vault/obsidian-vault/Journal/Projects/MOC_Automation/moc_log.log" 2>&1`: This redirects all output (standard output and errors) to a log file named `moc_log.log` within your `MOC_Automation` folder. This is useful for troubleshooting.

3.  **Save and Exit:**
    *   If using `nano`: Press `Ctrl + O` (to write out), then `Enter`, then `Ctrl + X` (to exit).
    *   If using `vim`: Press `Esc`, then type `:wq` (write and quit), then `Enter`.

Your cron job is now scheduled!

#### For Windows (using Task Scheduler)

Task Scheduler allows you to automate tasks on Windows.

1.  **Open Task Scheduler:**
    *   Press `Win + R`, type `taskschd.msc`, and press `Enter`.
    *   Alternatively, search for "Task Scheduler" in the Start Menu.

2.  **Create a Basic Task:**
    *   In the right-hand "Actions" pane, click "Create Basic Task...".
    *   **Name:** `Obsidian MOC Generator` (or anything descriptive).
    *   **Description:** `Automatically generates Maps of Content for Obsidian vault.`
    *   Click `Next`.

3.  **Trigger:**
    *   Select `Daily`.
    *   Click `Next`.
    *   **Start:** Choose a date and time (e.g., 3:00 AM).
    *   **Recur every:** `1` day.
    *   Click `Next`.

4.  **Action:**
    *   Select `Start a program`.
    *   Click `Next`.

5.  **Program/script:**
    *   **Program/script:** Type the full path to your Python executable.
        *   Example: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python39\python.exe`
        *   **How to find it:** Open Command Prompt and type `where python` or `where python3`. Use the path that ends with `python.exe`.
    *   **Add arguments (optional):** Type the full path to your script, enclosed in double quotes.
        *   Example: `"/Users/kesaru/Documents/Obsidian Vault/obsidian-vault/Journal/Projects/MOC_Automation/generate_mocs.py"`
    *   **Start in (optional):** Type the directory where your script is located.
        *   Example: `"/Users/kesaru/Documents/Obsidian Vault/obsidian-vault/Journal/Projects/MOC_Automation"`

6.  **Finish:**
    *   Click `Next`, then `Finish`.

Your task is now scheduled! You can right-click the task in Task Scheduler and select "Run" to test it immediately.

## Troubleshooting

*   **Script not running:**
    *   **Check paths:** Double-check all file paths in your cron job or Task Scheduler entry. Even a small typo can prevent it from running.
    *   **Permissions:** Ensure the script (`generate_mocs.py`) has execute permissions (on macOS/Linux, run `chmod +x generate_mocs.py` in its directory).
    *   **Python environment:** Make sure the `python3` (or `python`) command in your cron job/Task Scheduler points to the correct Python installation.
    *   **Log file:** Check the `moc_log.log` file (or Task Scheduler's "History" tab) for any error messages.

*   **MOCs not updating/appearing:**
    *   Run the script manually (Step 3) to see if it works.
    *   Ensure the script's `vault_root` variable correctly points to your Obsidian vault's root directory. The current script assumes `MOC_Automation` is inside `Journal/Projects/` which is inside your vault root. If your vault structure is different, you might need to adjust the `vault_root` line in `generate_mocs.py`.

## Future Enhancements (Manual)

While this script automates the basic MOC generation, you can further enhance your Obsidian experience:

*   **Manual Interlinking:** As discussed, for a "Wikipedia-like" interconnectedness, you will need to manually add more `[[internal links]]` within your individual notes, connecting related concepts, tasks, or resources across different projects.
*   **Tags:** Continue using tags (`#tag`) to categorize notes.
*   **YAML Frontmatter:** Add YAML frontmatter to your notes for structured metadata (e.g., `status: in-progress`, `project: Kiwlor-Mobile-App`). This can be used with Obsidian plugins like Dataview for powerful queries.

This automated system should provide a solid foundation for keeping your Obsidian vault organized!
