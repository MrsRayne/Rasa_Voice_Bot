# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os, aiohttp, asyncio, json, socket, binascii

#TCP_IP = '127.0.0.1'
#TCP_PORT = 60600
#BUFFER_SIZE = 1024
#rasa_url = 'http://localhost:5005/webhooks/rest/webhook'

class ActionGreet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
        return []

class ActionHappy(Action):
    def name(self):
        return 'action_happy'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_happy")
        return []


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
