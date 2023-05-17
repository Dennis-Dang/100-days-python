# Password Manager App
This is a GUI application that holds and generates passwords. This kind of program is designed to run locally. 

DISCLAIMER: I do not recommend practical use of this app to store passwords as it will save it in plaintext, which is 
absolutely not secure in today's application development standards. This program is only developed as a means of 
exercise for designing GUI apps.

## Run it remotely on my Replit!
https://replit.com/@DennisDang1/Password-Manager-GUI
<br>
Do not use actual personal passwords in this remote replit instance. I am not responsible for any harm done for any information breach.
This is just a link to demo my project. Please don't use personal information.
See disclaimer above.

## Or, build it locally:
```shell
git clone --depth 1 --filter=blob:none --sparse https://github.com/Dennis-Dang/100-days-python
cd "100-days-python"
git sparse-checkout init --cone 
git sparse-checkout set "Password Manager GUI"
```
Install the required packages inside the project directory using git:
```shell
pip install -r requirements.txt
```

Run the main.py script.
```shell
python main.py
```

## How to use:
### Generating a password:
1. Fill out the following fields: Website, Email/Username
2. Click Generate to generate password.
    1. NOTE: A password will be generated and will be copied to the user's clipboard.
3. Click Add to save password details to a password file.

### Looking up a password:
1. Type down the website for the corresponding password in the Website field.
   1. This field is not case-sensitive.
2. Click the Search button.
3. If there is a password entry found, A pop-up will appear with the corresponding password details.
