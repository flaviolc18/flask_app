import telepot

class Bot:
  bot = None
  chat_id = None

  def __init__(self):
    self.bot = telepot.Bot("647490139:AAGHiZzb06ZjbYnnmwJrslBRm1B_MrrUhXc")
  
  def get_ready(self, chat_id=None):
    if chat_id:
      self.chat_id = chat_id
      return True
    else:
      resp = self.bot.getUpdates()
      if not resp:
        return False
      else:
        self.chat_id = resp[0]['message']['from']['id']
        return True

  def send_msg(self, msg):
    self.bot.sendMessage(self.chat_id, msg)