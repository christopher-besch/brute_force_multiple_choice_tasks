# brute_force_multiple_choice_tasks
When you have a multiple choice task you sometimes get a solution word like this:

| expression | right | wrong |
|:---------- |:-----:|:-----:|
| 5 - 2 = 3  | L     | A     |
| 5 - 3 = 3  | N     | O     |
| 7 - 2 = 5  | G     | U     |
| 10 - 7 = 3 | I     | S     |
| 5 - 2 = 5  | E     | S     |
| 5 - 2 = 17 | N     | T     |
| 5 - 2 = 3  | I     | U     |
| 5 + 2 = 7  | K     | M     |

here you are supposed to take the character from the "right" row when the expression is logical and from the "wrong" row if not. When you add those characters together you get a word.</br>
this script can brute force this word. You simply have to change chars.txt to match with your task in the first line there are the characters for when it's right and in the second one for when it's not. You can add as many lines as your computer can handle.</br>
You might also want to change the database to match with your language you supect the word to be in.
