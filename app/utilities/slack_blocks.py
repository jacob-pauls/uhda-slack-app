# Jacob Pauls
# Nov 26, 2020
# slack_blocks.py

class SlackBlockTypes:

    def create_ticket_block_builder(self, username, description, title, priority, category):
        CREATE_TICKET_BLOCK =  [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":memo: \t" + username + " Created a Ticket",
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
                    "text": ":rolled_up_newspaper: *Title*: " + title + "\n\n"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":crystal_ball: *Description*: " + description + "\n\n"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": ":signal_strength: *Priority*: " + priority
                    },
                    {
                        "type": "mrkdwn",
                        "text": ":label: *Category*: " + category
                    }
                ]
            }
        ]
        return CREATE_TICKET_BLOCK