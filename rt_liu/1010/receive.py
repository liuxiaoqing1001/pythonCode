from kafka import KafkaConsumer

isoftConsumer = KafkaConsumer('spider', bootstrap_servers=['liu-1:9092'])
for msg in isoftConsumer:
    recv = "主题:%s,分区%d,数量:%d,分类:%s,爬取内容:%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)

# 先在虚拟机中开启zookeeper
# zookeeper.sh start
# 开启kafka
# ./kafka-server-start.sh
