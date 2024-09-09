from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import ScrollingGroup, Button
from aiogram_dialog.widgets.text import Const, Format

from dialogs.states import MySG, Prices
from .getters import get_prices

start_window = Window(
    Format('Приветствую! Вот список команд:\n/get_prices\n/get_demand\n/optimize_demand'),
    state=MySG.start_command,
)
start_dialog = Dialog(start_window)

get_prices_window = Window(
    ScrollingGroup(
        *get_prices(),
        id="prices",
        width=1,
        height=15,
), Const('Список цен:'), state=Prices.get_prices)

get_prices_dialog = Dialog(get_prices_window)


