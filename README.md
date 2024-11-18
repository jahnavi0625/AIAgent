# AIAgent
# Overview
This project includes creating an AI agent that reads through a dataset(CSV)
and performs a web search to retrieve specific information for each entity in a 
chosen column.The AI will leverage an LLM to parse web results based on the user's query
and format the extracted data in a structured output.The project includes building a simple dashboard where 
users can upload a file,define search queries,and download the results.

# setup Instructions
Make sure you install python and visual studio code to write code 
and the packaged required are pandas,streamlit,requests and openai
Make sure to install them using the command
"pip install pandas openai requests streamlit" on your command prompt for Windows"
load the app.py file attached over here
In visual studio code,You are supposed to open the terminal and locate to the directory where the app.py is available and
in terminal in Visual Studio Code you could run the code using the command
'streamlit run app.py'
here app.py is the file name and make sure you have internet connection for this to work out smoothly as the project uses ChatGPT and Microsoft Bing Integrations which are cloud based..
# Third party APIs 
ChatGPT(OpenAI) API integration for parsing results and Microsoft Bing for performing search
# How to get ChatGPT OpenAI API Key
To get a ChatGPT API key from OpenAI, follow these steps:
1) Sign Up for an Account: Go to the OpenAI platform at platform.openai.com and sign up using your email address or an existing Google, Microsoft, or Apple account.
2) Verify Your Email: After signing up, verify your email address to activate your account.
3) Access API Keys: Once your account is active, log in and navigate to the API keys page. You can find this by clicking on your profile icon and selecting "API keys."
4) Create a New API Key: Click on the "Create new secret key" button. You can give your key a name to help identify it later.
5) Copy and Save Your API Key: A unique alphanumeric key will be generated. Copy this key and save it somewhere secure1. Do not share your API key with anyone to keep your account secure.
6) Use the API Key: You can now use this API key in your applications to access OpenAI's services, such as ChatGPT

# How to get Microsoft Bing API Key
To get a Microsoft Bing API key, follow these steps:
1) Sign Up for an Azure Account: If you don't already have one, you'll need to create a Microsoft Azure account. You can sign up for a free trial if you don't want to commit to a paid subscription right away.
2) Navigate to the Azure Portal: Once you have an Azure account, log in to the Azure Portal.
3) Search for Bing Services: In the search box, type "Bing" and select the Bing service you're interested in (e.g., Bing Search or Bing Custom Search).
4) Create a Resource: Click on "Create a resource" and follow the prompts to set up your Bing service. You'll need to provide a name for your resource and select a subscription (you can use the free trial if you're eligible
5) Retrieve Your API Key: After creating the resource, navigate to the "Keys and Endpoint" section. Here, you'll find your API key. Copy this key and keep it secure.
6) Use the API Key: You can now use this API key in your applications to access Bing's search services.

use chatgpt key as OPEN_API_KEY
Microsoft bing key as SEARCH_API_KEY
# Video : Working of the Project
https://drive.google.com/file/d/18M9HuX87M86IS_oimMastV5bcTrmoG1U/view?usp=drivesdk
