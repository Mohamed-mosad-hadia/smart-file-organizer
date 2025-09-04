


# 🗂️ Smart File Organizer

A Python script that automatically organizes files in a directory into categorized folders based on file type. It runs every 10 minutes, prevents overwriting by renaming duplicates, and logs all actions.

---

## 🚀 Features

- 📁 Sorts files into categories: Code, Images, PDFs, Excel, Database, and Others.
- 🔁 Runs automatically every 10 minutes.
- 🧠 Avoids overwriting by renaming files if duplicates exist.
- 📜 Logs every move in `organizer_log.txt`.
- 🛑 Skips temporary, hidden, or incomplete files.

---

## 📂 Categories

| Folder Name | File Types |
|-------------|------------|
| Code        | `.py`, `.js`, `.css`, `.html`, `.json`, `.md`, `.pyc` |
| Excel       | `.xlsx`, `.csv`, `.xml` |
| PDFs        | `.pdf`, `.txt` |
| Images      | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Database    | `.sql`, `.db` |
| Other       | All other files |

---

## 🛠️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/smart-file-organizer.git
   cd smart-file-organizer








# 📌 Notes
-The script avoids moving itself.
Temporary files (e.g. .crdownload, .tmp, hidden files) are skipped.

-Designed for desktop environments (Windows, macOS, Linux).

-📝 All actions are logged to organizer_log.txt.



# 💡 Ideas for future improvements

  - GUI with drag & drop support
  
  - Watch any folder (not just current one)
  
  - Notification system (desktop or email)

👨‍💻 Author
Developed by Mohamed Mosaad 









