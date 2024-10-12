import urllib.parse
import sys

def url_decode(encoded_url):
    """
    解码浏览器 URL 中的编码字符。

    :param encoded_url: 编码后的 URL 字符串
    :return: 解码后的 URL 字符串
    """
    try:
        decoded_url = urllib.parse.unquote(encoded_url)
        return decoded_url
    except Exception as e:
        return f"解码失败: {e}"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    # 示例编码的 URL
    encoded_url = "xml_content=%3Cxml%3E%3Cname%3EMazda+rx7-FD%3C%2Fname%3E%3C%2Fxml%3E"
    
    # 解码 URL
    decoded_url = url_decode(encoded_url)
    
    # 输出解码后的 URL
    print("解码后的 URL:", decoded_url)