import configparser
import logging
import time
from threading import Thread, Lock
import json
import websocket
import datetime
import traceback

import nandbox
from outmessages.TextOutMessage import TextOutMessage
from util import Utils


def send(message):
    message_obj = message.to_json_object()
    logging.info()


class nandboxClient:
    CONFIG_FILE = 'config.properties'
    BOT_ID = None
    nandboxClient = None
    webSocketClient = None

    closingCounter = 0
    timeOutCounter = 0
    connRefusedCounter = 0

    _uri = None
    KEY_METHOD = "method"
    KEY_ERROR = "error"

    config = configparser.ConfigParser()

    def __init__(self, uri):
        self._uri = uri

    def init(self):
        Lock.acquire()

        if self.nandboxClient is not None:
            return

        self.nandboxClient = self.__init__()

        Lock.release()

    def get(self):
        if self.nandboxClient is None:
            self.init()

        return self.nandboxClient

    def connect(self):
        self.InternalWebSocket.__init__()
        self.webSocketClient = websocket.WebSocketApp(self._uri, on_error=self.InternalWebSocket.on_error,
                                                      on_close=self.InternalWebSocket.on_close,
                                                      on_message=self.InternalWebSocket.on_message(),
                                                      on_open=self.InternalWebSocket.on_open())

    def get_uri(self):
        return self._uri

    def set_uri(self, uri):
        self._uri = uri

    def set_logger(self):
        pass

    class InternalWebSocket:
        NO_OF_RETRIES_IF_CONN_TO_SERVER_REFUSED = 20
        NO_OF_RETRIES_IF_CONN_TIMEDOUT = 10
        NO_OF_RETRIES_IF_CONN_CLOSED = 20
        KEY_USER = "user"
        KEY_CHAT = "chat"
        KEY_NAME = "name"
        KEY_ID = "ID"

        callback = None
        session = None
        token = None
        api = None

        authenticated = False
        echo = False
        lastMessage = 0

        class PingThread(Thread):
            interrupted = False

            def run(self):
                while True:
                    try:
                        obj = {
                            nandboxClient.KEY_METHOD: "PING"
                        }

                        nandboxClient.InternalWebSocket.send(obj.dumps())
                    except():
                        logging.exception()

                    if self.interrupted:
                        return

                    try:
                        time.sleep(
                            3)  # this blocks the thread no the process: https://stackoverflow.com/questions/92928/time-sleep-sleeps-thread-or-process
                    except():
                        self.interrupted = True
                        return

        pingThread = None

        def __int__(self, token, callback):
            self.token = token
            self.callback = callback

        @staticmethod
        def __on_close(close_status_code, close_msg):
            logging.info("INTERNAL: ONCLOSE")
            logging.info("StatusCode = " + str(close_status_code))
            logging.info("Reason : " + str(close_msg))

            now = datetime.now()
            dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
            logging.info("Date = " + dt_string)

            nandboxClient.InternalWebSocket.authenticated = False

            if nandboxClient.InternalWebSocket.pingThread is not None:
                nandboxClient.InternalWebSocket.PingThread.interrupted = True

            nandboxClient.InternalWebSocket.pingThread = None

            nandboxClient.InternalWebSocket.callback.onClose()

            if (
                    close_status_code == 1000 or close_status_code == 1006 or close_status_code == 1001 or close_status_code == close_status_code == 1005) and nandboxClient.closingCounter < nandboxClient.InternalWebSocket.NO_OF_RETRIES_IF_CONN_CLOSED:
                try:
                    logging.info("Please wait 10 seconds for Reconnecting ")
                    time.sleep(10)
                    nandboxClient.closingCounter = nandboxClient.closingCounter + 1
                    logging.info("Conenction Closing counter is  : " + str(nandboxClient.closingCounter))
                except():
                    logging.info(traceback._cause_message)
                    nandboxClient.InternalWebSocket.PingThread.interrupted = True

                nandboxClient.InternalWebSocket.__stop_websocket_client()

                try:
                    nandboxClient.InternalWebSocket.__reconnect_websocket_client()

                except():
                    logging.info(traceback._cause_message)
                    nandboxClient.InternalWebSocket.PingThread.interrupted = True

        @staticmethod
        def __stop_websocket_client():
            logging.info("Stopping Websocket client");

            try:
                nandboxClient.InternalWebSocket.get_session()
            except():
                logging.info("Exception while closing the websocket session")
                logging.info(traceback._cause_message)

            try:
                if nandboxClient.webSocketClient is not None:
                    nandboxClient.webSocketClient.close()
                    nandboxClient.webSocketClient = None
                    logging.info("Websocket client stopped Successfully")
            except():
                logging.error("Exception while stopping websocket client")
                logging.erro(traceback._cause_message)

        @staticmethod
        def __reconnect_websocket_client():
            logging.info("Creating new web socket client")

            # TODO: Should I instantiate the websocket client here?

            logging.info("web socket client started")
            logging.info("Getting nandbox client instance")

            n_client = nandboxClient.get()

            logging.info("Calling nandbox client connect")
            n_client.connect(nandboxClient.InternalWebSocket.token, nandboxClient.InternalWebSocket.callback)

        def __send(self):
            pass

        def on_open(self, ws):

            logging.info("INTERNAL: ONCONNECT")

            auth_object = {
                "method": "TOKEN_AUTH",
                "token": self.token,
                "rem": True
            }

            class ApiImplementation(nandbox.nandbox.Api):
                def send(self, message):

                    message_obj = message.to_json_object()

                    now = datetime.now()
                    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")

                    logging.info(dt_string + ">>>>>> Sending Message :" + message_obj)
                    nandboxClient.InternalWebSocket.send(message_obj)  # TODO convert to string?

                def prepare_out_message(self, message, chat_id, reference, reply_to_message_id, to_user_id,
                                        web_page_preview, disable_notification, caption, chat_settings):
                    message.chat_id = chat_id
                    message.reference = reference

                    if to_user_id is not None:
                        message.to_user_id = to_user_id
                    if reply_to_message_id is not None:
                        message.reply_to_message_id = reply_to_message_id
                    if web_page_preview is not None:
                        message.web_page_preview = web_page_preview
                    if disable_notification is not None:
                        message.disable_notification = disable_notification
                    if caption is not None:
                        message.caption = caption
                    if chat_settings is not None:
                        message.chat_settings = chat_settings

                def send_text(self, chat_id, text):
                    reference = Utils.get_unique_id()
                    self.send_text(chat_id, text, reference)

                def send_text_with_background(self, chat_id, text, bg_color):
                    reference = Utils.get_unique_id()
                    self.send_text(chat_id, text, reference, None, None, None, None, None, bg_color)

                def send_text(self, chat_id, text, reference):
                    self.send_text(chat_id, text, reference, None, None, None, None, None, None)

                def send_text(self,  chat_id, text, reference, reply_to_message_id, to_user_id, web_page_preview, disable_notification, chat_settings, bg_color):
                    message = TextOutMessage()

                    self.prepare_out_message(message=message, chat_id=chat_id, reference=reference, reply_to_message_id=reply_to_message_id, to_user_id=to_user_id, web_page_preview=web_page_preview, disable_notification=disable_notification, caption=None, chat_settings=chat_settings)

                    message.method = "sendMessage"
                    message.text = text
                    message.bg_color = bg_color

                    self.send(message)

        @staticmethod
        def on_message(self, ws, message):
            print(message)

        @staticmethod
        def on_error(self, error):
            logging.error("INTERNAL: ONERROR")
            logging.error(error)

        def get_session(self):
            return self.session
