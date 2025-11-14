![CI](https://github.com/jermainewakeup/granpost/actions/workflows/ci.yml/badge.svg)

# 🚀 Granpost
##### 🏎️ *Social Media Content Engine using OpenAI API*
Granpost is a small content engine that turns page profiles (CSV) into structured, on-brand post drafts.
It standardizes how you describe each page (theme, audience, guardrails), validates that data, and then uses the OpenAI API to generate draft posts plus machine-readable JSON you can plug into automations like n8n or schedulers.
## ✅ Requirements
- [OpenAI API Key](https://platform.openai.com/api-keys)
- Python 3.11+ (tested on 3.13)
- An internet connection

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
### Configuration
After obtaining your API key, create a `.env` file at the root of the repo.
```zsh
# ./granpost/.env/
OPENAI_API_KEY="paste-key-here"
```

## 💻 Usage
### Importing CSV Files
Place your page profile CSV into the input folder (relative to the repo root):
```zsh
mv example.csv data/input/
```
You can use `data/input/sample_profile.csv` as a template for the required columns.

### Generating Content
Run `main.py`

## 🧩 Features
- ✍️ **Caption drafts**: multiple variants with on-brand phrasing.
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

