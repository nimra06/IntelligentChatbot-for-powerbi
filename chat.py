import openai
import config

openai.api_key = config.OPENAI_API_KEY

def chatbot(input):
    if input:
        messages=[
            {"role":"system","content":"You are an ai specialize in powerbi.Do not answer any questions outside of powerbi."},
            {"role":"user","content":input}
        ]
        
        chat=openai.ChatCompletion.create(
            model="gpt-3.0-turbo",
            messages=messages
        )
        response=chat.choices[0].message.content
        return response
