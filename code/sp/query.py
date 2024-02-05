from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform

def get_chrome_driver_path():
    system_name = platform.system()
    if system_name == 'Windows':
        return 'chromedriver.exe'  # 根据实际路径进行设置
    elif system_name == 'Darwin':  # macOS
        return './chromedriver_mac_arm64/chromedriver'  # 根据实际路径进行设置
    elif system_name == 'Linux':
        return '/usr/local/bin/chromedriver'  # 根据实际路径进行设置
    else:
        raise Exception(f'Unsupported operating system: {system_name}')


def setup_chrome_driver():
    # 获取Chrome驱动程序路径
    chrome_driver_path = get_chrome_driver_path()

    # 创建ChromeOptions对象
    chrome_options = Options()
    chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
    chrome_options.add_argument('--headless')

    # 创建Chrome WebDriver实例并传入ChromeOptions和驱动程序路径
    driver = webdriver.Chrome(options=chrome_options)

    return driver

if __name__ == "__main__":
    # 使用Chrome WebDriver
    driver = setup_chrome_driver()
    driver.get("http://www.baidu.com")
    print("网页标题:", driver.title)
    driver.quit()
