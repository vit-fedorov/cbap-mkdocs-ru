---
kbId:
title: Развёртывание кластера Kubernetes на Astra Linux SE 1.7
---

# Развёртывание кластера Kubernetes на Astra Linux SE 1.7

## Введение

## Требования к серверу

## Настройка конфигурации окружения ОС

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Обновите пакеты ОС:

    ``` sh
    sudo apt-get update && sudo apt-get upgrade -y
    ```

3. Откройте для редактирования настройки репозитория:

    ``` sh
    sudo nano /etc/apt/sources.list
    ```

4. Отредактируйте конфигурацию основного, базового и расширенного репозитория:

    ``` sh
    deb https://dl.astralinux.ru/astra/stable/1.7_x86-64/repository-main/     1.7_x86-64 main contrib non-free
    deb https://dl.astralinux.ru/astra/stable/1.7_x86-64/repository-base/     1.7_x86-64 main contrib non-free
    deb https://dl.astralinux.ru/astra/stable/1.7_x86-64/repository-extended/ 1.7_x86-64 main contrib non-free
    ```

5. Установите пакет `debian-archive-keyring`:

    ``` sh
    sudo apt install debian-archive-keyring
    sudo apt update
    ```

6. Добавьте репозиторий **Debian Buster**:

    ``` sh
    echo "deb https://deb.debian.org/debian/               buster         main contrib non-free" | sudo tee -a /etc/apt/sources.list.d/debian.list
    echo "deb https://security.debian.org/debian-security/ buster/updates main contrib non-free" | sudo tee -a /etc/apt/sources.list.d/debian.list
    sudo chmod 644 /etc/apt/sources.list.d/debian.list 
    sudo apt-get update
    ```

7. Установите необходимые пакеты:

    ``` sh
    sudo apt-get install -y apt-transport-https ca-certificates curl gnupg tmux curl
    ```

### Настройка модуля ядра br_netfilter

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Загрузите модуль ядра **GNU/Linux** `br_netfilter`:

    ``` sh
    modprobe br_netfilter
    ```

3. Добавьте модуль к списку загружаемых модулей ядра `/etc/modules-load.d`:

    ```shell
    echo 'br_netfilter' | tee -a /etc/modules-load.d/k8s.conf
    ```

### Настройка трафика мостов

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Чтобы направить трафик с мостов через `iptables`, отредактируйте параметр ядра `bridge-nf-call-iptables`:

    ``` sh
    echo 1 | tee /proc/sys/net/bridge/bridge-nf-call-iptables
    ```

3. Обновите настройки `sysctl`:

    ``` sh
    echo 'net.bridge.ссссссс=1' | tee -a /etc/sysctl.conf
    sysctl -p
    ```

### Настройка проброса кадров IPv4

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Обновите настройки `sysctl`:

    ``` sh
    ```shell
    cat <<EOF | tee /etc/sysctl.d/k8s.conf
    net.ipv4.ip_forward = 1
    EOF
    sysctl --system
    ```

3. Убедитесь, что значение параметра `net.ipv4.ip_forward` равно `1`:

    ```sh
    sysctl net.ipv4.ip_forward
    ```

4. Задайте `<hostName>` для машины:

    ``` sh
    sudo hostnamectl set-hostname <hostName>
    ```

5. Откройте для редактирования файл `/etc/hosts`:

    ``` sh
    nano /etc/hosts
    ```

6. Добавьте записи с данными узлов кластера по следующему образцу:

    ``` sh
    <ipAddress> <hostName>.corp.helloworld.com <hostName>
    ```

## Установка среды выполнения контейнеров containerd

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Установите `containerd`:

    ``` sh
    apt-get install -y containerd
    systemctl enable containerd
    ```

3. Создайте файл конфигурации для `containerd`:

    ``` sh
    mkdir -p /etc/containerd && \
    containerd config default | sudo tee /etc/containerd/config.toml > /dev/null
    ```

4. Откройте для редактирования файл `config.toml`:

    ``` sh
    nano /etc/containerd/config.toml
    ```

5. Отредактируйте директиву `[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]` следующим образом:

    ``` sh
    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
        ...
        [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
            SystemdCgroup = true
    ```

6. Чтобы применить настройки, перезапустите `containerd`:

    ``` sh
    systemctl restart containerd && \
    systemctl enable containerd
    ```

## Установка Kubernetes

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Создайте папку для хранения открытых ключей:

    ``` sh
    mkdir /etc/apt/keyrings
    ```

3. Добавьте ключ репозитория Kubernetes:

    ``` sh
    curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.24/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    ```

4. Настройте права доступа для файла открытого ключа:

    ``` sh
    chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    ```

5. Добавьте репозиторий Kubernetes:

    ``` sh
    echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.24/deb/ /' | tee /etc/apt/sources.list.d/kubernetes.list
    ```

6. Настройте права доступа для файла с адресом репозитория:

    ``` sh
    chmod 644 /etc/apt/sources.list.d/kubernetes.list
    ```

7. Установите пакет `cri-tools`:

    ```shell
    apt-get update && sudo apt-get install -y cri-tools=1.26.0-1.1
    ```

8. Установите компоненты Kubernetes:

    ``` sh
    sudo apt-get install -y kubelet kubeadm kubectl
    ```

9. Отключите автоматическое обновление установленных компонентов:

    ``` sh
    apt-mark hold kubelet kubeadm kubectl
    ```

## Инициализация основного узла кластера

1. Инициализируйте кластер и его основной узел:

    ``` sh
    kubeadm init --pod-network-cidr=<nodeIP>/<netMask>
    ```

    Здесь:

    - `<nodeIP>` — неизменная часть IP-адресов узлов кластера;
    - `<netMask>` — маска подсети.

    Например:

    - `192.168.1.100/32` (маска подсети `255.255.255.255`): один компьютер с IP-адресом `192.168.1.100`.
    - `192.168.1.0/24` (маска подсети `255.255.255.0`): все компьютеры с IP-адресами от `192.168.1.1` до `192.168.1.254`.

2. Настройте доступ для `kubectl` к кластеру:

    ``` sh
    mkdir -p $HOME/.kube
    cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    chown $(id -u):$(id -g) $HOME/.kube/config
    ```

3. Разверните подсеть подов:

    ``` sh
    kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
    ```

4. Убедитесь, что узел `control-plane` находится в состоянии `Ready`:

    ``` sh
    kubectl get nodes
    ```

## Инициализация дополнительных узлов

1. На первом узле создайте токен для включения узла в кластер:

    ``` sh
    kubeadm token create --print-join-command
    ```

2. Выполните токен на новом узле.
3. На первом узле проверьте, что новый узел подключился к кластеру:

    ``` sh
    kubectl get nodes
    ```

## Проверка работоспособности

1. На первом узле запустите развёртывание `mybusybox`:

    ```sh
    kubectl run mybusybox --restart=Never --image=busybox
    ```

2. Убедитесь, что `mybusybox` имеет статус `Completed`:

    ``` sh
    kubectl get pod mybusybox
    ```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
