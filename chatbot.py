

from openai import OpenAI
from scraper import extract_website_text
from processor import clean_text


"""
Website Chatbot Assessment Solution
Author: Jagadeesh
"""


API_KEY="ADD_YOUR_GROQ_API_KEY"

url="https://botpenguin.com"


client=OpenAI(

    api_key=API_KEY,

    base_url="https://api.groq.com/openai/v1"
)


print("Loading website...")

website_data=extract_website_text(url)

processed_data=clean_text(website_data)

print("Website data loaded successfully")

print("Website Chatbot Ready (type exit to quit)")


while True:

    question=input("You: ")

    if question.lower()=="exit":

        break

    if question.strip()=="":
        continue

    prompt=f"""
Website data:
{processed_data}

Question:
{question}

Answer only from website data.
"""

    response=client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {"role":"user","content":prompt}
        ],

        max_tokens=150
    )

    print("Bot:",response.choices[0].message.content)