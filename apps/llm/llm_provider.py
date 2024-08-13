import ollama

client = ollama.Client(host='https://d335-34-16-195-102.ngrok-free.app')

class ChatLLM:
    def __init__(self, model='llama3.1'):
        self.model = model

    def get_title(self, prompt, response):
        response = client.chat(model=self.model, messages=[
            {
                'role': 'user',
                'content': f'return a 2 to 4 words title for this user prompt:{prompt} and ai response: {response}. You must '
                           f'return only title and no other text like here is the title or The title is etc. just the Title.',
            },
        ])
        return response['message']['content']

    def get_response(self, prompt):
        response = client.chat(model=self.model, messages=[
          {
            'role': 'user',
            'content': f'{prompt}',
          },
        ])
        return response['message']['content']