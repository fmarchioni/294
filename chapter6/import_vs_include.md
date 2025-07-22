# Differenza tra `import_tasks` e `include_tasks` con `when`

## 🔹 `import_tasks` – Inclusione **statica**

* I task nel file importato possono essere **qualsiasi tipo di task** (installazioni, moduli, ruoli, ecc.).
* I task vengono **caricati al momento del parsing**, cioè **prima dell’esecuzione** vera e propria → quindi **non puoi usare variabili dinamiche** (es. registrate in task precedenti).
* Se usi `when:` sull’`import_tasks`, la condizione si applica **a tutti i task importati**, ma **non puoi basarla su risultati precedenti**.

### Esempio di import errato:

```yaml
- name: Salva risultato
  command: whoami
  register: user_output

- name: Import non valido con variabile registrata
  import_tasks: some_tasks.yml
  when: user_output.stdout == "root"   # ❌ Errore
```

---

## 🔹 `include_tasks` – Inclusione **dinamica**

* ✅ Anche qui puoi includere **qualsiasi task valido**.
* ✅ Viene valutato **al momento dell'esecuzione**, quindi puoi usare **variabili dinamiche e registrate**.
* ✅ `when:` sull’`include_tasks` determina **se il blocco viene caricato oppure no**.
* ✅ I singoli task inclusi possono avere le loro `when:`.

### ✅ Esempio valido:

```yaml
- name: Salva risultato
  command: whoami
  register: user_output

- name: Include solo se è root
  include_tasks: some_tasks.yml
  when: user_output.stdout == "root"
```

---

## 🔒 Cosa **non puoi** fare

| Operazione                                               | import\_tasks | include\_tasks             |
| -------------------------------------------------------- | ------------- | -------------------------- |
| Usare variabili registrate nel `when`                    | ❌ No          | ✅ Sì                       |
| Usare `loop:` direttamente sull’include                  | ❌ No          | ✅ Sì (con `include_tasks`) |
| Usare `tags:`                                            | ✅ Sì          | ✅ Sì                       |
| Includere lo stesso file più volte con parametri diversi | ❌ No          | ✅ Sì                       |

---

# Condizionali con import ed include:


## 📁 File di esempio: `tasks/mytasks.yml`

```yaml
- name: Task A
  debug:
    msg: "Eseguo Task A"

- name: Task B
  debug:
    msg: "Eseguo Task B"
```

---

## Caso 1 – `import_tasks` con `when`

```yaml
- name: Import con condizione
  hosts: localhost
  vars:
    esegui_tasks: false
  tasks:
    - name: Importa i task solo se esegui_tasks è true
      ansible.builtin.import_tasks: tasks/mytasks.yml
      when: esegui_tasks
```

### Comportamento

- I **task vengono caricati sempre** durante il parse time.
- La condizione `when: esegui_tasks` si applica **a tutti i task importati**.
- Se `esegui_tasks: false`, **i task non vengono eseguiti**, ma sono comunque presenti nella struttura del playbook.

---

## Caso 2 – `include_tasks` con `when`

```yaml
- name: Include con condizione
  hosts: localhost
  vars:
    esegui_tasks: false
  tasks:
    - name: Includi i task solo se esegui_tasks è true
      ansible.builtin.include_tasks: tasks/mytasks.yml
      when: esegui_tasks
```

### 🔍 Comportamento

- La condizione `when: esegui_tasks` viene valutata **solo sull'`include_tasks`**.
- Se la condizione è `false`, **il file `mytasks.yml` non viene nemmeno incluso**.
- È come se il blocco non esistesse affatto.

---

## Riassunto

| Comando           | File letto? | Task caricati? | Task eseguiti?              |
|------------------|-------------|----------------|-----------------------------|
| `import_tasks`   | ✅ Sì        | ✅ Sì           | ❌ Solo se `when` è `true`   |
| `include_tasks`  | ❌ No (se `when: false`) | ❌ No | ❌ Nessun task incluso       |




 
