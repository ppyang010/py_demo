import openai
from typing import Optional, Dict, Any

class OpenAIClient:
    def __init__(
        self, 
        api_key: str,
        base_url: Optional[str] = None,
        organization: Optional[str] = None
    ):
        """
        初始化OpenAI客户端
        
        Args:
            api_key: OpenAI API密钥
            base_url: 可选的自定义基础URL
            organization: 可选的组织ID
        """
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url,
            organization=organization
        )

    def chat_completion(
        self,
        messages: list,
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        **kwargs: Dict[str, Any]
    ) -> str:
        """
        发送聊天完成请求
        
        Args:
            messages: 消息列表
            model: 模型名称
            temperature: 温度参数
            **kwargs: 其他可选参数
        
        Returns:
            助手的回复文本
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"OpenAI API调用失败: {str(e)}") 