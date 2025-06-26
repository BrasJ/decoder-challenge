import requests
from bs4 import BeautifulSoup
import re

def fetch_grid(url):

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraph = soup.find_all(['p', 'div', 'span'])
    lines = [p.get_text().strip() for p in paragraph if p.get_text().strip()]
    return lines

def extract_grid(lines):
    grid_data = []
    for line in lines:
        matches = re.findall(r'(\d{1,2})(.)(\d{1})', line)
        for x, char, y in matches:
            grid_data.append((int(x), char, int(y)))
    return grid_data

def build_grid(grid_data):
    grid = {}
    max_x = max_y = 0

    for x, char, y in grid_data:
        grid[(x, y)] = char
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    result = []

    for y in reversed(range(max_y + 1)):
        row = ''.join(grid.get((x, y), ' ') for x in range(max_x + 1))
        result.append(row)
    return '\n'.join(result)

def print_from_doc(url):
    lines = fetch_grid(url)
    grid_data = extract_grid(lines)
    print(build_grid(grid_data))

if __name__ == '__main__':
    url= "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub"
    print_from_doc(url)