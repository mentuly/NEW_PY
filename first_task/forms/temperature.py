from aiogram.fsm.state import State, StatesGroup

class temperature(StatesGroup):
    temperature = State()  # це стан в якому бот чекає поки користувач введе щось і далі буде використовувати для того щоб продовжити завдання, якщо прям по простому казати то цей клас прописаний для того щоб показати свої знання і для того щоб облегчити трішки роботу