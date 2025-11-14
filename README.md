![CI](https://github.com/jermainewakeup/granpost/actions/workflows/ci.yml/badge.svg)

# 🚀 Granpost
 ##### 🏎️ *Social Media Content Engine using OpenAI API*

## 📦 Installation
### Unix/macOS
Clone repo and install dependencies:
```zsh
git clone https://github.com/jermainewakeup/granpost.git
cd granpost

python3 -m venv .venv
source .venv/bin/activate

pip install -U pip
pip install -e . #base dependencies
```
##### 🧷 Optional: Install pre-commit tools (lint, format, test)
```zsh
pip install -e ".[dev]"
```
## 💻 Usage
### Importing CSV Files
```zsh
mv example.csv /data/input/
```

### Generating Content
Run `main.py`

## 🧩 Features
- ✍️ **Caption drafts**: multiple variants with on-brand phrasing.
- 🖼️ **Image ideas**: optional concept/prompt + alt-text suggestions.
- 📦 **Local outputs**: JSON/CSV files + Markdown preview.

## 🛠️ Built With
* Python 3.13
* OpenAI API
* Pydantic

## 📜 License
MIT License
See `LICENSE` file for details

## 🌟 Credits
* My loved ones.

