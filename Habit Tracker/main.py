import datetime as dt
import api_handler

PIXELA_ENDPOINT = "https://pixe.la"

tracker = api_handler.FitTracker()


commands = '''
Add: Add an entry to the tracker for a day.
Modify: Modify an entry.
Delete: Delete an entry.
Settings: Configure account settings.
'''

print("Welcome to the Habit Tracker, what would you like to do?")
print("What would you like to do? "+commands)
to_do = input("> ").lower()
while 'exit' != to_do:
    if to_do == 'idk':
        print(commands)
    elif to_do == 'add':
        print("Enter the date you want to add the entry for. (YYYY-MM-DD)\n"
              "Or press Enter to submit as today's date.")
        str_date = input("> ")
        str_date = str_date.strip()
        date = None
        if not str_date:
            date = dt.datetime.today()
        else:
            try:
                date = dt.datetime.strptime(str_date, "%Y-%m-%d").date()
                if date > dt.datetime.today().date():
                    print(f"You are making an entry into the future. I cannot do that. "
                          f"Enter a date before {dt.datetime.today().strftime('%Y-%m-%d')}. Returning to menu.")
                    date = None
            except ValueError:
                print("Invalid date. Date must be formatted YYYY-MM-DD")

        if date:
            try:
                print(f"How many sit-ups did you do on {date.strftime('%Y-%m-%d')}?")
                quantity = int(input("> "))
            except ValueError:
                print("Quantity must be a number. Try again.")
            else:
                print(f"You've done {quantity} sit-ups on {date.strftime('%Y-%m-%d')}. Confirm? (Y/N)")
                confirm = input("> ").lower()
                if confirm == 'y':
                    if tracker.ids['GRAPH_ID']:
                        try:
                            tracker.add_pixel(str(quantity), tracker.ids['GRAPH_ID'], date.strftime("%Y%m%d"))
                        except Exception as e:
                            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
                        else:
                            print("Pixel added successfully.")
                    else:
                        print("GRAPH_ID not found. Try creating a graph first.")

    print("\nWhat would you like to do? (enter 'idk' for commands)")
    to_do = input("> ").lower()
