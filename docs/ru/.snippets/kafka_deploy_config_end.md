# Количество разделов (партиций) по умолчанию
num.partitions=4
# Количество потоков восстановления на каталог данных
num.recovery.threads.per.data.dir=1
# Фактор репликации темы смещений
offsets.topic.replication.factor=1
# Фактор репликации журнала состояния транзакций
transaction.state.log.replication.factor=1
# Минимальное количество ISR для журнала состояния транзакций
transaction.state.log.min.isr=1
# Время хранения журналов (в часах)
log.retention.hours=168
# Размер сегмента журнала
log.segment.bytes=1073741824
# Интервал проверки хранения журналов (в миллисекундах)
log.retention.check.interval.ms=300000
# Максимальный размер запроса
max.request.size=104857600
# Максимальный размер сообщения
max.message.bytes=104857600
# Максимальный размер сообщения
message.max.bytes=104857600
# Максимальный размер сообщения для выборки
fetch.message.max.bytes=104857600
# Максимальный размер сообщения для выборки реплики
replica.fetch.max.bytes=104857600
```