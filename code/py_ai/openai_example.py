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
        {"role": "user", "content": "请把一下内容按照重要信息变成表格:"
                                    "<p><span style=\"font-family:宋体;font-size:9.0000pt;\">常考机制有：粘(粘膜损伤、被攻击）、迟(胃排空延迟、贲门失迟缓术后）、清(食管清酸能力下降）、括(食管下段括约肌松弛）。</span></p><figure class=\"image\"><img src=\"https://img1.dxycdn.com/p/s73/2024/0422/962/8849742560754822871.png\" data-width=\"1050\" data-height=\"620\"></figure>"}
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