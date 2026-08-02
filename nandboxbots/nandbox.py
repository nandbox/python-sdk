class Nandbox:
    class Callback:
        def on_connect(self, api):
            pass

        def on_receive(self, incoming_msg):
            pass

        def on_receive_obj(self, obj):
            pass
        def on_product_detail(self,obj):
            pass
        def on_close(self):
            pass

        def on_error(self):
            pass

        def on_chat_menu_callback(self, chat_menu_callback):
            pass

        def on_inline_message_callback(self, inline_msg_callback):
            pass

        def on_message_ack_callback(self, msg_ack):
            pass

        def on_user_joined_bot(self, user):
            pass

        def on_chat_member(self, chat_member):
            pass

        def on_chat_administrators(self, chat_administrators):
            pass

        def user_started_bot(self, user):
            pass

        def on_my_profile(self, user):
            pass

        def on_user_details(self, user,app_id):
            pass

        def user_stopped_bot(self, user):
            pass

        def user_left_bot(self, user):
            pass

        def permanent_url(self, url):
            pass

        def on_chat_details(self, chat,app_id):
            pass

        def on_inline_search(self, inline_search):
            pass
        def on_black_list_pattern(self, black_list_pattern):
            pass
        def on_white_list_pattern(self, white_list_pattern):
            pass

        def on_black_list(self, black_list):
            pass

        def on_white_list(self, white_list):
            pass
        def on_remove_white_list(self,white_list):
            pass
        def on_remove_black_list(self,black_list):
            pass

        def on_schedule_message(self, incoming_schedule_msg):
            pass

        def on_workflow_details(self, workflow_details):
            pass

        def on_create_chat(self, chat):
            pass
        def on_collection_product(self,collectionProduct):
            pass
        def on_collection_item(self,collectionItem,app_id):
            pass
        def on_document_response(self, document_response):
            pass
        def on_payment_authorization_request(self,payment_request):
            pass

        def on_menu_callback(self, menu_callback):
            """Called when a user submits a menu form.

            menu_callback is a MenuCallback carrying the submitted cells; use
            Utils.get_fields_and_values(menu_callback.cells) for a flat mapping.
            """
            pass

        def on_webhook_event(self, webhook_event):
            """Called for an inbound WebhookEvent.

            webhook_event is a WebhookBody exposing ref, app_id, method and body.
            """
            pass

        def on_event_response(self, event_response):
            """Reply to subscribe_to_event, unsubscribe_from_event or list_event_subscriptions.

            event_response is an EventResponse; check ack before assuming the subscription
            changed.
            """
            pass

        def on_event_message(self, event_message):
            """Called for a change on an event this account is subscribed to.

            event_message is an EventMessage whose body is the raw payload; its keys vary by
            event and by the server side filter, so read defensively.
            """
            pass

    class Api:
        def send(self, message):
            pass
        def list_collection_item(self,app_id,reference):
            pass
        def get_collection_product(self,collection_id,app_id,reference):
            pass
        def get_product_detail(self, product_id,app_id,reference):
            pass
        def send_text_with_background(self, chat_id, text, bg_color,tags,app_id):
            pass

        def send_text(self, chat_id, text, reference, reply_to_message_id=None, to_user_id=None, web_page_preview=None,
                      disable_notification=None, chat_settings=None, bg_color=None, tab=None,tags=None,app_id=None):
            pass

        def send_photo(self, chat_id, photo_file_id, reference, reply_to_message_id=None, to_user_id=None,
                       web_page_preview=None,
                       disable_notification=None, caption=None, chat_settings=None, tab=None,tags=None,app_id=None):
            pass

        def send_video(self, chat_id, video_file_id, reference, reply_to_message_id=None, to_user_id=None,
                       web_page_preview=None,
                       disable_notification=None, caption=None, chat_settings=None, tab=None,tags=None,app_id=None):
            pass

        def send_audio(self, chat_id, audio_file_id, reference, reply_to_message_id=None, to_user_id=None,
                       web_page_preview=None,
                       disable_notification=None, caption=None, performer=None, title=None, chat_settings=None,
                       tab=None,tags=None,app_id=None):
            pass

        def send_contact(self, chat_id, phone_number, name, reference, reply_to_message_id=None, to_user_id=None,
                         web_page_preview=None, disable_notification=None, chat_settings=None, tab=None,tags=None,app_id=None):
            pass

        def send_voice(self, chat_id, voice_file_id, reference, reply_to_message_id=None, to_user_id=None,
                       web_page_preview=None,
                       disable_notification=None, caption=None, size=None, chat_settings=None, tab=None,tags=None,app_id=None):
            pass

        def send_document(self, chat_id, document_file_id, reference, reply_to_message_id=None, to_user_id=None,
                          web_page_preview=None,
                          disable_notification=None, caption=None, name=None, size=None, chat_settings=None, tab=None,tags=None,app_id=None):
            pass

        def send_location(self, chat_id, latitude, longitude, reference, reply_to_message_id=None, to_user_id=None,
                          web_page_preview=None, disable_notification=None, name=None, details=None, chat_settings=None,
                          tab=None,tags=None,app_id=None):
            pass

        def send_gif(self, chat_id, gif_file_id, reference, reply_to_message_id=None, to_user_id=None,
                     web_page_preview=None,
                     disable_notification=None, caption=None, chat_settings=None, tab=None,tags=None,app_id=None):
            pass

        def send_gif_video(self, chat_id, gif_file_id, reference, reply_to_message_id=None, to_user_id=None,
                           web_page_preview=None,
                           disable_notification=None, caption=None, chat_settings=None, tab=None,tags=None,app_id=None):
            pass

        def update_message(self, message_id, text=None, caption=None, to_user_id=None, chat_id=None,app_id=None):
            pass

        def update_text_msg(self, message_id, text, to_user_id, app_id):
            pass

        def update_media_caption(self, message_id, caption, to_user_id, app_id):
            pass

        def update_chat_msg(self, message_id, text, chat_id,app_id):
            pass

        def update_chat_media_caption(self, message_id, caption, chat_id, app_id):
            pass

        def get_user(self, user_id,app_id,reference):
            pass

        def get_chat(self, chat_id,app_id,reference):
            pass

        def get_chat_member(self, chat_id, user_id,app_id,reference):
            pass

        def get_chat_administrators(self, chat_id,app_id,reference):
            pass

        def ban_chat_member(self, chat_id, user_id,app_id,reference):
            pass

        def unban_chat_member(self, chat_id, user_id,app_id,reference):
            pass

        def remove_chat_member(self, chat_id, user_id,app_id,reference):
            pass

        def recall_message(self, chat_id, message_id, to_user_id, reference,app_id):
            pass

        def set_my_profile(self, user,reference):
            pass

        def set_chat(self, chat,app_id,reference):
            pass

        def get_my_profiles(self,reference):
            pass

        def generate_permanent_url(self, file, param1):
            pass

        def get_black_list(self,app_id,reference):
            pass

        def get_white_list(self,app_id,reference):
            pass

        def add_black_list(self, users,app_id,reference):
            pass

        def add_white_list(self,  users,app_id,reference):
            pass

        def delete_black_list(self, users,app_id,reference):
            pass

        def delete_white_list(self,  users,app_id,reference):
            pass

        def add_black_list_patterns(self, chat_id, data,app_id):
            pass

        def add_white_list_patterns(self, chat_id, data,app_id,reference):
            pass

        def delete_black_list_patterns(self, chat_id, pattern,app_id,reference):
            pass

        def delete_white_list_patterns(self, chat_id, pattern,app_id,reference):
            pass

        def update_menu_cell(self, user_id, menu_id, app_id, cells, reference, disable_notification):
            pass

        def set_workflow_action(self, user_id, vapp_id, screen_id, next_screen, reference,app_id):
            pass

        def create_chat(self, chat_type, title, is_public, reference,app_id):
            pass

        def add_chat_member(self, chat_id, user_id,app_id):
            pass

        def add_chat_admin_member(self, chat_id, user_id,app_id):
            pass
        def submit_payment_result(self,chat_id,user_id,order_id,provider_response,secret,currency,total_amount,app_id,status,debit_amount_cents):
            pass

        def send_notification(self, user_id, notification_type, title, message, app_id=None):
            pass
