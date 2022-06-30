import re
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
# Listens to incoming messages that contain "hello"
@app.message(re.compile("(hello|Hello)"))
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )
    
@app.message(re.compile("start"))
def message_start(message, say):
    blocks = [
            {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hi! :smile: Welcome to the *Chatter bot*, what is your question about?"}
			},
            {
			"type": "divider"
            },
                
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Company fields (Account)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-action1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Platform changes (IO level)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-action2"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Contacts"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-action3"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Opportunity"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-action4"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Insertion Order (IO)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-action5"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Contractual Account"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-action6"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Agency addition (IO level)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-action7"
                }
            }
            
            ]
    say(
        blocks=blocks,
        text="Let's start asking questions"
        )
        

@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")
    
    
# Sends a section block with datepicker when someone reacts with a 📅 emoji
@app.event("reaction_added")
def show_datepicker(event, say):
    reaction = event["reaction"]
    if reaction == "calendar":
        blocks = [{
          "type": "section",
          "text": {"type": "mrkdwn", "text": "Pick a date for me to remind you"},
          "accessory": {
              "type": "datepicker",
              "action_id": "datepicker_remind",
              "initial_date": "2020-05-04",
              "placeholder": {"type": "plain_text", "text": "Select a date"}
          }
        }]
        say(
            blocks=blocks,
            text="Pick a date for me to remind you"
        )

@app.action("button-action1")
def action_button1(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Ok! What do you want to know?"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Address"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-company1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Account Type Field"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-company2"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Credit segmentation"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-company3"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Company ID (US/RoW)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-company4"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Data sync (process)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-company5"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Account Team (sales process)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-company6"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Business units (definition & rules)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-company7"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Delete"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-company8"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Sales/AS fields (Retail Media)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-company9"
                }
            }
            ]
    say(blocks=blocks)
    
@app.action("button-company3")
def action_button_company3(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Definition*: The Credit Segmentation is necessary in order to enable the sales to create an initial IO from the Opportunity. It depends on the Applicated Monthly Revenue (AMR), which is either the observed revenue of the company or the estimated revenue of the company + the estimated revenue of the advertiser associated."
                }
            },
            {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Credit Segmentation",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/qvtLmzvn/amr-credit-seg.png",
                    "alt_text": "image1"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":arrow_right: The Prospect Segmentation must be populated at the Company Level, so the Credit Segmentation field would populate automatically (it could take time). Otherwise, ask the sales what value to put and use Salesforce Inspector to populate (:warning: When populating in the inspector field, save before clicking on the right arrow, to be sure to populate the value)."
                }
            }
            ]
    
    say(blocks=blocks)
    
@app.action("button-company4")
def action_button_company4(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":eyes: The Company ID is a way to identify exactly the company account related to an IO. The format could be specific (there is a major difference between the US and the Rest of the World). If the format is inaccurate, there will be erros at the opportunity and IO level."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":arrow_right: Go to the Account page. If the format is inaccurate, notice that an error message shows up in the right of the page (even before saving any change). Generally, this message indicates the right format to use. It is often sufficient to add an hyphen or a space at the good place to fix the problem."
                }
            },
            {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Company ID error message",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/J0r9FBhR/id-format.png",
                    "alt_text": "image1"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Sometimes it happens that the sales need to ask again to the client for the Company ID, when the error persists or when the ID is missing."
                }
            }
            ]
    say(blocks=blocks)

@app.action("button-company5")
def action_button_company5(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "The Data Sync is a *process* that enables to synchronise an account with a previous one. It retrieves the historical IOs and Opportunities and makes the current account eligible for IO submission."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":eyes: Check the billing address and the company ID, and compare to the ones of the previous account. If they are corresponding, you can synchronise with this account. If not, select *No match found* (:warning: This option is not very usual)."
                }
            }
            ]
    say(blocks=blocks)

@app.action("button-company8")
def action_button_company8(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning: Be very careful before deleting an account. It can have huge consequences."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":eyes: Check if there is any opportunity linked to this IO, \"RM Opportunity\" tab. If not, then you can delete the account."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":no_entry_sign: If you find existing opportunities, ask the sales to link them to another account before doing anything."
                }
            }
             ]
             
    say(blocks=blocks)
    
@app.action("button-action2")
def action_button2(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Ok! If you are changing the platform of a signed IO, do not forget to *uncheck* (i.e. *un-sign*) *the IO*. \n What is the type of change?"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Any platform -> RMP "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-platform1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Erms or RSX -> Erms or RSX"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-platform2"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "RMP -> Erms or RSX"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-platform3"
                }
            }
            ]
    say(blocks=blocks)
    
