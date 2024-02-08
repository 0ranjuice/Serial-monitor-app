import logging
import time
import random

# 設置logger
logging.basicConfig(filename=r'C:\Users\Hank\Downloads\serial_monitor/random_numbers.log', level=logging.INFO,
                    format='%(asctime)s:%(message)s')


def generate_random_number():
    """生成一個隨機的8位數並記錄到日誌文件中"""
    while True:
        random_number = random.randint(10000000, 99999999)  # 生成一個隨機的8位數
        logging.info(random_number)  # 將隨機數記錄到日誌中
        time.sleep(1)  # 每秒生成一次


# 啟動生成隨機數的過程
generate_random_number()
