import config

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
from loguru import logger
from googlesheet_table import GoogleTable


logger.add(
    config.settings['LOG_FILE'],
    format='{time} {level} {message}',
    level='DEBUG',
    rotation='1 week',
    compression='zip',
)


class BirthDateTelegramBot(Bot):
    def __init__(self, token, parse_mode, google_table=None):
        super().__init__(token, parse_mode=parse_mode)
        self._google_table: GoogleTable = google_table

bot = BirthDateTelegramBot(
    token=config.settings['TOKEN'],
    parse_mode=types.ParseMode.HTML,
    google_table=GoogleTable('creds.json', config.settings['GOOGLESHEET_URL']),
)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(filters.Regexp(regexp=r"(((Д|д)р))"))
async def bot_commands_handler(message_from: types.Message) -> None:
  names = bot._google_table.search_names(1)
  if names == -1:
    return
  name_str = '\n- '.join(list(names.values())[0])
  answer: str = (
    f'{list(names.keys())[0]} будет ДР у этих ребят:\n- {name_str}'
  )
  try:
      await message_from.reply(answer)
  except Exception as send_error:
      logger.debug(f"{send_error.message}: Empty data")
      return

    
if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
