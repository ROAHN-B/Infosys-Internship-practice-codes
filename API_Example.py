import requests
import os
from dotenv import load_dotenv
from colorama import Fore, Style,init

load_dotenv()

API_KEY= os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"
headers={
  "Content-Type": "application/json",
  "Authorization": f"Bearer {API_KEY}"
}

print(Fore.GREEN+Style.BRIGHT+"Welcome to the chatbot!!")

while True:
  CV=input("Give me brief about your CV: ")
  Job_Description=input(Fore.CYAN+Style.BRIGHT+"Give me Job Description: ")

  if CV.lower()=="exit" or Job_Description=="exit" :
    print("Have a nice day!!")
    break    

  try:
      response=requests.post(
        url=url,
        headers=headers,
        json={
              "messages": [
                  {
                      "role":"system",
                      "content":"""Act as a Hiring Manager."""
                  },
                {
                  "role": "user",
                  "content": Job_Description,
                  "content": CV
                }
              ],
              "model": "llama-3.3-70b-versatile",
              "temperature": 1.0
        }
      )
      if response.status_code==200:
        data=response.json()
        print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"Answer: ",data["choices"][0]["message"]["content"])
      else:
        print(f"Error: {response.status_code} - {response.text}")
  except Exception as e:
    print(f"Error: {e}")



