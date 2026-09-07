from groq import Groq
import base64
import os
from dotenv import load_dotenv

load_dotenv()

def detect_violation(img_path):
  with open(rf'{img_path}', 'rb') as f:
      image_base64 = base64.b64encode(f.read()).decode('utf-8')
  image_base64
  client =Groq(api_key=os.getenv("api_key"))
  response = client.chat.completions.create(
      model="qwen/qwen3.6-27b",
      messages=[
        {
          "role": "user",
          "content":[{'type':'text','text':"""tell me which traffice violation is the given image 
          is breaking :no helmet,overspeeding,no parking,triple seat.tell among this only.dont explain
          anything.just tell the name of violation"""},
          {'type':'image_url','image_url':{'url':f'data:image/jpeg;base64,{image_base64}'
              }
          }
              ]
        }
      ],
      
      reasoning_effort="none"
      
  )
  return(response.choices[0].message.content)

