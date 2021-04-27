### Case Study Leaderboard
_The program is written in Python and run with python 3.7.6_

##### How to run the program
Run `git clone https://github.com/siwatjames/case-study-leaderboard.git` to clone this repositoy, then run `python leaderboard.py {user_id} [{number_of_users_to_print}]` to run the program.

- Example 1: `python leaderboard.py zWK5IYwCegT1TvDi0EGfrjRnFKu2` will return a list of 10 users including the user id zWK5IYwCegT1TvDi0EGfrjRnFKu2

- Example 2: `python leaderboard.py zWK5IYwCegT1TvDi0EGfrjRnFKu2 5` will return a list of 5 users including the user id zWK5IYwCegT1TvDi0EGfrjRnFKu2

##### Arguments:
- `user_id` string : User id
- `number_of_users_to_print` int: _optional _ the number of users to print. Default 10.

##### Notes:
There are users with the same number of bananas. The ranking system impletemented is similar to MySql RANK function referenced [here](https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-rank-function/).