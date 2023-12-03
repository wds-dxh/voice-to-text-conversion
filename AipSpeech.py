import time
from threading import Thread

from aip import AipSpeech
import QT
import Read_voice


""" 你的 APPID AK SK """
APP_ID = '43993838'
API_KEY = 'h1rvZsv5hm8UrRKhAyUiyjE3'
SECRET_KEY = 'K8UZLTec6xu9zqlHOQdEHhWysQLOcZ8z'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)#创建一个客户端用以访问百度云
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_result():
    result  = client.asr(get_file_content('音频.wav'), 'pcm', 16000, {
        'dev_pid': 1537,
    })
    # print(result['result'][0])  #[0]的意思是只输出第一个结果，如果不加[0]，输出的结果是一个列表，列表中的元素是每个可能的结果
    return result['result'][0]

# global text
# text = ''
def thread_readvoice():
    global text
    while True:
        if Read_voice.get_audio('音频.wav') == 0:
            continue
        text = get_result()
        print(text)


def update_display():
        QT.display_text_window(get_result, font_size=20, timer_interval=5000)  #timer_interval：显示时间
        # print("update_display"+text)
            # time.sleep(0.1)  # 更新显示后稍作延时，避免过于频繁更新


if __name__ == '__main__':
    my_thread = Thread(target=thread_readvoice, daemon=True)
    my_thread.start()
    #
    # display_thread = Thread(target=update_display, daemon=True)
    # display_thread.start()
    QT.display_text_window(get_result, font_size=20, timer_interval=5000)

    while True:
        pass  # 主循环保持运行，可以在此处添加其他需要同时进行的逻辑

