import openai

openai.api_key = "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"  # Replace with your actual OpenAI API key

response = openai.Completion.create(
    model="gpt-3.5-turbo",  
    prompt="What is GitHub?",  
    max_tokens=100  
)

print(response.choices[0].text.strip()) 
