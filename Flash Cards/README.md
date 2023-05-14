# Flash Card App
This is a Flash Card study app where users can use to study 100 commonly used Vietnamese words. 

If you are not familiar with flash cards, these are generally used as a learning tool widely used in educational settings.
Flash cards consist of a set of cards, with a prompt on one side and the corresponding information on the other side. 
These are frequently used to test your knowledge and how you memorize information.

## How to use:
- You are given a set of cards and will cycle in random order.
- A Vietnamese word or phrase will appear on the screen for 3 seconds.
  - Within these 3 seconds, you are supposed to guess what the translation is.
- After 3 seconds, the card will flip over to show the English translation.
  - If your guess was correct, click the green checkmark to remove the word from the list.
  - If your guess was wrong, click the cross to continue with the next word.
- Your progress is saved to a file called `words_to_learn.csv`.
  - It contains a list of words that you have yet to memorize.
- Upon starting this program up again, the app will automatically read and import your progress from this file.