import openai
import config

OPENAI_COMPLETION_OPTIONS = {
    "temperature": 0.7,
    "max_tokens": 1000,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
}

openai.api_key = config.openai_api_key

def generate_prompt_messages(question):
    assistant_prompt = "As an advanced chatbot named ChatGPT, your primary goal is to assist users to the best of your ability. This may involve answering questions, providing helpful information, or completing tasks based on user input. In order to effectively assist users, it is important to be detailed and thorough in your responses. Use examples and evidence to support your points and justify your recommendations or solutions. Remember to always prioritize the needs and satisfaction of the user. Your ultimate goal is to provide a helpful and enjoyable experience for the user."
    messages = [{"role": "system", "content": assistant_prompt}]

    messages.append({"role": "user", "content": question})
    return messages

def get_answer_from_chatgpt(question_prompt):
    messages = generate_prompt_messages(question_prompt)
    answer = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=messages,
              **OPENAI_COMPLETION_OPTIONS
        )
        
    return answer.choices[0].message["content"]