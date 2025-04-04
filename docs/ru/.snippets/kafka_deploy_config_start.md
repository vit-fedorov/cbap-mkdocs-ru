``` ini
# Роли, в которых должен выступать сервер Kafka
process.roles=broker,controller
# Идентификатор узла
node.id=1
# IP-адрес сервера Kafka
controller.quorum.voters=1@<KafkaIP>:9093
# IP-адрес сервера Kafka
listeners=PLAINTEXT://<KafkaIP>:9092,CONTROLLER://<KafkaIP>:9093
# Имя слушателя для связи между брокерами
inter.broker.listener.name=PLAINTEXT
# Имена слушателей контроллера
controller.listener.names=CONTROLLER
# Карта протоколов безопасности для слушателей
listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL
# Количество сетевых потоков
num.network.threads=3
# Количество потоков ввода-вывода
num.io.threads=8
# Размер буфера отправки сокета
socket.send.buffer.bytes=102400
# Размер буфера приёма сокета
socket.receive.buffer.bytes=102400
# Максимальный размер запроса
socket.request.max.bytes=104857600