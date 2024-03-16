from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendMovie(Action):
    def name(self) -> Text:
        return "action_recommend_movie"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Logique pour recommander un film en fonction des préférences de l'utilisateur
        dispatcher.utter_message("Great! I'll find a movie for you.")

        return []

class ActionAskGenre(Action):
    def name(self) -> Text:
        return "action_ask_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Sure, I can help you find a movie. What genre are you in the mood for? You can say something like 'I want a comedy.'")

        return []
    

class ActionThankYou(Action):
    def name(self) -> Text:
        return "action_thank_you"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("You're welcome! Feel free to ask if you need more help.")
        return []

class ActionBotPresent(Action):
    def name(self) -> Text:
        return "action_bot_present"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Yes, I'm here to assist you!")
        return []