from aiogram.fsm.state import StatesGroup, State


class MySG(StatesGroup):
    start_command = State()

class Prices(StatesGroup):
    get_prices = State()