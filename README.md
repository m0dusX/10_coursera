# Coursera Dump

This script takes 20 random courses from coursera.org xml feed, gets information about them and writes collected info to xlsx file. 
The following info will be written to xlsx file: 
1) Course name
2) Language
3) Date of course start
4) Length (in weeks)
5) User ranking

# Quickstart

Place coursera.py somewhere. Then run command line, go to folder in which you moved script and execute it.

Example of script launch on Linux, Python 3.5:

```#!bash

$ python coursera.py

```

Output data example (xlsx file):

| Course Name                                                   | Course Language                                   | Starting | Course Length (weeks) | Rating  |
|---------------------------------------------------------------|---------------------------------------------------|----------|-----------------------|---------|
| Mandarin Chinese 3: Chinese for Beginners                     | English                                           | Oct 02   | 5                     | 4.8     |
| Business English: Meetings                                    | English                                           | Sep 25   | 4                     | 4.7     |
| Build Your Professional ePortfolio in English                 | English                                           | Oct 02   | 4                     | 4.6     |
| An Introduction to Interactive Programming in Python (Part 2) | English, Subtitles: Turkish, Chinese (Simplified) | Oct 16   | 4                     | 4.9     |
| Драгоценные камни: диагностика и экспертиза                   | Russian                                           | Oct 02   | 5                     | 4.9     |
| .......                                                       | .......                                           | .......  | .......               | ....... |

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
