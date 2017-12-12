import argparse
import random
from lxml import etree
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font


COURSE_XML = 'https://www.coursera.org/sitemap~www~courses.xml'
COURSE_COUNT = 20


def fetch_xml():
    request = requests.get(COURSE_XML).content
    root = etree.fromstring(request)
    list_of_random_courses = random.sample(
        [course[0].text for course in root], COURSE_COUNT)
    return list_of_random_courses


def fetch_html(course_slug):
    course_html = requests.get(url=course_slug)
    course_html.encoding = 'UTF-8'
    course_html = course_html.text
    return BeautifulSoup(course_html, 'lxml')


def get_course_info(soup):
    title = soup.find('h1', class_='title display-3-text')
    if title:
        title = title.text
    else:
        title = None
    language = soup.find('div', class_='rc-Language')
    if language:
        language = language.text
    else:
        language = None
    date_start = soup.find('div', class_='startdate ' +
                           'rc-StartDateString caption-text')
    if date_start:
        date_start = date_start.span.text[-6:]
    else:
        date_start = None
    weeks = len(soup.find_all('div', class_='week-heading body-2-text'))
    rating = soup.find('div', class_='ratings-text bt3-visible-xs')
    if rating:
        rating = rating.text[:3]
    else:
        rating = None
    return {'title': title,
            'language': language,
            'date_start': date_start,
            'weeks': weeks,
            'rating': rating,
            }


def fill_worksheet(worksheet, courses):
    ft = Font(bold=True, size=13)
    worksheet['A1'] = '№'
    worksheet.column_dimensions['A'].width = 10.0
    for course_number, cell in \
            enumerate(worksheet['A2':'A{}'.format(COURSE_COUNT + 1)], 1):
        cell[0].value = course_number
        cell[0].alignment = Alignment(horizontal='center')
    # To change columns order in future just change values of keys
    columns_order = {
        'title': 'B',
        'language': 'C',
        'date_start': 'D',
        'weeks': 'E',
        'rating': 'F',
    }
    horizontal_columns = {'date_start', 'weeks', 'rating'}
    for column_id, column in columns_order.items():
        current_value_list = [course[column_id] if course[column_id] is not
                              None else 'N/A' for course in courses]
        for current_number, current_value in enumerate(current_value_list, 2):
            current_cell = worksheet['{}{}'.format(column, current_number)]
            current_cell.value = current_value
            if column_id in horizontal_columns:
                current_cell.alignment = Alignment(horizontal='center')
    title_column = columns_order['title']
    worksheet['{}1'.format(title_column)] = 'Course Name'
    worksheet.column_dimensions[title_column].width = 90.0
    language_column = columns_order['language']
    worksheet['{}1'.format(language_column)] = 'Course Language'
    worksheet.column_dimensions[language_column].width = 30.0
    date_start_column = columns_order['date_start']
    worksheet['{}1'.format(date_start_column)] = 'Starting'
    worksheet.column_dimensions[date_start_column].width = 25.0
    weeks_column = columns_order['weeks']
    worksheet['{}1'.format(weeks_column)] = 'Course Length (Weeks)'
    worksheet.column_dimensions[weeks_column].width = 30.0
    rating_column = columns_order['rating']
    worksheet['{}1'.format(rating_column)] = 'Rating'
    worksheet.column_dimensions[rating_column].width = 20.0
    for raw_title in worksheet[1]:
        raw_title.alignment = Alignment(horizontal='center')
        raw_title.font = ft
    return worksheet


def save_workbook(workbook, filepath):
    workbook.save(filepath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='coursera.org parser')
    parser.add_argument(
        'path_to_xlsx', help='path to xlsx file with results')
    args = parser.parse_args()
    workbook = Workbook()
    worksheet = workbook.active
    file_output = args.path_to_xlsx
    print('Taking 20 random courses and fetching html for each of them...')
    courses_parsed_info = [get_course_info(fetch_html(course)) for course in
                           fetch_xml()]
    print('Filling xlsx with courses info...')
    filled_xlsx = fill_worksheet(worksheet, courses_parsed_info)
    save_workbook(workbook, file_output)
    print('Done, check {}'.format(file_output))
