# Jupyter-Notebook-Project-Using-Python-basics-functions
Jupyter Notebook Using Python basics functions

Project Description

1.Assign the string 'Hello, Jupyter!' to a variable named welcome_message.

2.Assign the boolean True to a variable named first_cell.

3.Run the code you wrote above. A new code cell should be inserted below the cell you ran. In this new cell:

4.Assign the result of 1200 / 5 to a variable named result.

5.Assign the boolean True to a variable named second_cell.

6.In the first cell, print the content of the variable welcome_message only if first_cell stores the boolean True.
In the second cell, print the content of the variable result only if second_cell stores the boolean True.
Run both cells at once by clicking Run all, which you can find in the Cell menu.

7.In the first code cell, add print('First cell'). Run all the code using the keyboard shortcut corresponding to the run cell, select below action.

8.In the second code cell, add print('Third cell'). Run all the code using the keyboard shortcut corresponding to the run selected cell action. Make sure that no new code cell is created below.

9.Using only the keyboard, use the action run cell, insert below to insert a new cell between the current two cells. To do that:

10.Run the first code cell using the keyboard shortcut corresponding to the run cell, insert below action.
Once the new code cell is created, type print('Second cell') inside. Run the code, and make sure no new code cell is inserted below.

11.Enter command mode by clicking the Jupyter interface somewhere outside the code cells, menu bar, and toolbar.
Select the second code cell using the Up and Down keys. This should be the cell containing only the code print('Second cell').
Delete this second code cell by pressing D twice: D, D.
Select the second code cell (which before deletion was the third code cell) using the keyboard and enter edit mode by pressing Enter.
Once in edit mode, use only your keyboard to change the code print('Third cell') to print('Second cell'). You can move the cursor using Up, Down, Left, and Right.
Run the code in this second cell without creating any new cell below.
Enter command mode, select the second cell. Create a new cell below it by pressing B.
Enter edit mode in this new third cell, type the code print('A true third cell'). Run the code cell while simultaneously creating a new cell below it.

12. Delete all the cells you created so far by pressing D, D.

In the first code cell:

Write a function named welcome() that takes as input a parameter named a_string and prints the concatenated string 'Welcome to ' + a_string + '!'. The function doesn't return anything, it just prints the string.
Assign the string 'Dataquest' to a variable named dq.
Assign the string 'Jupyter Notebook' to a variable named jn.
Assign the string 'Python' to a variable named py.
Run the code in this first cell. Insert a new cell below.

In this newly created code cell, use the welcome() function on the variables dq, jn, and py.

13.Run the %history -p command to get an understanding of the current state of your program.

The output of %history -p should be pretty verbose since we ran quite a lot of code so far — you should also see that it's not very easy to understand the state of the program at this point.
Restart the state of your program and clear the output of every cell by clicking the Restart & Clear Output action from the Kernel menu.

In a separate cell, run the %history -p command again to confirm that no code has been run (except for %history -p).

Run the code we wrote in the previous exercise again.

Modify the first cell (the one where you defined only the function welcome() and the variables dq, jn, and py):

The function should not print the string 'Welcome to ' + a_string + '!' anymore. Instead, the string 'Welcome to ' + a_string + '!' is saved to a variable and the variable is returned (using a return statement).
Delete the line of code where you assigned the string 'Python' to the py variable.
Run the modified code, and then try to think about the state of the program just by using the code and the output you see.

You should notice that the state you deduced is contradictory to the output printed in the second cell — for instance, welcome(dq) is not supposed to print anything (because we didn't use print() this time), and welcome(py) should raise an error because py is not defined anymore.
Pretend you don't know what happened exactly and run the %history -p command again to find out.

Fix the issue either by running the second code cell again or by clicking Restart & Run All in the Kernel menu.

14. A code cell, open the AppleStore.csv data set. Read it in as a list of lists, and display the first few rows.

Create a Markdown cell above the code cell you used to open the data set and explain the steps you took to open the data set.

Below the code cell, add another Markdown cell, where you give some information about the data set you just opened. Assume you're writing for someone who doesn't know anything about the data set. Mention:

What the data set is about
The source of the data set
Where the data set can be downloaded from and where the documentation can be found.
