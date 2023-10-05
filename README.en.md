# Bowling Game Kata using TDD (Test Driven Development) on Python

[![Fr](https://img.shields.io/badge/lang-fr-fr)](https://github.com/meriemsmt/BowlingGameKata-TDD/blob/main/README.md)
[![En](https://img.shields.io/badge/lang-en-en?color=red)](https://github.com/meriemsmt/BowlingGameKata-TDD/blob/main/README.en.md)

TDD (Test Driven Development) is a good practice for writing test code before production code.
This includes repeating a cycle of writing test code that fails, developing production code that passes the test, and refactoring on both sides.

By using Git&GitHub to monitor code changes during commits, this tutorial shows, step by step, a Python version of the bowling game kata.

## Problem
Here is an example of a bowler's scoreboard:

| Frame | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Rolls | 1 &nbsp;&nbsp; 4 | 4 &nbsp;&nbsp; 5 | 6 &nbsp;&nbsp; / | 5 &nbsp;&nbsp; / | ✕ | 0 &nbsp;&nbsp; 1 | 7 &nbsp;&nbsp; / | 6 &nbsp;&nbsp; / | ✕ | 2 &nbsp;&nbsp; / &nbsp;&nbsp; 6 |
|Score| 5 | 14 | 29 | 49 | 60 | 61 | 77 | 97 | 117 | **133** |

The rules of the game are:
>The game consists of 10 frames as shown above. In each frame, the player has two chances to knock down 10 pins. The frame score is the total number of pins knocked down, plus bonuses from Strikes and Spares.
>
>A Spare is when the player knocks down all 10 pins in two tries. The bonus for this frame is the number of pins knocked down on the next roll. For example, for frame 3 above, the score is 10 (the total number of pins knocked down) plus a bonus of 5 (the number of pins knocked down on the next roll.)
>
>A strike is when the player knocks down all 10 pins on his first try. The bonus for this box is the value of the next two balls thrown.
>
>For the tenth frame, a player who rolls a spare or a strike is allowed to roll an additional ball to complete the square. However, no more than three balls may be thrown into the tenth frame.

The challenge is to develop a class to calculate the final score obtained in a bowling game using TDD which leads to extensive testing and clean code. The resulting *Game* class should have two methods:

- *Roll:* Used to return the number of pins that fell on each roll.
- *Score:* Used at the end of the game to obtain the final score.

​## Solution
Here is the cycle of a TDD:
![alt text](https://github.com/meriemsmt/BowlingGameKata-TDD/blob/main/TDDWorkflow.png)

1. [![Generic badge](https://img.shields.io/badge/⎍-Test-red.svg)](https://shields.io/)
     Write a test that involves some of the program's logic. This should start with the simplest logic and move on to slightly more complicated logics in later rounds. Since there is no production code for the feature at this time, it should **fail**.
2. [![Generic badge](https://img.shields.io/badge/⎍-Code-brightgreen.svg)](https://shields.io/)
     To write the minimum amount of production code just to **pass** the failing unit test, but no further.
3. [![Generic badge](https://img.shields.io/badge/⎍-Refactor-blue.svg)](https://shields.io/)
     Cleaning both test code and production code into clean codes.

The solution is found on the two files *test_bowling.py* and *bowling.py*, where the first contains the test code and the second the production code. To see the development, please go to the **commits** section, from commit "1st Test - Scoring Zeros" to "Final Refactoring".
