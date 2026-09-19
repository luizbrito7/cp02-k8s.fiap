# Checkpoint 01 - Cloud Native FIAP

<p align="center">
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣽⣿⣿⣿⣿⣯⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⢀⣴⣾⣷⣶⣄⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⣠⣶⣾⣷⣦⡀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⢀⠀⠀⡀⠀⠀⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠘⠿⣿⣿⣇⠀⠙⢿⡿⠋⠀⢀⣤⣶⣾⣿⣿⠀⠀⣿⣿⣷⣶⣤⡀⠀⠙⢿⡿⠋⠀⣸⣿⣿⠿⠃⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⠀⣾⣿⣿⣷⣦⠀⠀⠀⢶⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⣴⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠁⠀⣴⣄⠀⠙⠿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⡿⠋⠀⣠⣦⠀⠈⢿⣿⣿⣿⡄⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⣼⣿⣿⣿⠃⠀⣸⣿⣿⣿⣦⡀⠈⠻⢿⣿⠀⠀⣿⣿⠟⠁⢀⣴⣿⣿⣿⣇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⢠⣿⣿⣿⣿⠀⢀⣿⣿⣿⣿⣿⣿⣷⣄⠀⠉⠀⠀⠉⠀⣠⣾⣿⣿⣿⣿⣿⣿⡀⠀⢿⣿⣿⣿⡄⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⣸⣿⣿⣿⡇⠀⢸⣿⣿⣿⡿⠿⠿⠛⠛⠀⠀⠀⠀⠀⠀⠛⠛⠿⠿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣇⠀⠀⠀⠀  <br>
    ⠀⣠⣶⣶⣿⣿⠿⠿⠛⠀⠈⠉⠁⢀⣀⣠⣤⣴⣶⣶⠀⠀⠀⠀⢶⣶⣤⣤⣄⣀⡀⠈⠉⠁⠀⠚⠿⠿⣿⣿⣶⣶⣄⠀  <br>
    ⢸⣿⣿⣿⣿⣄⣠⣤⣤⡄⠀⠸⣿⣿⣿⣿⣿⣿⣿⠃⢀⣾⣷⡀⠈⣿⣿⣿⣿⣿⣿⣿⠇⠀⢠⣤⣤⣀⣠⣿⣿⣿⣿⡇  <br>
    ⠈⠻⣿⣿⡿⢿⣿⣿⣿⣿⡄⠀⠹⣿⣿⣿⣿⣿⠃⢀⣾⣿⣿⣷⡀⠘⣿⣿⣿⣿⣿⠏⠀⢀⣾⣿⣿⣿⡿⢿⣿⣿⠟⠁  <br>
    ⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣄⠀⠈⠻⣿⣿⠃⢀⣾⣿⣿⣿⣿⣷⡀⠘⣿⣿⠟⠁⠀⣠⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣷⣄⠀⠈⠁⠀⢾⣿⣿⣿⣿⣿⣿⡷⠀⠈⠁⠀⣠⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⠂⢀⣀⡀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠐⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠃⠀⣼⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣷⡀⠘⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  <br>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  <br>

</br>

Este repositório contém o **Checkpoint 01** da matéria **Cloud Native Development**.

O objetivo é praticar Pods, Services e depuração de manifestos em Kubernetes, executando os exercícios 3.1 a 3.4 da apostila num cluster local com **kind** e documentando cada passo em PDF.

## Exercícios

| Exercício | Enunciado | Manifestos | Evidência |
| --- | --- | --- | --- |
| 3.1: Manifesto de Pod completo da store-api | [README](./exercises/3.1/README.md) | [Pasta](./exercises/3.1/) | [PDF](./exercises/3.1/03-evidence.pdf) |
| 3.2: Três Services e a prova de DNS | [README](./exercises/3.2/README.md) | [Pasta](./exercises/3.2/) | [PDF](./exercises/3.2/07-evidence.pdf) |
| 3.3: Consertar o manifesto quebrado | [README](./exercises/3.3/README.md) | [Pasta](./exercises/3.3/) | [PDF](./exercises/3.3/04-evidence.pdf) |
| 3.4: Pod multi-container com initContainer, sidecar e emptyDir | [README](./exercises/3.4/README.md) | [Pasta](./exercises/3.4/) | [PDF](./exercises/3.4/04-evidence.pdf) |

## Estrutura

```text
.
├── assets/
│   ├── 00-kind-cluster.yaml   # manifesto do cluster kind
│   ├── 01-setup-cluster.sh    # sobe o cluster e prepara o namespace
│   ├── 02-build-pdf.py        # gera o PDF de evidência a partir do markdown
│   └── 03-style.css           # estilo do PDF
├── exercises/
│   └── 3.x/                   # enunciado, manifestos, prints e PDF de cada exercício
└── material/                  # contexto da entrega e guia visual
```

## Cluster local

Pré-requisitos: `docker`, `kind` e `kubectl`. A imagem `store-api:1.0` precisa existir localmente; o passo a passo do build está na apostila do curso (laboratório 2.11).

```bash
./assets/01-setup-cluster.sh
export KUBECONFIG=$PWD/assets/kubeconfig
kubectl apply -f exercises/3.1/01-pod-store-api.yaml
```

O `kubeconfig` fica isolado em `assets/` (e fora do Git), para nunca misturar com o de outros clusters.
