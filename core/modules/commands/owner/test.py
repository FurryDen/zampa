import core.decorators

@core.decorators.owner.init
def init(update,context):
    bot = context.bot
    bot.send_message(update.messate.chat_id, text="OWNER COMMAND")