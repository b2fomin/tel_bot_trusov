from aiogram import Dispatcher, types
from aiogram.filters.command import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils import get_currency_rate

storage = MemoryStorage()
dp=Dispatcher(storage=storage)

class Form(StatesGroup):
    answer = State()

@dp.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer('Добрый день! Как вас зовут?')
    await state.set_state(Form.answer)

@dp.message(Form.answer)
async def answer(message: types.Message, state: FSMContext):
    name = message.text
    await state.clear()
    currency = get_currency_rate()
    await message.answer(f'Рад знакомству, {name}. Курс доллара сегодня: {currency}')