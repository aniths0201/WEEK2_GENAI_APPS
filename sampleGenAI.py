import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["GOOGLE_API_KEY"] = "AIzaSyBJFhn7sUNbU21k50WCExFiA2AJc5R1S_w"
# 1. MODEL I/O: Initialize the Gemini Model
# Make sure you have your environment variable set: export GEMINI_API_KEY="your-api-key"
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash", 
    temperature=0.7
    
)

# 2. PROMPTS: Define the template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert educator. Explain the following topic in a way that a {audience} can easily understand."),
    ("human", "Explain this topic: {topic}")
])

# 4. CHAINS: Chain the components together using LCEL (LangChain Expression Language)
# The pipeline flows: Prompt -> Model -> Output Parser
chain = prompt_template | model | StrOutputParser()

# 5. RUNNING THE CHAIN: Invoke the chain with inputs
if __name__ == "__main__":
    inputs = {
        "audience": "5-year-old",
        "topic": "Generative AI"
    }
    
    print(f"--- Asking Gemini to explain '{inputs['topic']}' to a {inputs['audience']} ---\n")
    
    # Run the chain
    response = chain.invoke(inputs)
    
    print(response)