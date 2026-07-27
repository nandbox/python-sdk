# import json
#
#
# class Button:
#     __KEY_BUTTON_SPAN = "button_span"
#     __KEY_BUTTON_ORDER = "button_order"
#     __KEY_BUTTON_TEXT_COLOR = "button_textcolor"
#     __KEY_BUTTON_BG_COLOR = "button_bgcolor"
#     __KEY_BUTTON_CALLBACK = "button_callback"
#     __KEY_BUTTON_LABEL = "button_label"
#     __KEY_BUTTON_URL = "button_url"
#     __KEY_BUTTON_QUERY = "button_query"
#     __KEY_NEXT_MENU = "next_menu"
#     __KEY_CHAT = "chat"
#     __KEY_BUTTON_ICON = "button_icon"
#     __KEY_BUTTON_ICON_BG_COLOR = "button_icon_bgcolor"
#     __BUTTON_QUERY_LOCATION = "location"
#     __BUTTON_QUERY_CONTACT = "contact"
#     __KEY_BUTTON_NAV_TYPE = "nav_type"
#
#     button_span = None
#     button_order = None
#     button_textcolor = None
#     button_bgcolor = None
#     button_callback = None
#     button_label = None
#     button_url = None
#     button_query = None
#     next_menu = None
#     chat = None
#     button_icon = None
#     button_icon_bgcolor = None
#     location = None
#     contact = None
#     nav_type = None
#
#     def __init__(self, dictionary):
#         self.button_order = int(dictionary[self.__KEY_BUTTON_ORDER]) if dictionary.get(self.__KEY_BUTTON_ORDER) is not None else None
#         self.button_span = int(dictionary[self.__KEY_BUTTON_SPAN]) if dictionary.get(self.__KEY_BUTTON_SPAN) is not None else None
#         self.button_textcolor = str(dictionary[self.__KEY_BUTTON_TEXT_COLOR]) if dictionary.get(self.__KEY_BUTTON_TEXT_COLOR) is not None else None
#         self.button_bgcolor = str(dictionary[self.__KEY_BUTTON_BG_COLOR]) if dictionary.get(self.__KEY_BUTTON_BG_COLOR) is not None else None
#         self.button_callback = str(dictionary[self.__KEY_BUTTON_CALLBACK]) if dictionary.get(self.__KEY_BUTTON_CALLBACK) is not None else None
#         self.button_label = str(dictionary[self.__KEY_BUTTON_LABEL]) if dictionary.get(self.__KEY_BUTTON_LABEL) is not None else None
#         self.button_url = str(dictionary[self.__KEY_BUTTON_URL]) if dictionary.get(self.__KEY_BUTTON_URL) is not None else None
#         self.button_query = str(dictionary[self.__KEY_BUTTON_QUERY]) if dictionary.get(self.__KEY_BUTTON_QUERY) is not None else None
#         self.next_menu = str(dictionary[self.__KEY_NEXT_MENU]) if dictionary.get(self.__KEY_NEXT_MENU) is not None else None
#         self.chat = str(dictionary[self.__KEY_CHAT]) if dictionary.get(self.__KEY_CHAT) is not None else None
#         self.button_icon = str(dictionary[self.__KEY_BUTTON_ICON]) if dictionary.get(self.__KEY_BUTTON_ICON) is not None else None
#         self.button_icon_bgcolor = str(dictionary[self.__KEY_BUTTON_ICON_BG_COLOR]) if dictionary.get(self.__KEY_BUTTON_ICON_BG_COLOR) is not None else None
#         self.nav_type = str(dictionary[self.__KEY_BUTTON_NAV_TYPE]) if dictionary.get(self.__KEY_BUTTON_NAV_TYPE) is not None else None
#
#     def to_json_obj(self):
#
#         dictionary = {}
#
#         if self.button_order is not None:
#             dictionary[self.__KEY_BUTTON_ORDER] = self.button_order
#         if self.button_span is not None:
#             dictionary[self.__KEY_BUTTON_SPAN] = self.button_span
#         if self.button_label is not None:
#             dictionary[self.__KEY_BUTTON_LABEL] = self.button_label
#         if self.button_callback is not None:
#             dictionary[self.__KEY_BUTTON_CALLBACK] = self.button_callback
#         if self.button_url is not None:
#             dictionary[self.__KEY_BUTTON_URL] = self.button_url
#         if self.button_bgcolor is not None:
#             dictionary[self.__KEY_BUTTON_BG_COLOR] = self.button_bgcolor
#         if self.button_textcolor is not None:
#             dictionary[self.__KEY_BUTTON_TEXT_COLOR] = self.button_textcolor
#         if self.button_icon is not None:
#             dictionary[self.__KEY_BUTTON_ICON] = self.button_icon
#         if self.button_icon_bgcolor is not None:
#             dictionary[self.__KEY_BUTTON_ICON_BG_COLOR] = self.button_icon_bgcolor
#         if self.button_query is not None:
#             dictionary[self.__KEY_BUTTON_QUERY] = self.button_query
#         if self.next_menu is not None:
#             dictionary[self.__KEY_NEXT_MENU] = self.next_menu
#         if self.chat is not None:
#             dictionary[self.__KEY_CHAT] = self.chat
#         if self.nav_type is not None:
#             dictionary[self.__KEY_BUTTON_NAV_TYPE] = self.nav_type
#
#         return json.dumps(dictionary), dictionary
