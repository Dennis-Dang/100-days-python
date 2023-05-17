# Rain Alert Project
This app sends a telegram text notification to my phone to alert me if there's going to be any rain today.

Upon launching this program, it will receive all weather conditions within the next 12 hours according to the client's
`Latitude` and `Longitude` coordinates using the Open Weather Map API.

Then, if any of the weather conditions are Snow, Rain, Drizzle, or Thunderstorm (defined by `weather code` ids), the app will send a telegram message
notification via a Telegram Bot.

## How to Install:
#### Download Project
```shell
git clone --depth 1 --filter=blob:none --sparse https://github.com/Dennis-Dang/100-days-python
cd "100-days-python"
git sparse-checkout init --cone 
git sparse-checkout set "Rain Alert"
```
#### Set up the environment variables in a `.env` file.
The program uses the following environment variables, I've also listed how to configure them:
- OWM_API_KEY 
  - Create a free account and retrieve your API Key on 
  <a href="https://home.openweathermap.org/users/sign_up">Open Weather Map.</a> 
- LATITUDE
  - A floating point number, find your latitude at https://www.latlong.net/
- LONGITUDE
  - A floating point number, find your latitude at https://www.latlong.net/
- TELEGRAM_API_KEY 
  - Create a Telegram account. Message @BotFather `/newbot`.
  - Enter a Display Name to call your new bot.
  - Enter a unique username for your new bot.
  - @BotFather will then finally give you this API key to use.
- TELEGRAM_CHAT_ID 
  - Have your TELEGRAM_API_KEY ready. Go to the following Telegram url to find the Chat ID.
    - `https://api.telegram.org/bot{TELEGRAM_API_KEY}/getUpdates`
    - For example, if your API key is `12345:ALSKKLJCAD4139213z`:
      - `https://api.telegram.org/bot12345:ALSKKLJCAD4139213z/getUpdates`


#### Set up a way to run the program every day in the morning.
<p>There are multiple ways to do this. If you have a Mac or Linux system, you can use a crontab to schedule `main.py` to run every day at a certain time. Otherwise if you have a Windows machine, you can use the Task Scheduler program to configure python to run the main.py script.</p>

The above method will only be practical if you leave your system on 24/7. I would recommend you to host this on the cloud service instead.
There are many cloud services out there nowadays that offer affordable costs to run such tasks.

##### Here's how to do it with <a href=https://www.pythonanywhere.com/>Python Everywhere</a>
1. Sign up to a limited account (One app per user, more details <a href=here>here</a>)
2. Navigate to Files, then upload the project files (don't forget the `.env` file too)
3. Navigate to Tasks, enter the time (UTC) you wish to run it every day.
   1. Then, enter the your run execution command: `python3 main.py`