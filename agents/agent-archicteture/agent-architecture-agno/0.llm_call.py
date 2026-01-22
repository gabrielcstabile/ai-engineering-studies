from agno.models.groq import Groq
from agno.models.message import Message
from dotenv import load_dotenv

load_dotenv()

model = Groq()

user_msg = Message(
    role="user",
    content=[{"type": "text", "text": "Olá, mundo!"}]
)

assistant_msg = Message(
    role="assistant",
    content=[]
)

response = model.invoke(
    messages=[user_msg],
    assistant_message=assistant_msg
)

print(response)
