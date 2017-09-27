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

| Course Name                                                                | Course Language                                           | Starting | Course Length (weeks) | Rating |
|----------------------------------------------------------------------------|-----------------------------------------------------------|----------|-----------------------|--------|
| Mandarin Chinese 3: Chinese for Beginners                                  | English                                                   | Oct 02   | 5                     | 4.8    |
| Business English: Meetings                                                 | English                                                   | Sep 25   | 4                     | 4.7    |
| Build Your Professional ePortfolio in English                              | English                                                   | Oct 02   | 4                     | 4.6    |
| An Introduction to Interactive Programming in Python (Part 2)              | English, Subtitles: Turkish, Chinese (Simplified)         | Oct 16   | 4                     | 4.9    |
| Драгоценные камни: диагностика и экспертиза                                | Russian                                                   | Oct 02   | 5                     | 4.9    |
| International Marketing Entry and Execution                                | English, Subtitles: Korean, Spanish, Chinese (Simplified) | Oct 02   | 4                     | 4.6    |
| Жизнь в почве                                                              | Russian                                                   | Oct 02   | 5                     | 4.4    |
| Ebola : Vaincre ensemble !                                                 | French, Subtitles: English                                | Oct 02   | 6                     | 4.4    |
| Business English: Basics                                                   | English                                                   | Sep 25   | 6                     | 4.4    |
| Bienestar, equidad y derechos humanos                                      | Spanish                                                   | Oct 09   | 3                     | 4.7    |
| Understanding Obesity                                                      | English                                                   | Dec 11   | 4                     | 4.4    |
| Chinese Politics Part 2 – China and the World                              | English                                                   | Sep 25   | 6                     | 4.8    |
| Write Professional Emails in English                                       | English, Subtitles: French, Japanese                      | Sep 25   | 5                     | 4.6    |
| ?????? Discrete Mathematics Generality                                     | Chinese (Simplified), Subtitles: English                  | Sep 25   | 13                    | 4.8    |
| Private Equity and Venture Capital                                         | English                                                   | Oct 16   | 5                     | 4.7    |
| Strategic Leadership and Management Capstone                               | English                                                   | Nov 06   | 6                     | 4.5    |
| Visual Analytics with Tableau                                              | English                                                   | Oct 02   | 4                     | 4.4    |
| Advanced Search Engine Optimization Strategies                             | English                                                   | Sep 25   | 4                     | 4.5    |
| Desarrollo de Videojuegos 3D en Unity: Una Introducci?n                    | Spanish                                                   | Oct 02   | 5                     | 4.4    |
| Crafting Strategies for Innovation Initiatives for Corporate Entrepreneurs | English                                                   | Sep 25   | 4                     | None   |

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
