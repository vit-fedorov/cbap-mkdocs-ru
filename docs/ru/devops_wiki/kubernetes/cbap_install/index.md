# Развертывание Comindware Business Application Platform в кластере K8s

## Необходимые условия

- Кластер K8s
- Репозиторий для хранения образов контейнеров или container-registry.

## Комплект поставки

- архив образов компонент Платформы cbap-4.6.1864_images.tgz
- архив файлов манифестов для K8s cbap-k8s-manifests.tgz

## Развертывание Comindware Business Application Platform с помощью K8s

### Добавление образов компонент Платформы в репозиторий образов

Распаковать `cbap-4.6.1864-images.tgz` и добавить хранящиеся в нем образы в репозиторий образов.

#### Пример добавления образов в Docker Container Registry

Используя `docker container registry`, образы можно добавить с помощью следующих команд:

```bash
# Add container image to container registry:
docker load < IMAGE-NAME.tar.gz
# List images in registry:
docker images
```

Образy, находящемуся в `container registry`, добавить тег и загрузить в Container Registry.

```bash
docker tag IMAGE-NAME[:TAG] \
	REGISTRY-NAME/REPO-NAME[:TAG]
docker push REGISTRY-NAME/REPO-NAME[:TAG]
```

### Подготовка к развертыванию Платформы

Распакуйте архив `cbap-k8s.tgz` на машине, которая подключена к кластеру K8s.

Архив содержит yaml-конфигурации компонент продукта к кластеру K8s. yaml-конфиги в директориях `deployment`, `service`, `statefulset`.

```bash
cbap-k8s
|-- deployment
|   |-- adapterhost-deployment.yaml
|   |-- apigateway-deployment.yaml
|   |-- init-kafka-deployment.yaml
|   |-- platform-deployment.yaml
|   `-- web-app-deployment.yaml
|-- service
|   |-- adapterhost-service.yaml
|   |-- apigateway-service.yaml
|   |-- elasticsearch-service.yaml
|   |-- ignite-service.yaml
|   |-- kafka-service.yaml
|   |-- platform-service.yaml
|   `-- web-app-loadbalancer.yaml
`-- statefulset
    |-- elasticsearch-statefulset.yaml
    |-- ignite01-statefulset.yaml
    |-- ignite02-statefulset.yaml
    |-- ignite03-statefulset.yaml
    |-- kafka01-statefulset.yaml
    |-- kafka02-statefulset.yaml
    `-- kafka03-statefulset.yaml

```

#### Создать пространство имен для компонент Платформы

Рекомендуется развертывать компоненты Платформы в выделенном пространстве имен. Манифесты k8s предполагают, что в кластере K8s существует пространство имен `cbap`. Создать пространство имен `cbap` можно с помощью команды:

```bash
kubectl create namespace cbap
```

!!! Warning "Внимание"
    Если Платформа будет развернута в пространстве имен отличном от `cbap`, необходимо во всех манифестах заменить значение `cbap` на имя пространства имен.

    Например, если Платформа будет развернута в пространстве имен `MY-NS`, тогда необходимо:

    • во всех манифестах необходимо заменить значение поля `namespace` с `cbap` на `MY-NS`
    • в манифестах `platfrom-deployment`, `ignite01-statefulset`, `ignite02-statefulset`, `ignite03-statefulset` отредактировать значение поля `IGNITE_CLUSTER_IP_FINDER`, заменив `cbap` на `MY-NS`
    • в манифестах `adapterhost-deployment`, `apigateway-deployment`, `kafka01-statefulset`, `kafka02-statefulset`, `kafka03-statefulset` отредактировать значение поля `KAFKA_BOOTSTRAP`, заменив `cbap` на `MY-NS`

#### Развернуть сервисы для компонент Платформы

Развернуть сервисы `adapterhost-service`, `apigateway-service`, `elasticsearch-service`, `ignite-service`, `kafka-service`, `platform-service`, `web-app-loadbalancer`.

```bash
kubectl apply -f adapterhost-service.yaml
kubectl apply -f apigateway-service.yaml
kubectl apply -f elasticsearch-service.yaml
kubectl apply -f ignite-service.yaml
kubectl apply -f kafka-service.yaml
kubectl apply -f platform-service.yaml
kubectl apply -f web-app-loadbalancer.yaml
```

