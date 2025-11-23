from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def get_chatbot():
    bot=ChatBot('TerminalBot', database_uri='sqlite:///db.sqlite3')
    trainer=ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')
    return bot
