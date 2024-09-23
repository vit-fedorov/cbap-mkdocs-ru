# Настройка поддержки SSL для репозиториев Helm

```shell
sudo cp yourdomain.com.crt /usr/share/ca-certificates/
```

```shell
sudo update-ca-certificates
```

```shell
sudo mkdir /etc/containerd/certs.d/
```

```shell
cat <<EOF | sudo tee /etc/containerd/certs.d/hosts.toml
server = "https://docker.io"

[host."https://10.9.0.118/v2/docker.io/"]
  capabilities = ["pull", "resolve"]
  ca = "/usr/share/ca-certificates/yourdomain.com.crt"
  override_path = true
EOF
```

```shell
sudo systemctl restart containerd
```
