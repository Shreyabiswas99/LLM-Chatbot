# Building LLM Chatbots Using OpenAI(paid) and Ollama(open-source)
* Inside this project, I have build two chatbots that are very similar but in one OpenAI API key was used which is paid with GPT-4 and in another Ollama which is an open-source LLM software tool is used.
* First of all, I have already generated my secret openai api key and langchain api key by creating an account and stored them in a seperate file. We will call our api keys whenever we require using our os environment.
* Going ahead, a Prompt was created for the system and user and a title was given to out Chatbot
## Setup
* If using VSCode make sure to setup the environment for our model, we can do that by running this command on the terminal : create -p venv python=3.9 -y
* Activate it by using conda activate venv
* Make sure you have latest version of python and VSCode setup
* Lastly install all the required libraries by running pip install -r requirements.txt
## Running 
* Run the LLM model using Streamlit by using streamlit run filename
