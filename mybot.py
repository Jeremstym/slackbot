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

######### Company Account questions ###########################

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
                    "text": ":arrow_right: The \"Prospect Segmentation - Estimated Monthly Revenue\" must be populated at the Company Level, so the Credit Segmentation field would populate automatically (it could take time). Don't try to use Salesforce inspector to make the change directly on the CS field unless it is strictly necessary."
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
                    "text": ":eyes: The Company ID is a way to identify exactly the company account related to an IO. The format could be specific (there is a major difference between the US and the Rest of the World). If the format is inaccurate, there will be errors at the opportunity and IO level."
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

@app.action("button-company7")
def action_button_company7(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Definition*: The Business Unit is a box to check or not at the Account level. If it is checked, it means that the Account is a \"clone\" of another one, but named differently because there are two sales for the same company (for instance, Asus Canada is a business unit, derived from Asus US). Apart from that, the Company ID and the Billing Address are the same, but the RM Sales/AS change. It is a way to split the ownership and keep the same billing entity."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning: There is a procedure to follow while switching an account from company to business unit:"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":one: Uncheck the *IO Signed Box* (don't forget to choose manual signature to do so). Switch status bar to \"Approved\" if it is not done automatically."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":two: *Remove the attached Contractual Account* (use Salesforce Inspector to erase the corresponding field) and then update the needed changes (regarding business unit)."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":three: Check the *IO Signed Box*, always in the same Initial IO. It would generate a new Contractual Account. Make sure that the update is done in RMP."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":four: Move all Budget IOs to the new Contractual Account (simply change the Contractual Account field at the Budget IO level)."
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
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":white_check_mark: If you cannot delete the account for the previous reasons, you may at least change the account name and put \"DO NOT USE\"."
                }
            }
             ]
             
    say(blocks=blocks)
    
############### Platform change questions ####################
    
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
                        "text": ":three: If the changing is RMP :arrow_right: Erms, *contact Goeffrey Sorel*, to tell him to change the Financial Account linked to this IO (this is the only case where this step is necessary)."
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

############### Contact questions ################

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
    
############ Oportunity questions ########################"
    
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
                        "text": "*Definition*: The close date is the date when the negotiations end, the IO is signed. You can find the close date field at *the Opportunity level*. The most important is to know that *the close date cannot be higher than the launch/start date of the campaign*!"
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

@app.action("button-opportunity2")
def action_button_op2(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Definition*: An opportunity product is linked to the sold product in a contract. It can be for instance a Commerce display, a Sponsored product, etc. An opportunity product is created just after the creation of an opportunity. You can find the list of opportunity products in the associated tab, at the Opportunity level."
                }
            },
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "Opportunity product example",
                    "emoji": True
                },
                "image_url": "https://i.postimg.cc/wjB5zwRf/op-ex1.png",
                "alt_text": "image1"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning: *When the Opportunity is linked to a signed IO, you cannot create new opportunity products*. If necessary, the associated IO needs to be cancelled. Then the sales can add an Opportunity Product and create a new IO."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":eyes: It is possible to have only one Initial IO by Opportunity. If you want a new Initial IO, you have to cancel the previous one."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Creating an Opportunity Product is creating an IOD on the related IO in the same time*, with the same product (IO Product). The two products have to be the same, otherwise there would be an error. You can find the related IOD in the IO Details tab of the corresponding IO."
                }
            },
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "OP to IOD",
                    "emoji": True
                },
                "image_url": "https://i.postimg.cc/7hnr0YLP/op-ex2.png",
                "alt_text": "image1"
            },
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "IO Product and OP",
                    "emoji": True
                },
                "image_url": "https://i.postimg.cc/Jn8TJ3HJ/op-ex3.png",
                "alt_text": "image1"
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
                        "text": "*Definition*: The close date is the date when the negotiations end, the IO is signed. You can find the close date field at *the Opportunity level*. The most important is to know that *the close date cannot be higher than the launch/start date of the campaign*!"
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
    
############## IO Questions ################################

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
                    "text": "Commercial conditions/Payment terms"
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
    
#---------------- IOD questions -------------------------
    
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
    
