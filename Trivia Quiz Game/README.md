# Trivia Quiz Game
This is a trivia game that generates 10 random computer science questions from an API. These are True/False type of questions. The user can click the Red cross to answer False, or click the Green checkmark to answer True.
User will gain a score point for each correct answer. 

## Run it remotely on my Replit!
https://replit.com/@DennisDang1/Trivia-Quiz-Project

## Or, build it locally:
```shell
git clone --depth 1 --filter=blob:none --sparse https://github.com/Dennis-Dang/100-days-python
cd "100-days-python"
git sparse-checkout init --cone 
git sparse-checkout set "Trivia Quiz Game"
```

Install the required packages inside the project directory using git:
```shell
pip install -r requirements.txt
```

Run the main.py script.
```shell
python main.py
```