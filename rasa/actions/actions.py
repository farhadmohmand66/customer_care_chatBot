from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType, AllSlotsReset
from rasa_sdk.types import DomainDict
from rasa_sdk import Action

class ActionCheckStatus(Action):
    def name(self) -> Text:
        return "action_check_order_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        if name:
            dispatcher.utter_message(
                response="utter_order_status", name=name)
        else:
            dispatcher.utter_message(text=f"Sorry, not found your answer.")
        return []

class CancelOrderAction(Action):
    def name(self) -> Text:
        return "action_cancel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_cancel")
        return [AllSlotsReset()]


class ActionContactSupport(Action):
    def name(self) -> Text:
        return "action_contact_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_contact_support")
        return []

class ActionBusinessHours(Action):
    def name(self) -> Text:
        return "action_business_hours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_business_hours")
        return []


class ActionReturnPolicy(Action):
    def name(self) -> Text:
        return "action_return_policy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_return_policy")
        return []

class ActionResetPassword(Action):
    def name(self) -> Text:
        return "action_reset_password"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_reset_password")
        return []


class ActionPaymentMethods(Action):
    def name(self) -> Text:
        return "action_payment_methods"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_payment_methods")
        return []


class ActionInternationalShipping(Action):
    def name(self) -> Text:
        return "action_international_shipping"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_international_shipping")
        return []


class ActionProductRecommendations(Action):
    def name(self) -> Text:
        return "action_product_recommendations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_product_recommendations")
        return []


class ActionPricingPolicy(Action):
    def name(self) -> Text:
        return "action_pricing_policy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_pricing_policy")
        return []


class ActionCompanyInfo(Action):
    def name(self) -> Text:
        return "action_company_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_company_info")
        return []


class ActionDiscountsPromotions(Action):
    def name(self) -> Text:
        return "action_discounts_promotions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_discounts_promotions")
        return []


class ActionHelpSpecificProblem(Action):
    def name(self) -> Text:
        return "action_help_specific_problem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_help_specific_problem")
        return []


class ActionProductBenefits(Action):
    def name(self) -> Text:
        return "action_product_benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_product_benefits")
        return []

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_default_fallback")
        return []