######----------------------------------------------------

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
                    "text": "The status of an IOD is on pending validation when the IO is sent and the Retail Media team has to approve it. *You cannot change this status* since the contract is sent and there is no modification to be done."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":white_check_mark: But sometimes, modifications need to be done. So you have to ask the sales to *void the envelope*. For instance, it is necessary when you encounter this error:"
                }
            },
            {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Pending Validation error",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/zvKbmz10/pending-validation-error.png",
                    "alt_text": "image1"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Definition*: Void the envelope means that you make the contract juridically null and void (in order to make new changes and to send the contract again). It is the job of the sales to do it."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":eyes: If a sales cannot find the button, give the following indications.\n :arrow_right: Go to the *DocuSign Status* tab and click on the accurate \"DSX-XXXXX\". The button will appear to the top right corner of the screen."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning: If the IO is signed, voiding the envelope can't be done."
                }
            }
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
                        "text": "Approval fields",
                        "emoji": True
                    },
                    "image_url": "https://i.postimg.cc/xTt8QbwJ/approved-inspector.png",
                    "alt_text": "image1"
            }
             ]
    
    say(blocks=blocks)
    
@app.action("button-io5")
def action_button_io5(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Definition: Pay Per Consumption*: The client can add more budget when it's necessary without signing a new IO. PPC is used when there is no start/end dates. It is enough to sign one IO at the start."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning: Having an end date AND a PPC Box checked may cause some troubles. Ensure that there is no such kind of duplication."
                }
            }
            ]
          
    say(blocks=blocks)
    
@app.action("button-io10")
def action_button_io10(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":arrow_right: When we want to change the commercial conditions/payment terms (Client Mode, DSP, Fees, Commercial conditions, etc.), it is necessary to make a new *amendment* and to sign it. Amendments can be created at the Initial IO page level, where you will find a button. They have to appear on the generated contract at the end."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":eyes: Don't forget to copy the field that you want to preserve such as \"Client Mode\" or \"Send Bill Option\". If you choose *Managed* for the \"Client Mode\", you would have to populate the Managed Fees (and the dates)."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning: The *\"Contract Particular Conditions\" field is legal binding*, it requires an approval. Populate the \"Commercial Conditions\" field instead if possible."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":white_check_mark: However, if the commercial conditions/payment terms of an amendment are wrong from the start, it is possible to directly make the changes on the amendment (no need to create a new one)."
                }
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
                    "text": ":two: If the IO is already signed, *you have to un-sign the IO* because resigning the Initial IO will create a new Contractual Account. Then populate the *Non Standard  RMP Account* to *yes* if the platform is RMP. You have to be careful to the following condition:"
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
                    "text": ":x: If there is a different VATs (or Company ID), you need to un-sign (again) and to ask for a new legal approval. Then, the sales would need to use DocuSign again, so *do not forget to put the IO Type to \"Electronic Signature\"*."
                }
            }
             ]
    say(blocks=blocks)
    
    
############# Contractual Account questions ##############
    
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
    
@app.action("button-ca2")
def action_button_ca2(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "The Contractual Account is strongly related to an Initial IO. It appears automatically when an Initial IO is signed, and gets all its information from it. There are many things to be aware of:"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":no_entry_sign: *It is totally unusual to modify information directly on a CA* (even if a sales ask you to do it, don't, unless it is necessary)."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning: You will notice that a CA is linked to one and only one Initial IO. However, many types of IO can be related to a CA (such as Budget IO for instance). It is possible to change the related Initial IO of a Budget IO in order to link this Budget IO to the corresponding CA."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning::eyes: The Contracted Agency, if it exists, must be exactly the same in the IO and in the CA. You cannot simply change a Contracted Agency, nor put a new one, in an IO, since it is linked to a CA which says differently. To get further details :arrow_right: go to the Agency section."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":warning::eyes: That is the same thing for the platforms. To get further details    :arrow_right:" 
                },
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button-action2"
                }
            }
            ]
    say(blocks=blocks)
    
########################## Agency change questions ##############################

@app.action("button-action7")
def action_button7(ack, say):
    ack()
    blocks = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "It's easy to change of Managed Agency. But the *Contracted Agency is legal binding*. So you cannot change it freely because the IO is related to a CA which depends on this Contracted Agency as well."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":arrow_right: If a sales needs to change the Contracted Agency of an IO, or to add one, he has to create a new Initial IO. Signing it will create a new CA, with the Contracted Agency in the name. If the previous IO was a mistake, since the agency was inaccurate, it has to be cancelled."
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":white_check_mark: Sometimes, it may happen that the IO already has a Contracted Agency, but the related CA has not. In this case, you have to link the IO with the correct CA. Don't forget to ensure that the CA and the IO are related to the same Initial IO, otherwise make the correction *at the IO level*."
                }
            }
            ]
    say(blocks=blocks)
    


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
