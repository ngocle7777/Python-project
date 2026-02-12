Binh Thuan Local Education App (Grade 10)
An interactive educational application designed for 10th-grade students in Binh Thuan Province, Vietnam. This tool helps students explore local history, geography, music, and literature through a vivid, multimedia-rich interface.

🌟 Features
Localized Content: Specifically tailored to the "Local Education" (Giáo dục địa phương) curriculum of Binh Thuan.

Interactive UI: Integrated visuals including local landscapes and themed backgrounds.

Immersive Audio: Features background music (Vlog No Copyright Music) and interactive sound effects for correct/incorrect answers.

Portable: No installation required—runs directly from a single executable file.

🛠 Tech Stack
Language: Python 3.x

GUI Framework: Tkinter / Pygame (Integrated for multimedia handling)

Packaging: PyInstaller (via .spec configuration)

📂 Project Structure
Based on the Hoc_GDDP_Binh_Thuan.spec file, the project utilizes the following resource mapping:

Plaintext
├── Hoc_GDDP_Binh_Thuan.py   # Main source code
├── Hoc_GDDP_Binh_Thuan.spec # PyInstaller configuration
├── Hoc_GDDP_Binh_Thuan.exe  # Compiled Windows executable
└── Assets (Bundled):
    ├── Audio: vebt.mp3, negative.mp3, correct-.mp3, button-click.mp3, etc.
    └── Images: background.jpg, diali_bg.jpg, logo.png, lop10_button_image.png, etc.
🚀 Getting Started
For Users
Go to the Releases page.

Download Hoc_GDDP_Binh_Thuan.exe.

Double-click to run (Windows only).

For Developers
Clone the repository:
https://github.com/ngocle7777/Python-project.git
Install dependencies: (Note: Ensure you have the required libraries like pygame or Pillow installed)

Bash
pip install -r requirements.txt
Run the script:

Bash
python Hoc_GDDP_Binh_Thuan.py
📦 Building from Source
To compile the script into a single executable using the provided spec file:

Bash
pyinstaller Hoc_GDDP_Binh_Thuan.spec
📝 License
This project is developed for educational purposes.

Author: 

Location: Lâm Đồng (Binh Thuan), Vietnam 🇻🇳
