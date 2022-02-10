import requests
import settings

def send_message(chat_id,Type,text="",image_path=""):
        
        if Type=="sendMessage":
            url = "https://api.telegram.org/bot" + settings.token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
            results = requests.post(url)
        if Type=="sendDocument":
            url = "https://api.telegram.org/bot" + settings.token + "/sendDocument" + "?chat_id=" + chat_id +"&caption=" + text
            image_file = open(image_path,"rb")
            results = requests.post(url, files={"document": image_file})


