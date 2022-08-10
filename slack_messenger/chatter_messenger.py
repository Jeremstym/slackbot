#-----*utf-8*-------
# Chatter messages definition for the Chatter Bot

import re

class ChatterMessenger:    
    
    def __init__(self):
        self.backup = "In case of issues with the app, go to: \
        https://criteo.atlassian.net/wiki/spaces/RMLTC/pages/1811679505/The+Chatter+Bot+inside+out+WiP"
    
    def start(self, app):
        
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
            
        @app.message(re.compile("(help|Help)"))
        def message_help(say):
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Hey there :elephant: Welcome to the Chatter Bot. Here you\
can select every topics you need to know more about. To start the exploration, just write \"start\"."
                        }
                    }
                    ]
                    
            say(blocks=blocks, text=self.backup)

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
            say(f"<@{body['user']['id']}> clicked the button. Now you can write \"start\".")
            
            
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
                    ]
                    
            say(blocks=blocks, text=self.backup)

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
                            "text": ":arrow_right: The \"Prospect Segmentation - Estimated Monthly Revenue\" must be populated at the Company Level, so the Credit Segmentation field would populate automatically (it could take time)."
                        }
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
                    }
                    ]
            
            say(blocks=blocks, text=self.backup)
            
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
                            "text": "Sometimes it happens that the sales needs to use a surrogate ID in the meanwhile, with the accurate format. In this case, a new change in the Company ID field would be necessary. The sales has to ask the company/client for it."
                        }
                    }
                    ]
            say(blocks=blocks, text=self.backup)

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
                            "text": "The Data Sync is a *process* that enables to synchronise an account with the Parent Account. It makes the current account eligible for IO submission. The Data Sync button is located in the top right corner of the account page."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":eyes: Check the billing address and the company ID, and compare to the ones of the current account. If they are corresponding, you can synchronise with this account. The recommended accounts appear by matching score order. The most probable parent account is the first one. If there is no relevant match, select *No match found*."
                        }
                    }
                    ]
            say(blocks=blocks, text=self.backup)

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
                            "text": "*Definition*: The Business Unit is a box to check or not at the Account level. If it is checked, it means that the Account is a \"clone\" of another one, but named differently because there are two sales for the same company (for instance, Asus Canada is a business unit, derived from Asus US). Apart from that, the Company ID is the same, but the RM Sales/AS change. It is a way to split the ownership and keep the same billing entity."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: There is a procedure to follow *at the IO level* while changing an account from a company to a business unit:"
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
                    
            say(blocks=blocks, text=self.backup)

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
                            "text": ":no_entry_sign: If you find existing linked opportunities, ask the sales what to do."
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
                     
            say(blocks=blocks, text=self.backup)
            
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
                            "text": "Ok! If you are changing the platform of a signed IO, do not forget to *uncheck* (i.e. *un-sign*) *the IO*. \n Secondly, be very aware of *the type of IO* you are dealing with : Initial IO (the current term of the CA) or Budget IO.\n What is the type of change?"
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
            say(blocks=blocks, text=self.backup)
            
        @app.action("button-platform1")
        def action_platform1(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":arrow_right: If you are on a CA's current term (Initial IO), just change the platform. When the IO would be signed, a new CA would be generated."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning::arrow_right: If the current term is an Amendment IO, you have to correct the platform on both the Initial IO and the Amendment IO. *Then check and uncheck the PO Required Flag* (or the other way around if it is already checked) in order to register the change in BRIM. Then, if there are Budget IOs, change the platform on these IOs."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":arrow_right: If you are on a Budget IO, you need to follow the steps below:"
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
                            "text": ":two: If the accurate CA already exists, click on it and copy the ID in the URL. Then use Salesfroce Inspector to paste the new ID in the contractual account field, for the IO in question. Only after that, you can change the platform field."
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
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: If there is no CA with the corresponding platform, the Budget IO needs to be transformed into an Initial IO."
                        }
                    }
                    ]
            
            say(blocks=blocks, text=self.backup)
            
        @app.action("button-platform2")
        def action_platform2(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":arrow_right: If you are on a CA's current term (Initial IO), you can make the change freely."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":arrow_right: If you are on a Budget IO, you need to follow the steps below:"
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
                            "text": ":two: If the accurate CA already exists, click on it and copy the ID in the URL. Then use Salesfroce Inspector to paste the new ID in the contractual account field, for the IO in question. Only after that, you can change the platform field."
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
                    }
                    ]

            say(blocks=blocks, text=self.backup)

        @app.action("button-platform3")
        def action_platform3(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":arrow_right: If you are on a CA's current term (Initial IO), check if there are commercial conditions or not. If there are not, then the sales needs to generate a CPOP ID. The platform needs to be changed in the Initial IO AND in the Contractual Account. Then change the platform fields in the associated Budget IOs. However, *if there are specific commercial conditions in the IO PDF*, the sales needs to sign a new Initial IO. Then the associated Budget IOs need to be changed to the new Contractual Account (follow the steps bellow). And then, change the platform fields at the Budget IO level."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*For the Budget IOs, you need to follow the steps below:"
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
                            "text": ":two: If the accurate CA already exists, click on it and copy the ID in the URL. Then use Salesfroce Inspector to paste the new ID in the contractual account field, for the IO in question. Only after that, you can change the platform field."
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
                            "text": ":three: If the changing is RMP :arrow_right: Erms and if the Budget IO is signed, *contact Goeffrey Sorel*, to tell him to change the Financial Account linked to this IO (this is the only case where this step is necessary)."
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
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: If there is no CA with the corresponding platform, the Budget IO needs to be transformed into an Initial IO."
                        }
                    }
                    ]
            
            say(blocks=blocks, text=self.backup)

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
                            "text": "Active/Inactive contacts"
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
            say(blocks=blocks, text=self.backup)
            
            
        @app.action("button-contact1")
        def action_button_contact1(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":no_entry_sign: *DON'T EVER DO IT BY YOURSELF*."
                        }
                    }
                    ]
                    
            say(blocks=blocks, text=self.backup)
            
        @app.action("button-contact2")
        def action_button_contact2(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Sometimes you can be asked to delete a contact from the account page of a company. You have to follow some steps to do so:"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":one: Go to the Contacts tab at the Account level and spot the contacts you have to delete. If there is a trash icon on the left, click on it."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":two: If there is not, click on the contact name. In the contact account page, change the *Account Name* field (which is related to the company account you're working on), remove the company name and replace it by a test account (the most used is *Test Selin Company* for instance)."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":three: Return to the Contacts tab of the Company page. The trash icon appears now, you can click on it."
                        }
                    }
                    ]
                    
            say(blocks=blocks, text=self.backup)

        @app.action("button-contact3")
        def action_button_contact3(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Sometimes, the fact that the client contact of an IO is inactive (meaning that the persons left or has changed of job) prevents the updates or the sending from being made. It is necessary to change the owner to an active member."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":eyes: A contact can be inactive if the email address is not detected as valid."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":arrow_right: After checking with the sales, two solutions: either it is an error of Salesforce and then you go to the contact page and change the status to active (in the corresponding field), or the contact is really inactive and you have to change it, with the sales agreement."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: An inactive contact cannot be used as Primary Contact nor eSigner. It has to be active and valid."
                        }
                    }
                    ]
            
            say(blocks=blocks, text=self.backup)
            
        ############ Opportunity questions ########################"
            
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
            say(blocks=blocks, text=self.backup)
            
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
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": ":white_check_mark: It happens that a sales want to create an opportunity for a campaign that has already run and ended. In this case, the sales has to create the opportunity and the IO with the wrong dates (because Salesforce will not allow dates in the past), and then you can change the dates with the bypass validation, once everything is completed."
                            }
                        }
                        ]
            
            say(blocks=blocks, text=self.backup)

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
                            "text": ":eyes: It is possible to have only one Initial IO OR one Renewal IO by Opportunity. If you want to create a new IO, you have to cancel the previous one."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Creating an Opportunity Product entails the creation of an IOD on the related IO in the same time*, with the same product (IO Product). The sales have to link the OP to the IOD (it is not done automatically). The two products have to be the same, otherwise there would be an error. You can find the related IOD in the IO Details tab of the corresponding IO."
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
                    
            say(blocks=blocks, text=self.backup)

        @app.action("button-opportunity3")
        def action_button_opp3(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "A Renewal IO, like an Initial IO, is created from an opportunity. *It is not possible to have an Initial IO and a Renewal IO for the same opportunity*."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":eyes: Unlike an Initial IO, a Renewal IO does not contain Billing information, it is shorter. A Renewal IO is created when an Initial IO already exists with the company, it is used to restart a campaign, to change some information like the budget amount. *A Budget IO and a Renewal IO are the same thing*."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: While creating a Renewal IO, it is necessary to be careful about the alignment with the Contractual Account (same Contracted Agency for instance, same Initial IO if it is a Budget IO. As a reminder, a new Contractual Account is created when an Initial IO is signed). To see further details about CA :arrow_right:"
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
                    }
                    ]
                    
            say(blocks=blocks, text=self.backup)
            
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
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Billing Option change"
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Click Me",
                                "emoji": True
                            },
                            "value": "click_me_123",
                            "action_id": "button-io12"
                        }
                    }
                    ]
            say(blocks=blocks, text=self.backup)
            
            
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
            say(blocks=blocks, text=self.backup)
            
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
                            "text": "That's one of the most common task. A sales wants to update the IO dates because the clients asked for it or because the billing team did. Follow the steps below."
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
                            "text": ":arrow_right: The correct process is to do a *Change Order* for *date extension* in this case. When the billing team asks for a date change, just change the dates at the IO level, not at the IOD level."
                            }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: If the CO \"date extension\" has been made, check the IO Details tab, if there is indeed a Change Order for date extension."
                            }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":two: Otherwise, if this is not a \"date extension\" matter, you have to go to the *IO Details* and change the dates at the IOD level."
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
                            "action_id": "button-opportunity1"
                        }
                    },
                    ]
            say(blocks=blocks, text=self.backup)  
            
        @app.action("button-iod2")
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
                            "text": "*Definition*: A Change Order is an operation that enables to extend the campaign dates or to modify the budget of the campaign (upsell/downsell). The sales has to create the Change Order at the IO level, select the correct Change Order Type and then link it to the corresponding IO Product (cf. Opportunity Product). This operation updates the Revised Budget (when the status is \"Validated\" or \"Pending Validation\")."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: When the Change Order is a downsell, the budget amount must be negative (with the minus sign)."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":eyes: Sometimes, an error occurs when creating a CO with an end date lower than the Original End Date. In this case, remove the Original End Date and adapt the main page of the IO."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: To create a new Change Order, it is necessary that *the previous one is either Validated or Cancelled*."
                        }
                    }
                    ]
            
            say(blocks=blocks, text=self.backup)
            
        @app.action("button-iod3")
        def action_button_io3(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Basically, an IO Product is the first IOD created with an IO. It is linked to an Opportunity Product, linked to the product sold with the contract (for instance, Commerce Display). A Change Order is created after, when a change in the budget amount or in the campaign dates is necessary. These are IODs as well."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: Even if a Change Order is cancelled, it must be linked to an IO Product, otherwise Salesforce sends an error."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":eyes: It is important to link a CO to the IO Product, because it gets the information from it (dates, budget, etc.). It retrieves the features of the Opportunity Product, related to the IO. All this information is visible in the PDF contract."
                        }
                    }
                    ]
                    
            say(blocks=blocks, text=self.backup)
            
        @app.action("button-iod4")
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
                            "text": "*The Change Order status* depends on the signature of the IO/IOD. When a CO is created, the original IO is already signed. The status is then \"New\" for the CO. When it is \"Pending Validation\", the CO has been sent to the client for approval and signature. When it is \"Validated\", all the parties have signed the new contract."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: It is not possible to create a Change Order if there is already a Change Order \"New\" or \"Pending Validation\". If a sales needs to make changes, put the status on \"New\" so it is possible to directly make the modifications on the CO. Otherwise, it is also possible to cancel the current CO and to create a new one."
                        }
                    }
                    ]
                    
            say(blocks=blocks, text=self.backup)
                    
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
                            "text": "The status of an IO is equal to \"pending validation\" when the IO is sent to the client. *You cannot change this status* since the contract is sent and we are not able to make any modification."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":white_check_mark: But sometimes, modifications need to be done when the sales ask for it, but they forgot to \"void the envelope\" before reaching out in Chatter. So you have to ask the sales to *void the envelope*. For instance, it is necessary when you encounter the following error message:"
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
                            "text": "*Definition*: Void the envelope means that you make the contract juridically null and void (in order to make new changes and to send the contract again). It is the job of *the sales who sent the contract* to do it."
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
            say(blocks=blocks, text=self.backup)

        @app.action("button-io3")
        def action_button_io3(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":x: When the business is cancelled or the sales made a mistake about the IO features, the IO has to be cancelled and it will not be taken into account in the reporting."
                        }
                    }
                    ]
            
            say(blocks=blocks, text=self.backup)
            
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
                            "text": "*Usually*, the IO Signed Box is checked automatically when the client signs the contract if the *IO Type* is \"Standard with Electronic Signature\" or \"Third Party\". If the IO Type is \"Standard with Manual Signature\", the Sales has to check the IO Signed box."
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
                            "text": ":warning::eyes: If a sales asks you to check the IO Signed box, first you have to verify if there is actually a signed contract in the *Notes & Attachments* section. Then you can check the box."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":no_entry_sign: Sometimes it happens you encounter an *approval issue*. It can be a mistake since the IO is already signed (and then, necessarily approved). In this case :arrow_right: go to the Salesforce Inspector, look for \"Approval\" in the search bar and populate *true* for the \"In Approval\" field."
                        }
                    },
                    {
                            "type": "image",
                            "title": {
                                "type": "plain_text",
                                "text": "Approval fields",
                                "emoji": True
                            },
                            "image_url": "https://i.postimg.cc/vHts2VYP/approved-inspector.png",
                            "alt_text": "image1"
                    }
                     ]
            
            say(blocks=blocks, text=self.backup)
            
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
                            "text": "*Definition: Pay Per Consumption*: The Client pays for what he needs for his use. For instance, if the client doesn't run a campaign, the total paid amount would be 0. The client can add more budget when it's necessary without signing a new IO."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":eyes: Generally, when the PPC Box is checked, there is no end date and the budget amount is equal to 0. This is visible in the PDF contract."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: Sometimes, it is also necessary to have the Budget Type populated with \"Uncapped\" if the PPC Box is checked."
                        }
                    }
                    ]
                  
            say(blocks=blocks, text=self.backup)
            
        @app.action("button-io6")
        def action_button_io6(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Definition*: The Revised Budget is a field located at the IO level. It must be equal to the Original Budget + the Change Order amount (downsell or upsell). The Change Order has to be either validated or pending validation, it would be taken into account (this it not the case if the CO status is \"New\" or \"Cancelled\". The budget would be visible on the contract when it is modified."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "When a sales asks for modifying a budget, it is generally about the Revised Budget, but the sales might want to modify the Original Budget as well sometimes. :warning: Sometimes, an error occurs and it is necessary to change the budget manually. In this case, check if the Change Orders exist before modifying the budget."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":eyes: Sometimes, it is necessary to void the envelope when changing the budget of an IO not signed yet."
                        }
                    }
                    ]
                    
            say(blocks=blocks, text=self.backup)

        @app.action("button-io7")
        def action_button_io7(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":eyes: This is the place where you can find the contracts, signed or not. When the contract is signed, the sales have to upload it in this area when it is not done automatically. The area is located to the bottom right of the IO page."
                        }
                    }
                    ]
                    
            say(blocks=blocks, text=self.backup)

        @app.action("button-io9")
        def action_button_io9(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Definition*: The Working Media Budget is the budget of the campaing, minus the part that Criteo takes. The formula is: WMB = Original Budget - (DSP Fees x Original Budget + Managed Service Fees x Original Budget)"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: If a sales asks to modify a WMB so it's equal to a specific value, it is not possible. Generally, the sales has forgotten to populate the DSP or the Managed fees."
                        }
                    }
                    ]
            
            say(blocks=blocks, text=self.backup)

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
                            "text": ":white_check_mark: However, if the commercial conditions/payment terms of an amendment are wrong from the start, it is possible to directly make the changes on the amendment or on the IO (no need to create a new one) *but you have to follow the same procedure than for the agency changes* :arrow_right:"
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
                    
            say(blocks=blocks, text=self.backup)
                    
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
            say(blocks=blocks, text=self.backup)
            
        @app.action("button-io12")
        def action_button_io12(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "If the Billing Options are wrong, due to a mistake, you have to follow the same procedure than for the agency changes due to a mistake, step by step :arrow_right:"
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
                    
            say(blocks=blocks, text=self.backup)
            
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
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Merge of CA"
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Click Me",
                                "emoji": True
                            },
                            "value": "click_me_123",
                            "action_id": "button-ca4"
                        }
                    }
                    ]
            say(blocks=blocks, text=self.backup)
            
        @app.action("button-ca1")
        def action_button_ca1(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "There are some things to know while dealing with Contractual Accounts:"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":warning: A new Contractual Account is created only when an Initial IO is signed. The CA would be related to it (unless you make changes in the connections). That is why when you make important updates at the IO level (platform, company, agency), you have to either re-sign the IO or to link the IO to an existing CA. In the last case, remember that a Budget IO and its related CA always have to be linked to the same Initial IO. If they are not, make the change at the IO level, never at the CA level."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":eyes: Here is how you have to understand the name of a CA.\n 1. CA stands for Contractual Account \n 2. Then comes the name of the Company Account, linked to the current IO \n 3. There here is the name of the mentioned platform of the IO \n 4. Here comes a precision regarding the Client mode : Managed Service (MS) or Self Service (SS) \n 5. If it exists, the name ends by the Contracted Agency"
                        }
                    },
                    {
                        "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "Contractual Account name",
                            "emoji": True
                        },
                        "image_url": "https://i.postimg.cc/Jhgrf6VW/ca-explained.png",
                        "alt_text": "image1"
                    }
                    ]
                    
            say(blocks=blocks, text=self.backup)
            
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
                            "text": ":no_entry_sign: *It is totally unusual to modify information directly on a CA* (even if a sales asks you to do it, don't, unless it is necessary)."
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
            say(blocks=blocks, text=self.backup)
            
        @app.action("button-ca3")
        def action_button_ca3(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "The CPOP is an identification number for the advertiser. There are two categories: *Audience extension IO* and *Contractual Account RSX*."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":arrow_right: For the Audience extension, the sales has to go to the Account page (where the Entity Type is \"Advertiser\"), and then populate the Web URL field. The sales needs to go to the IOD page to create a New Integration, clicking on the button located to the top right of the page."
                        }
                    },
                    {
                       "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "Web URL at the Account level",
                            "emoji": True
                        },
                        "image_url": "https://i.postimg.cc/jdQMpC5V/company-weburl-CPOP.png",
                        "alt_text": "image1"
                    },
                    {
                       "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "New Integration button at the IOD level",
                            "emoji": True
                        },
                        "image_url": "https://i.postimg.cc/CM2Dr0YG/RSX-integration-CPOP.png",
                        "alt_text": "image1"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":arrow_right: For the CA RSX, the Website URL field has to be populated. Then click on the RSX Integration button to the top right of the CA page to generate an Integration Status. Besides, the name of the Contractual Account should not surpass 70 characters (otherwise, an error message would appear : \"patnername invalid\")."
                        }
                    },
                    {
                       "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "Website URL",
                            "emoji": True
                        },
                        "image_url": "https://i.postimg.cc/L4QBdfkZ/weburl-CPOP.png",
                        "alt_text": "image1"
                    },
                    {
                       "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "RSX Integration button",
                            "emoji": True
                        },
                        "image_url": "https://i.postimg.cc/CM2Dr0YG/RSX-integration-CPOP.png",
                        "alt_text": "image1"
                    }
                    ]
                    
            say(blocks=blocks, text=self.backup)
            
        @app.action("button-ca4")
        def action_button_ca4(ack, say):
            ack()
            blocks = [
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "When a sales signed an initial IO with contracted agency whereas it was supposed to be Managed only, this case applies. For instance, Casper US has an IO with contracted & managed agency, however signer & payer is Casper US. You have to follow the steps below:"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":one: Confirm if the contracted agency was filled out by mistake and misunderstanding, meaning that it was managing agency only. Sales cannot resign a new initial IO in case there is already one existing without contracted agency, so this will require a merge."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":two: Identify the 2 Contractual Accounts to merge."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":three: On the wrongly created one (with contracted agency), identify Initial IO."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":four: On the initial IO perform the following actions with Salesforce inspector: \n a) Change Record type to Budget IO one \n b) Replace Contractual Account ID with the one of the correct one (without Contracted Agency) \n c) Add Initial IO ID (of the correct Contractual Account) \n d) Remove the Contracted Agency \n e) Click save"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":five: Check if on the correct Contractual Account you have this IO appearing under the \"Budget IO\" section."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":six: From the wrong Contractual Account transfer all the Budget IOs & Amendments by replacing: \n a) Contractual Account with the one from the correct one \n b) Initial IO with the one of the correct Contractual Account \n c) Empty \"Contracted Agency\" \n d) Add \"Managed Agency\" (the one which was in contracted)"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":seven: Add \"[DO NOT USE]\" to the wrong Contractual Account."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":eight: Ask Sales to update GUID in the RMP and fees (if necessary)."
                        }
                    },
                    ]
                    
            say(blocks=blocks, text=self.backup)
            
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
                            "text": ":arrow_right: If a sales needs to change the Contracted Agency of an IO, or to add one, *because he signs a new contract*, he has to create a new Initial IO. Signing it will create a new CA, with the Contracted Agency in the name."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":white_check_mark: Sometimes, it may happen that the IO already has a Contracted Agency, but the related Contractual Account has not. In this case, you have to link the IO with the correct Contractual Account if it exists. Don't forget to ensure that the Contractual Account and the IO are related to the same Initial IO, otherwise make the correction *at the IO level*."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":arrow_right: *If it is the wrong agency (due to a mistake)*, then follow the procedure in order to make the change:"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":one: Uncheck the *IO Signed Box*, then switch the status bar to \"Approved\" if it is not done automatically."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":two: Remove the attached Contractual Account (use Salesforce Inspector to erase the corresponding field)."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":three: The sales can update the needed changes, then he has to *resign the SAME Initial IO*. It would generate a new Contractual Account (It has to be updated in RMP)."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ":four: Then you can move all Budget IOs to the new Contractual Account (simply change the Contractual Account field at the Budget IO level)."
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "If the sales needs to remove an agency from an Initial IO, the same steps have to be followed."
                        }
                    }
                    ]
            say(blocks=blocks, text=self.backup)