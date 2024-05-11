'''
First of all install these things into colab and select T4 runtime

!pip install gpt4all
!apt install libvulkan1
!apt install libnvidia-gl-525-server
'''

from gpt4all import GPT4All

model = GPT4All("mistral-7b-openorca.gguf2.Q4_0.gguf", device='gpu')

tokens = []
prompt = "tell me about some python interview questions?"
with model.chat_session():
    for token in model.generate(prompt, streaming=True, max_tokens=1000, temp=0.7):
        tokens.append(token)
        print(token, end='')