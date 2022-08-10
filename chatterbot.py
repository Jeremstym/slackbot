from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from configuration.chatterbot_config import AppConfig
from slack_messenger.chatter_messenger import ChatterMessenger
from app_home.app_home import AppHome


class ChatterBot():

    def __init__(self):
        self.tokens = AppConfig.resolve()
        self.app = App(token=self.tokens.bot_token)
        self.Messenger = ChatterMessenger()
        self.Messenger.start(self.app)
        self.Home = AppHome()
        self.Home.start(self.app)

    def run(self):
        SocketModeHandler(self.app, self.tokens.app_token).start()

# Start the app

def main():
    chatterbot = ChatterBot()
    chatterbot.run()


if __name__ == "__main__":
    main()
