# Obsidian MOC Automation ✨

## Automate Your Maps of Content (MOCs) for a Super Organized Obsidian Vault! 🚀

Are you an Obsidian user who loves the power of Maps of Content (MOCs) but finds manually updating them a chore? This simple yet powerful Python script is here to save your day! 🤖 It automatically generates and updates MOC files in your Obsidian vault, ensuring your notes are always interconnected and easy to navigate.

---

### What are MOCs? 🤔

Maps of Content (MOCs) are a fantastic way to organize your notes in Obsidian. Think of them as curated indexes or tables of contents for specific topics, projects, or areas of your knowledge. They link to related notes, helping you see the bigger picture and discover connections you might otherwise miss.

### Why Automate? 💡

As your Obsidian vault grows, keeping MOCs up-to-date can become a tedious task. New notes, renamed files, or restructured folders mean constant manual adjustments. This automation script takes that burden off your shoulders!

*   **Always Up-to-Date:** Your MOCs will reflect the latest structure of your vault.
*   **Effortless Organization:** Focus on writing, not on maintaining indexes.
*   **Enhanced Navigation:** Easily jump between related notes and explore your knowledge graph.
*   **Visual Clarity:** Improve Obsidian's graph view with well-connected MOCs.

---

## How It Works 🛠️

The `generate_mocs.py` script scans your Obsidian vault. For every folder that contains Markdown files (`.md`) or other subfolders, it creates (or updates) a special Markdown file named `_MOC.md` (e.g., `Journal_MOC.md`, `Projects_MOC.md`). This `_MOC.md` file then lists and links to all the Markdown files and subfolders within that directory.

The script is designed to be portable! 🌍 It automatically detects the root of your Obsidian vault based on its own location, so you can move or clone your entire vault without needing to adjust paths manually.

---

## Setup Instructions 🚀

Follow these steps to get your MOC automation up and running!

### Step 1: Ensure Python is Installed ✅

This script requires Python 3. Most modern operating systems (macOS, Linux) come with Python pre-installed.

*   **How to check:** Open your terminal or command prompt and type:
    ```bash
    python3 --version
    # or
    python --version
    ```
    If you see a version number (e.g., `Python 3.x.x`), you're good to go! If not, follow the instructions below for your operating system.

*   **Installing Python (if needed):**
    *   **macOS:** Python is usually pre-installed. If you need a newer version, consider using Homebrew: `brew install python3`
    *   **Linux:** Python is usually pre-installed. If not, use your distribution's package manager (e.g., `sudo apt install python3` on Ubuntu/Debian, `sudo yum install python3` on Fedora/RHEL).
    *   **Windows:** Download the installer from the official Python website: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
        *   **IMPORTANT:** During installation, make sure to check the box that says "Add Python to PATH". This is crucial for running Python commands from any directory.

### Step 2: Place the Script 📂

The `generate_mocs.py` script should be placed within your Obsidian vault. A good place is often a dedicated "scripts" or "automation" folder. For example, you could place it in a structure like:

```
Your_Obsidian_Vault/
├── .obsidian/
├── Journal/
├── Projects/
│   └── MOC_Automation/
│       └── generate_mocs.py  <-- Place it here!
└── Notes/
```

**Note:** You've already copied the script to `/Users/kesaru/Projects/Obsidian-MOC-Automation/generate_mocs.py`. When you integrate this into your Obsidian vault, you'll need to place it in a suitable location within the vault itself.

### Step 3: Test the Script (Manual Run) 🧪

Before automating, let's make sure the script runs correctly.

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you placed `generate_mocs.py`. For example, if you placed it in `Your_Obsidian_Vault/Projects/MOC_Automation/`:
    ```bash
    cd "path/to/Your_Obsidian_Vault/Projects/MOC_Automation"
    ```
3.  Run the script:
    ```bash
    python3 generate_mocs.py
    # (If `python3` doesn't work, try `python` instead)
    ```

After running, check some of your folders in Obsidian. You should see new `_MOC.md` files appearing (e.g., `Journal_MOC.md`, `Projects_MOC.md`, etc.).

### Step 4: Automate Daily MOC Generation ⏰

Now, let's set up the script to run automatically every day.

#### For macOS and Linux (using Cron) 🐧🍎

Cron is a time-based job scheduler in Unix-like operating systems.

1.  **Open your crontab for editing:**
    ```bash
    crontab -e
    ```
    If it's your first time, it might ask you to choose an editor (e.g., `nano`, `vim`). `nano` is generally easier for beginners.

2.  **Add the cron job:**
    Add the following line to the end of the file. This command will run the script every day at 3:00 AM. **Remember to replace `/path/to/your/obsidian/vault/` with the actual path to your Obsidian vault's root directory where the script resides.**

    ```cron
    0 3 * * * /usr/bin/python3 "/path/to/your/obsidian/vault/Projects/MOC_Automation/generate_mocs.py" >> "/path/to/your/obsidian/vault/Projects/MOC_Automation/moc_log.log" 2>&1
    ```
    *   `0 3 * * *`: This means "at 0 minutes past 3 AM, every day of every month, every day of the week."
    *   `/usr/bin/python3`: This is the full path to your Python 3 executable. You can find this by typing `which python3` (or `which python`) in your terminal. Replace this path if yours is different.
    *   `>> "/path/to/your/obsidian/vault/Projects/MOC_Automation/moc_log.log" 2>&1`: This redirects all output (standard output and errors) to a log file named `moc_log.log` within your script's folder. This is useful for troubleshooting.

3.  **Save and Exit:**
    *   If using `nano`: Press `Ctrl + O` (to write out), then `Enter`, then `Ctrl + X` (to exit).
    *   If using `vim`: Press `Esc`, then type `:wq` (write and quit), then `Enter`.

Your cron job is now scheduled! 🎉

#### For Windows (using Task Scheduler) 🪟

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
        *   Example: `"/path/to/your/obsidian/vault/Projects/MOC_Automation/generate_mocs.py"`
    *   **Start in (optional):** Type the directory where your script is located.
        *   Example: `"/path/to/your/obsidian/vault/Projects/MOC_Automation"`

6.  **Finish:**
    *   Click `Next`, then `Finish`.

Your task is now scheduled! You can right-click the task in Task Scheduler and select "Run" to test it immediately.

---

## Troubleshooting 🐛

*   **Script not running:**
    *   **Check paths:** Double-check all file paths in your cron job or Task Scheduler entry. Even a small typo can prevent it from running.
    *   **Permissions:** Ensure the script (`generate_mocs.py`) has execute permissions (on macOS/Linux, run `chmod +x generate_mocs.py` in its directory).
    *   **Python environment:** Make sure the `python3` (or `python`) command in your cron job/Task Scheduler points to the correct Python installation.
    *   **Log file:** Check the `moc_log.log` file (or Task Scheduler's "History" tab) for any error messages.

*   **MOCs not updating/appearing:**
    *   Run the script manually (Step 3) to see if it works.
    *   Ensure the script's `vault_root` variable correctly points to your Obsidian vault's root directory. The current script assumes it's placed within your vault. If your vault structure is different, you might need to adjust the `vault_root` logic in `generate_mocs.py` (though it's designed to be adaptive).

---

## Contribute! 🤝

Got ideas for improvements? Found a bug? We'd love your contributions! Feel free to open an issue or submit a pull request.

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by Your GitHub kesaruhasun
