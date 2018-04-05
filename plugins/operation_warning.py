from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random

@listen_to('rm')
def warning_command(message):
    randomnumber = int(random.choice('123456789'))
    print(randomnumber)
    if randomnumber < 3 :
      message.reply('気をつけてね！')
