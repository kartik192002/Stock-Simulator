from taipy import Gui
import pandas as pd

data = {
    "Date": pd.date_range("2023-01-01", periods=4, freq="D"),
    
    "Min": [222,419.7,662.7,323.5],
    "Max": [28.6,68.2,666.5,173.5]
}




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

page ="""
<|text-center |
<|{path}|image|>

<|{title}|hover_text=Welcome to stock Screener|>

Name of Stock:<|{company}|input|>

MIN Price: <|{company_minp}|input|>

MAX Price: <|{company_maxp}|input|>

<|Run Simulation|button|on_action=KT|>

<|{title}|hover_text=Your Simulation|>


<|{data}|chart|mode=lines|x=Date||y[1]=Min|y[2]=Max|line[1]=dash|color[2]=blue|>





>
"""
if __name__=="__main__":
 app = Gui(page) 
 app.run(use_reloader=True)
