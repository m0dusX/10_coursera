from lxml import etree
import requests
import random
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
import sys

def get_courses_list():
    course_count = 20
    r = requests.get('https://www.coursera.org/sitemap~www~courses.xml')
    root = etree.fromstring(r.content)
    list_of_random_courses = random.sample([course[0].text for course in 
        root], course_count)
    return list_of_random_courses

def get_course_info(course_slug):
    course_html  = requests.get(url=course_slug)
    course_html.encoding = 'UTF-8'  #support russian language
    course_html = course_html.text
    soup = BeautifulSoup(course_html, 'lxml')
    title = soup.find('h1', class_='title display-3-text')
    if title:
        title = title.text
    else:
        title = 'Untitled'
    language = soup.find('div', class_='rc-Language')
    if language:
        language = language.text
    else:
        language = 'Undefined'
    date_start = soup.find('div', 
        class_='startdate rc-StartDateString caption-text')
    if date_start:
        date_start = date_start.span.text[-6:]
    else:
        date_start = 'Undefined'
    weeks = len(soup.find_all('div', class_='week-heading body-2-text'))
    rating = soup.find('div', class_='ratings-text bt3-visible-xs')
    if rating:
        rating = rating.text[:3]
    else:
        rating = 'None'
    return [title, language, date_start, weeks, rating]

def output_courses_info_to_xlsx(filepath, course_list):
    wb = Workbook()
    ws = wb.active
    ft = Font(bold=True, size=13)
    ws['A1'] = 'Course Name'
    ws.column_dimensions['A'].width = 90.0
    ws['B1'] = 'Course Language'
    ws.column_dimensions['B'].width = 30.0
    ws['C1'] = 'Starting'
    ws.column_dimensions['C'].width = 25.0
    ws['D1'] = 'Course Length (weeks)'
    ws.column_dimensions['D'].width = 30.0
    ws['E1'] = 'Rating'
    for column_title in ws[1]:
        column_title.alignment = Alignment(horizontal='center')
        column_title.font = ft
    for course_idx, course in enumerate(course_list, 2):
        parsed_info = get_course_info(course)
        for cell_idx, cell in enumerate(ws[course_idx]):
            cell.value = parsed_info[cell_idx]
            if cell_idx != 0 and cell_idx != 1:
                cell.alignment = Alignment(horizontal='center')
    wb.save(filepath)

if __name__ == '__main__':
    filepath = input('Please write path to xlsx file: ')
    output_courses_info_to_xlsx(filepath, get_courses_list())
    print('Done, check {}'.format(filepath))
    sys.exit()
