import os
import csv

from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const


def get_prices():
    prices = list()
    os.open('/Users/kabynks/desktop/bot/model/start.py', os.O_RDONLY)
    with open('/Users/kabynks/desktop/bot/model/result.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            prices.append(Button(Const(row['predict']), id="price"))
    return prices