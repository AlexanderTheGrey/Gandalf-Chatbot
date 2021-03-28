import json
from random import randint
from pathlib import Path
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionCheckExistence(Action):
    friend_knowledge = Path("data/lotr_friends.txt").read_text().split("\n")
    enemy_knowledge = Path("data/lotr_enemies.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_check_existence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            r = randint(0, 1)

            for blob in tracker.latest_message['entities']:
                name = blob['value'].lower()
                friend_responses = [f"Yes, {name} is my old friend.", f"Ah yes, my old friend {name}."]
                enemy_responses = [f"No, {name} is a wretched soul from the darkest depths of Middle-earth.", f"A disgusting soul {name} is."]
                if name in self.friend_knowledge:
                    dispatcher.utter_message(text=friend_responses[r])
                elif name in self.enemy_knowledge:
                    dispatcher.utter_message(text=enemy_responses[r])
                else:
                    dispatcher.utter_message(text=f"I know not of who you speak.")

            return []