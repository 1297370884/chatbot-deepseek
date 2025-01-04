document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const responseContent = document.getElementById('response-content');

    function handleLogin(e){
        e.preventDefault(); // 阻止表单默认提交行为
        
        // 获取输入内容
        const content = chatInput.value.trim();
        if (!content) {
            alert("请输入内容");
            return;
        }

        // 清除欢迎消息
        const welcomeMessage = document.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }

        // 显示加载状态
        const loadingMessage = appendAIMessage('正在思考...');

        // 发送请求
        $.ajax({
            url: "/chat",  
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({
                'content': content
            }),
            success: function (response) {
                console.log("成功回调：", response);
                if (response.message === "成功") {
                    // 更新AI回复内容
                    loadingMessage.textContent = response.response; // 假设后端返回的数据中包含response字段
                    
                    // 清空输入框
                    chatInput.value = '';
                    
                    // 滚动到最新消息
                    loadingMessage.scrollIntoView({ behavior: 'smooth' });
                } else {
                    loadingMessage.textContent = response.message || "发送失败";
                    console.error("发送失败，返回数据：", response);
                }
            },
            error: function(xhr, status, error) {
                loadingMessage.textContent = "发送失败，请稍后重试";
                console.error("请求失败：", status, error);
            }
        });
    }

    // 添加AI消息到界面
    function appendAIMessage(content) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'ai-message';
        messageDiv.textContent = content;
        
        responseContent.appendChild(messageDiv);
        return messageDiv;
    }

    // 绑定提交事件
    chatForm.addEventListener('submit', handleLogin);

    // Enter发送消息，Shift+Enter换行
    chatInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleLogin(e);
        }
    });
});