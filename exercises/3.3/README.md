#### Exercício 3.3 — Consertar o manifesto quebrado (análise/depuração) · 40 min

- **Objetivo:** localizar e corrigir cinco defeitos distintos em manifestos, classificando cada um por tipo de erro.
- **Enunciado:** Salve os dois manifestos abaixo como `quebrado.yaml`. Eles contêm **cinco defeitos**. Para cada um, você deve identificar: (1) a linha; (2) o tipo do defeito (sintaxe YAML / API inválida / valor incoerente com outro objeto / valor incoerente com a aplicação); (3) a mensagem de erro ou o sintoma que ele produz; (4) o comando que revela o problema; (5) a correção.

  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: store-api
    namespace: store-dev
    labels:
      app: store-api
       tier: backend
      env: dev
  spec:
    containers:
      - name: store-api
        image: store-api:1.0
        ports:
          - name: http
            containerPort: 8000
        livenessprobe:
          httpGet:
            path: /health
            port: 8000
  ---
  apiVersion: extensions/v1beta1
  kind: Service
  metadata:
    name: store-api
    namespace: store-dev
  spec:
    type: ClusterIP
    selector:
      app: store-api
      env: prod
    ports:
      - port: 80
        targetPort: 9000
  ```

  Trabalhe de forma **incremental**: corrija um defeito, tente aplicar, leia a nova mensagem de erro, corrija o próximo. Documente essa progressão — a sequência de mensagens de erro é parte do entregável, porque ela mostra a ordem em que o Kubernetes valida as coisas (parser YAML → esquema da API → admission → runtime → conectividade). Ao final, entregue `corrigido.yaml` funcionando, com o Service devolvendo um endpoint e um `curl` bem-sucedido a partir de um Pod cliente. **Pergunta de fechamento (obrigatória, 5 linhas):** dois dos cinco defeitos **não** geram nenhum erro no `kubectl apply` — o objeto é criado com sucesso e o problema só aparece em tempo de execução. Quais são, e o que isso ensina sobre confiar no `apply` como validação?
- **Entregável:** `ex3-3.md` com a tabela dos 5 defeitos (colunas: linha, tipo, sintoma, comando revelador, correção), a progressão das mensagens de erro, e o arquivo `corrigido.yaml`.
- **Critério de aceite:** os cinco defeitos identificados são: (i) indentação de `tier: backend` desalinhada; (ii) `livenessprobe` em minúsculas (campo desconhecido); (iii) `apiVersion: extensions/v1beta1` para um Service (deve ser `v1`); (iv) selector com `env: prod` divergente do label `env: dev` do Pod (Endpoints vazio, **sem erro no apply**); (v) `targetPort: 9000` sem processo escutando (timeout, **sem erro no apply**). A resposta de fechamento identifica corretamente (iv) e (v).
- <details><summary>Dica</summary>Aplique com <code>kubectl apply --dry-run=server -f quebrado.yaml</code> para pegar (i), (ii) e (iii) sem sujar o cluster. Para (iv) e (v), o único caminho é <code>kubectl get endpoints</code> e um <code>curl</code> de dentro do cluster — nenhuma validação estática pega esses dois.</details>
