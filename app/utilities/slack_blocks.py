from config import get_env

# Jacob Pauls
# Nov 26, 2020
# slack_blocks.py

class SlackBlockTypes:

    def create_ticket_block(self, ticket_data):
        CREATE_TICKET_BLOCK =  [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":memo: \t" + ticket_data["username"] + " Created a Ticket",
                    "emoji": True
                }
            },
            { 
                "type": "divider" 
            },
             {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":rolled_up_newspaper: *Title*: " + ticket_data["title"] + "\n\n"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":crystal_ball: *Description*: " + ticket_data["description"] + "\n\n"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": ":signal_strength: *Priority*: " + ticket_data["priority"]
                    },
                    {
                        "type": "mrkdwn",
                        "text": ":label: *Category*: " + ticket_data["category"]
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<"+get_env('EMPLOYEE_VIEW_URL')+"|View>* \n\n"
                }
            }
        ]
        return CREATE_TICKET_BLOCK

    def pickup_ticket_block(self, ticket_data): 
        PICKUP_TICKET_BLOCK = [ 
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":admission_tickets: Your ticket has been picked up:\n",
                    "emoji": True
                }
            },
            { 
                "type": "divider" 
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": ":rolled_up_newspaper: *Ticket*: " + ticket_data["title"]
                    },
                    {
                        "type": "mrkdwn",
                        "text": ":heavy_check_mark: *Picked Up By:* " + ticket_data["username"]
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Thanks for your patience! We're on it!"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<"+get_env('UHDA_URL')+"|Open UHDA>* \n\n"
                }
            }
        ]   
        return PICKUP_TICKET_BLOCK

    def assigned_ticket_block(self, ticket_data):
        ASSIGNED_TICKET_BLOCK =  [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":admission_tickets: Ticket assignment updated:\n",
                    "emoji": True
                }
            },
            { 
                "type": "divider" 
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": ":rolled_up_newspaper: *Ticket*: " + ticket_data["title"]
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": ":heavy_check_mark: *" + ticket_data["username"] + "* has been assigned to your ticket!"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<"+get_env('UHDA_URL')+"|Open UHDA>* \n\n"
                }
            }
        ]
        return ASSIGNED_TICKET_BLOCK

    def field_update_block(self, ticket_data, field):
        FIELD_UPDATE_BLOCK =  [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":admission_tickets: Ticket " + field + " updated:\n",
                        "emoji": True
                    }
                },
                { 
                    "type": "divider" 
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": ":rolled_up_newspaper: *Ticket*: " + ticket_data["title"]
                        }
                    ]
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": ":heavy_check_mark: *" + ticket_data["username"] + "* set the ticket " + field + " to *" + ticket_data[field] + "*"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*<"+get_env('UHDA_URL')+"|Open UHDA>* \n\n"
                    }
                }
            ]
        return FIELD_UPDATE_BLOCK

    def error_ticket_block(self):
        DEFAULT_TICKET_BLOCK = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":four: :zero: :four:",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Uh oh, something weird happened!*"
                }
            }
        ]
        return DEFAULT_TICKET_BLOCK
