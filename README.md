# Python File & JSON Handler (IS Project)

## Description
A Python project developed for an Information Systems (IS) course.  
The program uses built-in modules (os and json) to manage files/directories and handle JSON data without requiring external dependencies.

The script demonstrates structured data handling, basic automation, and file system processing.

---

##  Technologies Used
- Python 3.x
- os (built-in)
- json (built-in)

---

##  Project Structure
| File | Description |
|------|-------------|
| main.py | Main script (rename to match your file) |
| data.json | Example JSON data (optional) |
| README.md | Project information & usage instructions |

> Rename main.py to your actual filename if different.

---

##  Features
✔ Reads JSON data from files  
✔ Writes serialized JSON data  
✔ Interacts with file system using os  
✔ No external libraries required  
✔ Suitable for academic demonstration  

---

##  How to Run
1. Install Python 3.x (if not installed)
2. Open terminal in the project folder
3. Run:

``bash
python main.py
Replace main.py with your actual file name.

Example Usage (Conceptual)
python
Copy code
import os
import json

# Listing files in directory
print(os.listdir())

# Reading JSON file
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)
 Notes
No external packages are required

Works on Windows, Linux, and macOS

Designed for educational use in IS course work
