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

print(Fore.GREEN+Style.BRIGHT+"Welcome to the chatbot!!\n")

while True:
  CV=input(Fore.GREEN+Style.BRIGHT+"Give me brief about your CV (Type 'Exit' to close chat): "+Style.RESET_ALL)
  Job_Description=input(Fore.CYAN+Style.BRIGHT+"\nGive me Job Description: \n"+Style.RESET_ALL)

  if CV.lower()=="exit" or Job_Description.lower()=="exit" :
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
                      "content":"""Act as a Hiring Manager. Tell me technological gap using provided CV and Job Description. Give Strengths and Weaknesses"""
                  },
                {
                  "role": "user",
                  "content": f"Job description:{Job_Description}\n\n candidate CV:{CV}"
                }
              ],
              "model": "llama-3.3-70b-versatile",
              "temperature": 1.0
        }
      )
      if response.status_code==200:
        data=response.json()
        print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\nAnswer: ",data["choices"][0]["message"]["content"]+Style.RESET_ALL)
      else:
        print(f"Error: {response.status_code} - {response.text}")
  except Exception as e:
    print(f"Error: {e}")



