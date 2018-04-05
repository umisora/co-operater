from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random

@listen_to('rm -[a-zA-Z]|shutdown')
def warning_command(message):
    randomnumber = int(random.choice('123456789'))
    print(randomnumber)
    if randomnumber < 8 :
      message.reply('コマンド気をつけてね！')
