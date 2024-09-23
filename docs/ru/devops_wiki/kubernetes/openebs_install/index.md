# Установка OpenEBS в контуре Kubernetes

```shell
kubectl apply -f https://openebs.github.io/charts/openebs-operator.yaml
```

```shell
kubectl get pods -n openebs
```

List the storage classes to check if OpenEBS has been installed with default StorageClasses.

```shell
kubectl get sc
```
