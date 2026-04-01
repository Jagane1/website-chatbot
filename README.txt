WEBSITE CHATBOT ASSESSMENT

Process Followed:

1. Environment Setup
Created Python virtual environment.
Installed required libraries:
openai
requests
beautifulsoup4

2. Website Data Extraction
Used requests library to fetch website content.
Used BeautifulSoup to parse HTML.
Removed script and style elements.
Extracted clean readable text.

3. Data Processing
Cleaned unwanted spaces.
Limited text size to avoid token overflow.
Prepared context for LLM.

4. Chatbot Implementation
Used Groq LLM API (OpenAI compatible).
Provided website text as context.
User interacts through console input.
Bot answers based only on website data.

5. Testing
Tested with questions related to:
Website description
Services
Features
Integrations

Project Structure:

scraper.py → website extraction
processor.py → text cleaning
chatbot.py → chatbot logic
requirements.txt → dependencies
README.txt → documentation

Result:
Successfully created a console chatbot that answers questions based on website content.

IMPORTANT:

Before running the program:

1. Get a free Groq API key from:
https://console.groq.com/

2. Open chatbot.py

3. Replace:
API_KEY="ADD_YOUR_GROQ_API_KEY"

with your actual API key.

4. Run:
python chatbot.py