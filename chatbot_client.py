from django.core.management.base import BaseCommand
from terminal_chat.bot import get_chatbot

class Command(BaseCommand):
    help="Start terminal bot"

    def handle(self,*args,**opts):
        bot=get_chatbot()
        print("Bot ready. Type 'exit' to quit.")
        while True:
            msg=input("you: ")
            if msg.lower()=="exit":
                print("bot: Goodbye")
                break
            print("bot:", bot.get_response(msg))
