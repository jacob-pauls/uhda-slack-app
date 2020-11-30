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

    def default_ticket_block(self):
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
