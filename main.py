from pypresence import Presence
import time
import tailer
import sys
from pathlib import Path

client_id = '699335298567634954'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

RPC.update(large_image="stk", state="SuperTuxKart", details="Main menu", start=time.time(), large_text="SuperTuxKart RPC script by undevdecatos!")

# TODO: detect the log path according to os

for line in tailer.follow(open(str(Path.home()) + '/.config/supertuxkart/config-0.10/stdout.log', encoding='UTF8')):
    if '[info   ] ProtocolManager: A 12GameProtocol protocol has been started.' in line:
        RPC.update(large_image="stk", small_image="online", state="SuperTuxKart", details="In an online match", start=time.time())
    elif '[info   ] ProtocolManager: A 12GameProtocol protocol has been terminated.' in line:
        RPC.update(large_image="stk", small_image="online", state="SuperTuxKart", details="Waiting in an online lobby", start=time.time())
    elif '[info   ] ProtocolManager: A 11ClientLobby protocol has been terminated.' in line:
        RPC.update(large_image="stk", state="SuperTuxKart", details="Main menu", start=time.time())
    elif '[info   ] ProtocolManager: A 11ClientLobby protocol has been started.' in line:
        RPC.update(large_image="stk", small_image="online", state="SuperTuxKart", details="Waiting in an online lobby", start=time.time())
    elif '[info   ] Singleton: Destroyed singleton.' in line:
        break;
