class DeepSeek:
    def __init__(self):
        self.chat_history = []

    def core(self, role, content):
        messages = {
            "role": role,
            "content": content
        }
        self.chat_history.append(messages)
        chat_response = "hello"

        return chat_response

    def history(self):
        return self.chat_history


if __name__ == "__main__":
    a = DeepSeek()
    response = a.core("lpl", "你好")
    print(response)
    now_store = a.history()
    print(now_store)
    response = a.core("cxk", "只因你太美")
    print(response)
    now_store = a.history()
    print(now_store)