@app.action("button-platform1")
def action_platform1(ack, say):
    ack()
    blocks = [{
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Okay, you need to follow the steps below:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*:one: Check if there is not already an existing Contracutal Account with the new platform*. Go to the hierarchy icon and look for the accurate CA. To do that, click on the current CA and then you will find the hierarchy icon to the right of the name above. \n If you find the CA field empty (rare), try the Company/Advertiser name."
                    }
                },
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Hierarchy icon",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/9F6nqxLc/chatterbot-hierarchy.png",
                    "alt_text": "image1"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":two: If the accurate CA already exists, click on it and copy the ID in the URL. Then use Salesfroce Inspector to paste the new ID in the contractual account field, for the IO in question. Then you can change the platform field."
                    }
                },
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Contractual Account ID in URL",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/3N1p5n2D/chatterbot-ca-id.png",
                    "alt_text": "image1"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":three: Finally, the sales need to resign the IO with the client. If it is already done, just check the box 'IO Signed by Client' :white_square: (do not forget to put \"manual signature\")."
                    }
                },
                {
                    "type": "divider"
                }
                ]
    
    say(blocks=blocks)
    
@app.action("button-platform2")
def action_platform2(ack, say):
    ack()
    blocks =blocks = [{
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Okay, you need to follow the steps below:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*:one: Check if there is not already an existing Contracutal Account with the new platform*. Go to the hierarchy icon and look for the accurate CA. To do that, click on the current CA and then you will find the hierarchy icon to the right of the name above. \n If you find the CA field empty (rare), try the Company/Advertiser name."
                    }
                },
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Hierarchy icon",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/9F6nqxLc/chatterbot-hierarchy.png",
                    "alt_text": "image1"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":two: If the accurate CA already exists, click on it and copy the ID in the URL. Then use Salesfroce Inspector to paste the new ID in the contractual account field, for the IO in question. Then you can change the platform field."
                    }
                },
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Contractual Account ID in URL",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/3N1p5n2D/chatterbot-ca-id.png",
                    "alt_text": "image1"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":three: Finally, the sales need to resign the IO with the client. If it is already done, just check the box 'IO Signed by Client' :white_square: (do not forget to put \"manual signature\")."
                    }
                },
                {
                    "type": "divider"
                }
                ]
    say(blocks=blocks)

@app.action("button-platform3")
def action_platform3(ack, say):
    ack()
    blocks = [{
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Okay, you need to follow the steps below:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*:one: Check if there is not already an existing Contracutal Account with the new platform*. Go to the hierarchy icon and look for the accurate CA. To do that, click on the current CA and then you will find the hierarchy icon to the right of the name above. \n If you find the CA field empty (rare), try the Company/Advertiser name."
                    }
                },
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Hierarchy icon",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/9F6nqxLc/chatterbot-hierarchy.png",
                    "alt_text": "image1"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":two: If the accurate CA already exists, click on it and copy the ID in the URL. Then use Salesfroce Inspector to paste the new ID in the contractual account field, for the IO in question. Then you can change the platform field."
                    }
                },
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Contractual Account ID in URL",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/3N1p5n2D/chatterbot-ca-id.png",
                    "alt_text": "image1"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":three: Contact Goeffrey Sorel, to tell him to change the Financial Account linked to this IO (this is the only case where this step is necessary)."
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":four: Finally, the sales need to resign the IO with the client. If it is already done, just check the box 'IO Signed by Client' :white_square: (do not forget to put \"manual signature\")."
                    }
                },
                {
                    "type": "divider"
                }
                ]
    
    say(blocks=blocks)

@app.action("button-action3")
def action_button3(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Ok! What do you want to know?"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning: Sales/AS are the one creating contacts"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-contact1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Deleting contact process"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-contact2"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Active/inactive account"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-contact3"
                }
            }
            ]
    say(blocks=blocks)
    
@app.action("button-action4")
def action_button4(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Ok! Pick a topic!"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Close date rule"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-opportunity1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Opportunity product (definition & rules)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-opportunity2"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Creation renewal (IO and CA)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-opportunity3"
                }
            }
            ]
    say(blocks=blocks)
    
@app.action("button-opportunity1")
def action_opportunity1(ack, say):
    ack()
    blocks = [  {
                "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "You need to be careful since the close date is the source of many mistakes and errors in Salesforce."
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Definition*: The close date is the date when the negociations end, the IO is signed. You can find the close date field at *the Opportunity level*. The most important is to know that *the close date cannot be higher than the launch/start date of the campaign*!"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":white_check_mark: While changing end/start dates, sometimes it is necessary to change the close date. Generally, it is sufficient to put the last date before the beginning of the campaign."
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":warning: Sometimes, the opportunity is in the past, so you have to put the close date in the past. Salesforce does not allow you to do that, so you have to check the *bypass validation rules* in your settings as an exception."
                    }
                },
                {
                    "type": "divider"
                }
                ]
    
    say(blocks=blocks)

@app.action("short_cut_close_date")
def action_opportunity1_shortcut(ack, say):
    ack()
    blocks = [  {
                "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "You need to be careful since the close date is the source of many mistakes and error in Salesforce."
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Definition*: The close date is the date when the negociations end, the IO is signed. You can find the close date field at *the Opportunity level*. The most important is to know that *the close date cannot be higher than the launch/start date of the campaign*!"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":white_check_mark: While changing end/start dates, sometimes it is necessary to change the close date. Generally, it is sufficient to put the last date before the beginning of the campaign."
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":warning: Sometimes, the opportunity is in the past, so you have to put the close date in the past. Salesforce does not allow you to do that, so you have to check the *bypass validation rules* in your settings as an exception."
                    }
                },
                {
                    "type": "divider"
                }
                ]
    
    say(blocks=blocks)

