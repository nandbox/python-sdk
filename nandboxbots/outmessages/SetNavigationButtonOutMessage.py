import json

from nandboxbots.outmessages.OutMessage import OutMessage


class SetNavigationButtonOutMessage(OutMessage):
    __KEY_NAVIGATION_BUTTONS = "navigation_button"
    __KEY_NAV_TYPE = "nav_type"
    __KEY_MENU_OPEN = "menu_open"

    navigation_button = ""
    nav_type = None
    menu_open = None

    def __init__(self):
        self.method = "setNavigationButton"

    def to_json_obj(self):
        _, dictionary = super(SetNavigationButtonOutMessage, self).to_json_obj()

        if self.navigation_button is not None:
            dictionary[self.__KEY_NAVIGATION_BUTTONS] = self.navigation_button
        if self.nav_type is not None :
            dictionary[self.__KEY_NAV_TYPE] = self.nav_type
        if self.menu_open is not None :
            dictionary[self.__KEY_MENU_OPEN] = self.menu_open

        return json.dumps(dictionary), dictionary
    
