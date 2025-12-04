import requests

AUTH_TOKEN = "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"

url = "https://api.groq.com/openai/v1/chat/completions"
headers={
  "Content-Type": "application/json",
  "Authorization": f"Bearer {AUTH_TOKEN}"
}

print("Welcome to the chatbot!!")

while True:
  user_input=input("Hello how can i help you!!")

  if user_input.lower()=="exit":
    print("Have a nice day!!")
    break      
  try:
      response=requests.post(
        url=url,
        headers=headers,
        json={
              "messages": [
                  {
                      "role": "system",
                      "content": "You are a professional Data scientist"
                  },
                  {
                      "role":"system",
                      "content":"Give answers only in 5 line."
                  },
                {
                  "role": "user",
                  "content": user_input
                }
              ],
              "model": "llama-3.3-70b-versatile",
              "temperature": 1.0
        }
      )
      if response.status_code==200:
        data=response.json()
        print("Answer: ",data["choices"][0]["message"]["content"])
      else:
        print(f"Error: {response.status_code} - {response.text}")
  except Exception as e:
    print(f"Error: {e}")