@app.action("button-action5")
def action_button5(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Ok! What do you want to know about IOs?"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Everything about IO Details"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Pending validation"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io2"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Cancelled field (definition)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io3"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "IO Signed box"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io4"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "PPC Box"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io5"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Revised budget and other modifications"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io6"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Notes and attachments"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io7"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Change Order (upsell/downsell)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io8"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Working media budget"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io9"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Commercial terms/payment terms"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io10"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Company changes"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-io11"
                }
            }
            ]
    say(blocks=blocks)
    
@app.action("button-action6")
def action_button6(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Ok! What do you want to know about Contractual Accounts (aka CA)?"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Global explanation (creation, naming, rules)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-ca1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Alignment with Initial IO"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-ca2"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "CPOP ID"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-ca3"
                }
            }
            ]
    say(blocks=blocks)
    
@app.action("button-action7")
def action_button7(ack, say):
    ack()
    say("Nothing to show, for now!")
    

######## Action for the IO Details below ---------------------------------

@app.action("button-io1")
def action_button1_io(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Ok! What do you want to know about IO Details?"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Date change (start/end)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-iod1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Change Order process"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-iod2"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "IO Product vs. Change Order (explanation)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-iod3"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Status (cancelled/validated)"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-iod4"
                }
            }
            ]
    say(blocks=blocks)
    
@app.action("button-io2")
def action_button_io2(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "The status of an IOD is on pending validation when the IO is sent and the Retail Media team has to approve it. *You cannot change this status* since the contract is send and there is no modification to be done."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":white_check_mark: But sometimes, modifications need to be done. So you have to ask the sales to *void the envelope*."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Definition*: Void the envelope means that you make the contract juridically null and void (in order to make new changes and to send the contract again). It is the job of the sales to do it."
                }
            },
            ]
    say(blocks=blocks)
    
@app.action("button-io4")
def action_button_io4(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Usually*, the IO Signed Box is checked automatically when the client signs the contract. Then the *IO Type* is \"Standard with Electronic Signature\". If the IO Type is \"Standard with Manual Signature\", the Sales has to check the IO Signed box."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":arrow_right: Sometimes, it happens that you have to uncheck the IO Signed box, for several reasons (generate a new Contractual Account, save a platform change, etc.). In this case, you have to *select the \"Standard with Manual Signature\" for the IO Type field* otherwise Salesforce won't enable you to un-sign the IO."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning::eyes: If a sales ask you to check the IO Signed box, first you have to verify if there is actually a signed contract in the *Notes & Attachments* section. Then you can check the box."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":no_entry_sign: Sometimes it happens you encounter an *approval issue*. It can be a mistake since the IO is already signed (and then, necessarily approved). In this case :arrow_right: go to the Salesforce Inspector, look for \"Approval\" in the search bar and populate *Approved* wherever it's possible (when you see the \"picklist\" option in the Type column)."
                }
            },
            {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "IO Change Type",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/xTt8QbwJ/approved-inspector.png",
                    "alt_text": "image1"
            }
             ]
    
    say(blocks=blocks)
            

@app.action("button-io11")
def action_button_io11(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":one: First of all, check if the IO is already signed or not. If it is not, just change the company name."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":two: If the IO is already signed, *you have to un-sign the IO* because resigning the Initial IO will create a new Contractual Account. Then populate the *Non Standard  RMP Account* to *yes*. You have to be careful to the following condition:"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":white_check_mark: If the VATs (or Company ID) is the same, there is no need to ask the client for legal approval, just re-apply old signature date via dataloader."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":x: If there is a different VATs (or Company ID), you need to un-sign (again) and to ask for a new legal approval. Then, the sales would need to use DocuSign again, so *do not forget to put the IO Type to\"Electronic Signature\"*."
                }
            }
             ]
    say(blocks=blocks)
    
@app.action("button-iod1")
def action_button_iod1(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Ok! That's one of the most common task. Follow the steps below."
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":one: First, you have to check if the sales need to make a Change Order for *\"date extension\"*. If only the end date is postponed, meaning that the campaign duration is extended, then the sales needs to make this Change Order."
                    }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":two: Otherwise, you have to go to the *IO Details* and change the dates at the IOD level."
                    }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":three: If the dates did not change automatically at the IO level, change them."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":eyes: It would be necessary to have the \"*IO Change Type*\" field populated. If this is not the case, ask to the sales what value to put."
                }
            },
            {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "IO Change Type",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/1Xg7WrBp/IO-change-type.png",
                    "alt_text": "image1"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":no_entry_sign: The launch/start date must be higher than the close date                       :arrow_right:"     
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "short_cut_close_date"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":no_entry_sign: In the Change Order case, *you must not populate the start/end dates* if they already exist in the IOD. Just populate the \"Original Start Date\" and the \"Original End Date\"."
                }
            }
            ]
    say(blocks=blocks)  


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()