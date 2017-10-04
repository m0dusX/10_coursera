# Coursera Dump

This script takes 20 random courses from coursera.org xml feed, gets information about them and writes collected info to xlsx file. 
The following info will be written to xlsx file: 
1) Course name
2) Language
3) Date of course start
4) Length (in weeks)
5) User ranking

# Quickstart

Place coursera.py somewhere. Then run command line, go to folder in which you moved script and execute it with one parameter containing path to xlsx file.

Script usage on Linux, Python 3.5:

```#!bash

$ python coursera.py [-h] <path_to_xlsx>

```

Output data example (xlsx file):

| №   | Course Name                                                       | Course Language                                  | Starting | Course Length (weeks) | Rating |
|-----|-------------------------------------------------------------------|--------------------------------------------------|----------|-----------------------|--------|
| 1   | Single Variable Calculus                                          | English                                          | Oct 09   | 5                     | N/A    |
| 2   | Drug Discovery                                                    | English                                          | Oct 16   | 3                     | 4.6    |
| 3   | Redacci?n de documentos empresariales de gran impacto             | Spanish, Subtitles: Vietnamese, English, Russian | Oct 09   | 4                     | 4.4    |
| 4   | Social Marketing Capstone Project                                 | English                                          | Oct 09   | 5                     | 4.9    |
| 5   | Planning for Climate Change in African Cities                     | English                                          | Oct 23   | 5                     | N/A    |
| 6   | Geospatial Analysis Project                                       | English                                          | Dec 18   | 8                     | 4.9    |
| 7   | Kinematics: Describing the Motions of Spacecraft                  | English                                          | Oct 16   | 4                     | 5.0    |
| 8   | The Music of the Rolling Stones, 1962-1974                        | English                                          | Oct 09   | 7                     | 4.7    |
| 9   | First Steps in Making the Business Case for Sustainability        | English                                          | Oct 02   | 5                     | N/A    |
| 10  | Economie du sol et de l'immobilier I                              | French                                           | Oct 02   | 6                     | 4.8    |
| 11  | Mandarin Chinese 3: Chinese for Beginners                         | English                                          | Oct 02   | 5                     | 4.8    |
| 12  | Читаем русскую классику вместе.  М. Булгаков «Мастер и Маргарита» | Russian                                          | Oct 09   | 6                     | 4.3    |
| ... | ...                                                               | ...                                              | ...      | ...                   | ...    |
| 20  | Global Health at the Human-Animal-Ecosystem Interface             | English, Subtitles: French, Chinese (Simplified) | Oct 02   | 6                     | 4.8    |

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
