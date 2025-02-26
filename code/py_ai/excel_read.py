import pandas as pd
from openai_client import OpenAIClient


def get_chat_completion(api_key, base_url, message_content, model="deepseek-ai/DeepSeek-V3", temperature=0.7):
    """
    发送消息到OpenAI客户端并获取回复。

    参数:
    api_key (str): OpenAI API密钥。
    base_url (str): OpenAI API的基础URL。
    message_content (str): 用户的消息内容。
    model (str): 使用的模型名称，默认为"deepseek-ai/DeepSeek-V3"。
    temperature (float): 温度参数，默认为0.7。

    返回:
    str: 助手的回复。
    """
    try:
        # 初始化客户端
        client = OpenAIClient(
            api_key=api_key,
            base_url=base_url
        )

        # 准备消息
        messages = [
            {"role": "system", "content": "你是一个有帮助的助手。"},
            {"role": "user", "content": message_content}
        ]

        # 发送请求
        response = client.chat_completion(
            messages=messages,
            model=model,
            temperature=temperature
        )
        return response
    except Exception as e:
        return f"发生错误: {str(e)}"


def main():

    # 配置参数
    api_key = "sk-cgtofovntjmndnfqwtlatchwnajfwbchehbsfgefpgyxolpi"
    base_url = "https://api.siliconflow.cn/v1"  # 可以替换为其他基础URL
    # 定义Excel文件路径
    file_path = './query_result_20250226205744.xlsx'

    # 使用pd.ExcelFile读取Excel文件
    excel_file = pd.ExcelFile(file_path)

    # 打印所有工作表名称
    print("工作表名称:", excel_file.sheet_names)

    # 选择特定工作表进行读取（例如第一个工作表）
    # 跳过第一行：在读取时指定 skiprows=1 参数，以跳过第一行。
    df = pd.read_excel(excel_file, sheet_name=excel_file.sheet_names[0], skiprows=1)

    # 打印 DataFrame 的基本信息
    print("DataFrame 形状:", df.shape)
    print("DataFrame 前几行数据:")
    print(df.head())

    # 打印第二列的值
    second_column_name = df.columns[1]  # 获取第二列的列名

    print(f"\n第二列 '{second_column_name}' 的值:")
    for index, value in df[second_column_name].head(2).iteritems():
        print(f"行 {index + 1}")
        # print(f"行 {index + 1}: {value}")
        # 准备消息内容
        message_content = "请把一下内容按照重要信息变成表格:"+value
        # 获取助手回复
        response = get_chat_completion(api_key, base_url, message_content)
        print("助手回复:", response)




if __name__ == "__main__":
    main()




