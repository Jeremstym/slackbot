#------*utf-8*------------------
# App Home to welcome people

class AppHome():
    
    def start(self, app):
    
        @app.event("app_home_opened")
        def update_home_tab(client, event, logger):
            # Call views.publish with the built-in client
            client.views_publish(
                # Use the user ID associated with the event
                user_id=event["user"],
                # Home tabs must be enabled in your app configuration
                view={
                    "type": "home",
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "*Welcome, <@" + event["user"] + "> :elephant:*"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                              "type": "mrkdwn",
                              "text": "Here is a list a command you can use with the bot. \n *help* to know what to do \n *start* to pick a topic \n Or just come to say *hello*"
                            }
                        }
                    ]
                }
            )