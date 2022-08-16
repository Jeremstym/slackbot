# ----*utf-8*-------
# Set configuations for the chatter bot app

import os
import rattle_configuration


class AppConfig:

    def __init__(self, config: rattle_configuration.RattleConfig):
        self.bot_token = config.get("slack.bot_token")
        self.app_token = config.get("slack.app_token")

    @classmethod
    def resolve(cls):
        return cls(rattle_configuration.RattleConfig.resolve())
