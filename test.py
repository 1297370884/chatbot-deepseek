import json

from openai import OpenAI

class DeepSeek:
    def __init__(self):
        self.chat_history = []

    def core(self, role="user", content=None):
        if content is None:
            return "没有输入问题，请重新提问"

        client = OpenAI(api_key="sk-edc20c136a9a4622b0e5a628a102c84e", base_url="https://api.deepseek.com")
        messages = {
            "role": role,
            "content": content
        }
        self.chat_history.append(messages)

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=self.chat_history,
            timeout=30
        )

        chat_response = response.choices[0].message.content

        self.chat_history.append(response.choices[0].message)
        return chat_response

    def get_chat_history(self):
        # 返回聊天记录的JSON格式
        return self.chat_history

if __name__ == "__main__":
    chat = DeepSeek()
    response = chat.core(content="你好呀")
    print(response)
    response = chat.core(content="你是谁呀")
    print(response)
    chat_history = chat.get_chat_history()
    print(chat_history)







