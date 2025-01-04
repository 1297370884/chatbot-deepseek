import openai
from robyn import Request, Response, status_codes, jsonify

from createchat import chat

from settings import render_template

"""
视图层 应该专注于 处理请求 并 返回响应
"""

async def index_view(request):
    return render_template("chat.html",request=request)


async def chat_view(request: Request):

    message = request.json()
    content = message.get("content")
    try:
        chat_response = chat.core(content=content)
    except openai.APIConnectionError as e:
        return {"error": "连接服务器失败，请检查网络设置或稍后重试"}
    except Exception as e:
        return {"error": f"发生错误: {str(e)}"}
    return Response(
        status_code=status_codes.HTTP_200_OK,
        headers={"Content-Type": "application/json"},
        description=jsonify({"content": chat_response})
    )









