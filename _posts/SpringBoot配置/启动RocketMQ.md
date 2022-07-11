
cd C:\Users\li\Documents\maven\rocketmq-all-4.5.1-bin-release\bin

start mqnamesrv.cmd

start mqbroker.cmd -n 127.0.0.1:9876 autoCreateTopicEnable=true