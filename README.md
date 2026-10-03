# ⚙️ Python Settings Manager

A lightweight Python script designed to manage and manipulate user configurations/settings using dictionaries. It provides clean CRUD (Create, Read, Update, Delete) operations with case-insensitive handling and formatted output displays.

---

## 🚀 Features

*   **Add Settings:** Safely adds new configuration parameters while checking for existing keys to prevent duplicates.
*   **Update Settings:** Modifies existing preference values with automated validation checks.
*   **Delete Settings:** Removes unwanted configuration keys safely.
*   **View Settings:** Formats and prints current user settings cleanly with capitalized keys.
*   **Case Insensitive:** Automatically standardizes configuration keys and values to lowercase for consistency.

---

## 📂 Project Structure

```text
├── settings.py       # Contains settings management functions and sample test dictionary
└── README.md         # Project documentation

from settings import add_setting, update_setting, view_settings, test_settings

# View current settings
print(view_settings(test_settings))

# Add a new setting
print(add_setting(test_settings, ['language', 'english']))

# Update an existing setting
print(update_setting(test_settings, ['theme', 'light']))
