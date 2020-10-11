import threading
import time
from kafka import KafkaProducer


def jdSpider():
    # 在虚拟机/app/kafka/config/server.properties
    # listeners=PLAINTEXT://9092
    jdProducer = KafkaProducer(bootstrap_servers='liu-1:9092')
    while True:
        # send(topic:主题,给后台发送的消息,拿到的数据,partition:放到哪个分区)
        jdProducer.send("spider", bytes("iphone", encoding="utf8"), bytes("phone", encoding="utf8"), partition=0)
        print("京东爬虫")
        time.sleep(1)
    jdProducer.close()


def tbSpider():
    tbSpider = KafkaProducer(bootstrap_servers='liu-1:9092')
    while True:
        tbSpider.send("spider", bytes("羽绒服", encoding="utf8"), bytes("服装", encoding="utf8"), partition=0)
        print("淘宝爬虫")
        time.sleep(2)
    tbSpider.close()


def pddSpider():
    pdd = KafkaProducer(bootstrap_servers='liu-1:9092')
    while True:
        pdd.send("spider", bytes("面膜", encoding="utf8"), bytes("化妆", encoding="utf8"), partition=0)
        print("拼多多爬虫")
        time.sleep(3)
    pdd.close()


t1 = threading.Thread(target=jdSpider)
t2 = threading.Thread(target=tbSpider)
t3 = threading.Thread(target=pddSpider)

t1.start()
t2.start()
t3.start()

# 开启
