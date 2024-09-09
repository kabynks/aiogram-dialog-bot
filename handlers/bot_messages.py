from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager
from dialogs.states import Prices, MySG

router = Router()

@router.message(Command('get_prices'))
async def echo(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(Prices.get_prices)

@router.message(Command('start'))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.start_command)