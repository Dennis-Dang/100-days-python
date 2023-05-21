import datetime as dt
import pyinputplus as pyip
import api_handler

PIXELA_ENDPOINT = "https://pixe.la"

tracker = api_handler.FitTracker()


commands = '''
Commands: 
Add: Add an entry to the tracker for a day.
Modify: Modify an entry.
Delete: Delete an entry.
Settings: Configure account settings.
'''


def get_date() -> str or None:
    print("Enter the date interest for the pixel. (YYYY-MM-DD)\n"
          "Or press Enter to submit as today's date.")
    str_date = pyip.inputDatetime('Enter Date ', formats=('%Y-%m-%d',),
                                  blank=True)
    if not str_date:
        date = dt.datetime.today()
    else:
        date = str_date.date()
        if date > dt.datetime.today().date():
            print(f"You are making an entry into the future. I cannot do that. "
                  f"Enter a date before or on {dt.datetime.today().strftime('%Y-%m-%d')}. Returning to menu.")
            return None

    return date.strftime('%Y%m%d')


print("Welcome to the Habit Tracker.")
to_do = pyip.inputMenu(['add/modify', 'delete', 'settings', 'idk'], "What would you like to do?\n", numbered=True)
while 'exit' != to_do:
    if to_do == 'idk':
        print(commands)
    elif to_do == 'add/modify':
        pixel_date = get_date()

        if pixel_date:
            quantity = pyip.inputNum(f"How many sit-ups did you do on {pixel_date}? ")
            confirm = pyip.inputYesNo(f"You've done {quantity} sit-ups on {pixel_date}. Confirm? (Y/N) ")
            if confirm == 'yes':
                if tracker.ids['GRAPH_ID']:
                    try:
                        tracker.add_pixel(str(quantity), pixel_date)
                    except Exception as e:
                        print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
                    else:
                        print("Pixel added successfully.")
                else:
                    print("GRAPH_ID not found. Try creating a graph first.")
    elif to_do == 'delete':
        pixel_date = get_date()
        tracker.delete_pixel(pixel_date)
    to_do = pyip.inputMenu(['add/modify', 'delete', 'settings', 'idk'], "What would you like to do?\n",
                           numbered=True)
