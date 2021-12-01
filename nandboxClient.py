import configparser
import logging
import time
from threading import Thread, Lock
import json
import websocket
import datetime
import traceback


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
        self.webSocketClient = websocket.WebSocketApp(on_error=self.InternalWebSocket.on_error,
                                                      on_close=self.InternalWebSocket.on_close)

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

            if(close_status_code == 1000 or close_status_code == 1006 or close_status_code == 1001 or close_status_code == close_status_code == 1005) and nandboxClient.closingCounter < nandboxClient.InternalWebSocket.NO_OF_RETRIES_IF_CONN_CLOSED:
                try:
                    logging.info("Please wait 10 seconds for Reconnecting ")
                    time.sleep(10)
                    nandboxClient.closingCounter = nandboxClient.closingCounter + 1
                    logging.info("Conenction Closing counter is  : " + str(nandboxClient.closingCounter))
                except():
                    logging.info(traceback._cause_message)
                    nandboxClient.InternalWebSocket.PingThread.interrupted = True

        @staticmethod
        def __reconnect_websocket_client():
            logging.info("Creating new webSocketClient")

        def __send(self):
            pass

        def stop_websocket_client(self):
            pass

        def on_open(self, ws):
            pass

        @staticmethod
        def on_message(self, ws, message):
            print(message)

        @staticmethod
        def on_error(self, error):
            print(error)

        def get_session(self):
            return self.session
