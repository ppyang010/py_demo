from openai_client import OpenAIClient

def main():
    # 配置参数
    api_key = "sk-cgtofovntjmndnfqwtlatchwnajfwbchehbsfgefpgyxolpi"
    base_url = "https://api.siliconflow.cn/v1"  # 可以替换为其他基础URL
    
    # 初始化客户端
    client = OpenAIClient(
        api_key=api_key,
        base_url=base_url
    )
    
    # 准备消息
    messages = [
        {"role": "system", "content": "你是一个有帮助的助手。"},
        {"role": "user", "content": "你是谁"}
    ]
    
    try:
        # 发送请求
        response = client.chat_completion(
            messages=messages,
            model="deepseek-ai/DeepSeek-V3",
            temperature=0.7
        )
        print("助手回复:", response)
        
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main() 