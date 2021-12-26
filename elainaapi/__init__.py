import requests

def chatbot(msg, token, timeout=10):
    data = {"key": token,
            "msg": msg,}
    try:
      r = requests.get('https://api.elainateam.xyz/chatbot', params=data, timeout=timeout)
      r  = r.json()
      msg = r["msg"]
      if int(r["code"]) == 200:
        return msg
      if int(r["code"]) == 403:
        print("Key không hợp lệ")
        return None
      if int(r["code"]) == 404:
        return msg
    except:
      print("Lỗi")
      return "Lỗi"
