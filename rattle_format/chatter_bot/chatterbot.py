from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import gourde

from chatter_bot.configuration.chatterbot_config import AppConfig
from chatter_bot.slack_messenger.chatter_messenger import ChatterMessenger
from chatter_bot.app_home.app_home import AppHome


class ChatterBot():

    def __init__(self, registry=None):
        self.gourde = gourde.Gourde(__name__, registry=registry)
        self.tokens = AppConfig.resolve()
        self.app = App(token=self.tokens.bot_token)
        self.Messenger = ChatterMessenger()
        self.Messenger.start(self.app)
        self.Home = AppHome()
        self.Home.start(self.app)

    def run(self):
        SocketModeHandler(self.app, self.tokens.app_token).start()
        self.gourde.run()

# Start the app


def main():
    chatterbot = ChatterBot()
    chatterbot.run()


if __name__ == "__main__":
    main()
