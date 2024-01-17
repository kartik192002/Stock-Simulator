import socket
from threading import Thread
from taipy.gui import Gui, State, invoke_callback, get_state_id
import pandas as pd
HOST = "127.0.0.1"
PORT = 5050

data = {
    "Date": pd.date_range("2023-01-01", periods=4, freq="D"),
    
    "Min": [222,419.7,662.7,323.5],
    "Max": [28.6,68.2,666.5,173.5]
}



state_id_list = []

def on_init(state: State):
    state_id = get_state_id(state)
    if (state_id := get_state_id(state)) is not None:
        state_id_list.append(state_id)
def client_handler(gui: Gui, state_id_list: list):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, _ = s.accept()
    while True:
        if data := conn.recv(1024):
            print(f"Data received: {data.decode()}")
            if hasattr(gui, "_server") and state_id_list:
                invoke_callback(
                    gui, state_id_list[0], update_received_data, (str(data.decode()),)
                )
        else:
            print("Connection closed")
            break


def update_received_data(state: State, val):
    state.received_data = val
    tempdata = state.Data
    tempdata["Price"][3] =  state.received_data.split(",")[0]
    state.company = state.received_data.split(",")[1]
    state.data= tempdata
 
title = "Stock Simulator By KARTIK"
path = "logo.png"
company = "KT STOCKS"
company_minp = 340
company_maxp = 740

def KT(state):
 print("Hey hello")
 print(state.path)
 print(state.company_minp)

 with open("data.txt","w") as f:
  f.write(f"{state.company},{state.company_minp},{state.company_maxp}")

data = {
    "Date": pd.date_range("2023-01-01", periods=4, freq="D"),
    
    "Price": [222,419.7,662.7,323.5],
    
}

received_data = "No Data"


md = """
<|text-center |
<|{path}|image|>

<|{title}|hover_text=Welcome to stock Screener|>

Name of Stock:<|{company}|input|>

MIN Price: <|{company_minp}|input|>

MAX Price: <|{company_maxp}|input|>

<|Run Simulation|button|on_action=KT|>

<|{title}|hover_text=Your Simulation|>


<|{data}|chart|mode=lines|x=Date||y[1]=Price|line[1]=dash|>


>
"""
gui = Gui(page=md)

t = Thread(
    target=client_handler,
    args=(
        gui,
        state_id_list,
    ),
)
t.start()

gui.run(title="Receiver Page")
