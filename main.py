import tkinter
import requests

window= tkinter.Tk()
window.title("GUI Program")
window.minsize(width=600, height=600)





my_lable= tkinter.Label (text="The Great Kanye...says", font=("arial", 14, "bold"))
my_lable.pack()

response= requests.get("https://api.kanye.rest")
response.raise_for_status()


data= response.json()
finaltweet=data["quote"]
print(finaltweet)



Kanye_qoutes= tkinter.Label(text=finaltweet)
Kanye_qoutes.pack()




tkinter.mainloop()