#### Настроить volume provisioning

По-умолчанию в манифестах используется StorageClass `yc-network-ssd`. Если есть необходимость использовать иное решение, нужно отредактировать поле `spec.storageClassName` для всех манифестов типа StatefulSet.

#### Настроить пути к образам компонент Платформы

Для всех манифестов типа Deployment и StatefulSet отредактировать значение поля `spec.containers.image`, указав адрес Container Registry и тег образа.

#### Развертывание кластера брокера сообщений

Развернуть StatefulSet `kafka01-statefulset.yaml` с помощью команды

```bash
kubectl apply -f kafka01-statefulset.yaml
```

Подождать пока под `kafka01-0` перейдет в статус “ContainerCreating” или “Running”.

Развернуть StatefulSet `kafka02-statefulset.yaml` с помощью команды

```bash
kubectl apply -f kafka02-statefulset.yaml
```

Подождать пока под `kafka02-0` перейдет в статус “ContainerCreating” или “Running”.

Развернуть StatefulSet `kafka03-statefulset.yaml` с помощью команды

```bash
kubectl apply -f kafka01-statefulset.yaml
```

Подождать пока под `kafka03-0` перейдет в статус “ContainerCreating” или “Running”.

Развернуть Deployment `init-kafka-deployment.yaml` с помощью команды

```bash
kubectl apply -f init-kafka-deployment.yaml
```

Подождать пока под перейдет в статус “Completed” и удалить Deployment `init-kafka`.

```bash
kubectl delete deployment init-kafka
```

Посмотреть логи любого из подов `kafka01-0`, `kafka02-0`, `kafka03-0` и убедиться, что топики с префиксом `kfk` были созданы.

```bash
kubectl get pod -n cbap
kubectl logs -n cbap kafka01-0-HASHCODE
```

#### Развертывание сервисов Платформы

Развернуть Deployment’ы `adapterhost-deployment.yaml` и `apigateway-deployment.yaml` .

```bash
kubectl apply -f adapterhost-deployment.yaml
kubectl apply -f apigateway-deployment.yaml
```

Убедитесь, что соответствующие сервисам поды перешли в статус “Running”.

#### Развертывание базы данных Платформы

Развернуть StatefulSet’ы `ignite01-statefulset.yaml` `ignite02-statefulset.yaml` `ignite03-statefulset.yaml`.

```bash
kubectl apply -f ignite01-statefulset.yaml
kubectl apply -f ignite02-statefulset.yaml
kubectl apply -f ignite03-statefulset.yaml
```

Убедиться, что поды `ignite01-0`, `ignite02-0`, `ignite03-0` перешли в статус “Running”.

Посмотреть логи любого из подов и убедиться, что кластер состоит из трех нод:

```bash
kubectl logs -n cbap ignite01-0 | grep Topology
```

Пример ответа:

```bash
[09:49:25] Topology snapshot [ver=3, locNode=a5ad8fca, \
servers=3, clients=0, state=INACTIVE, CPUs=12, \
offheap=20.0GB, heap=48.0GB]
```

#### Развертывание и конфигурирование бекенда Платформы

Если используется внешний сервис Elasticsearch, отредактировать поле `spec.template.spec.env.value` для переменной `ELASTICSEARCH_URI` введя URI внешнего сервиса Elasticsearch.

Если необходимо развернуть Elasticsearch в контуре K8s, развернуть StatefulSet `elasticsearch-statefulset.yaml`.

```bash
kubectl apply -f elasticsearch-statefulset.yaml
```

Убедиться, что под `elasticsearch01` перешeл в статус “Running”.

#### Развертывание балансировщика Платформы

Развернуть Deployment `web-app-loadbalancer.yaml`.

```bash
kubectl apply -f web-app-loadbalancer.yaml
```

Убедиться, что соответствующий компоненте под перешел в статус “Running”.

#### Получение доступа к Платформу методом проброса портов

Установить проброс портов с сервиса web-app на локальную машину

```bash
kubectl port-forward service/web-app 30000:8081 -n cbap
```

В браузере отправиться на `localhost:30000`.