# 🪄 Variabili Magiche in Template Jinja2 per Ansible

Questo file elenca tutte le **variabili magiche** utilizzabili all’interno dei template Jinja2 in Ansible, **senza che tu debba definirle manualmente**.

---

## 🔁 Variabili Magiche del Loop (`loop.`)

Queste sono disponibili **solo dentro un ciclo** `{% for ... %}`:

| Variabile           | Descrizione |
|---------------------|-------------|
| `loop.index`        | Indice del ciclo (partendo da 1) |
| `loop.index0`       | Indice del ciclo (partendo da 0) |
| `loop.revindex`     | Indice inverso (da N a 1) |
| `loop.revindex0`    | Indice inverso (da N-1 a 0) |
| `loop.first`        | `true` se è il primo elemento |
| `loop.last`         | `true` se è l’ultimo elemento |
| `loop.length`       | Numero totale di elementi nella lista |
| `loop.cycle(...)`   | Cicla valori: `loop.cycle('odd', 'even')` |
| `loop.depth`        | Profondità del ciclo (se annidato) |
| `loop.depth0`       | Come sopra, ma partendo da 0 |
| `loop.parent`       | Riferimento al ciclo esterno (se annidato) |

---

## 🌍 Variabili Magiche Globali in Template Jinja2 (Ansible)

Queste sono disponibili in **qualsiasi punto del template**:

| Variabile                  | Descrizione |
|----------------------------|-------------|
| `ansible_managed`          | Frase di gestione automatica (commento) |
| `inventory_hostname`       | Nome dell'host nel file inventario |
| `inventory_hostname_short` | Nome corto (senza dominio) |
| `ansible_hostname`         | Hostname remoto (dai facts) |
| `ansible_fqdn`             | Nome FQDN completo dell'host |
| `ansible_playbook_python`  | Percorso al binario Python in uso |
| `ansible_version`          | Informazioni sulla versione di Ansible |
| `ansible_check_mode`       | `true` se il playbook è in modalità check |
| `hostvars`                 | Variabili disponibili per tutti gli host |
| `groups`                   | Mappa dei gruppi dell'inventario |
| `group_names`              | Elenco dei gruppi di cui fa parte l’host |
| `play_hosts`               | Lista di host nel play corrente |
| `playbook_dir`             | Directory dove si trova il playbook |
| `role_name`                | Nome del ruolo corrente (se applicabile) |
| `role_path`                | Percorso assoluto del ruolo corrente |

---

## Esempio di uso:

```jinja2
# {{ ansible_managed }}
Host: {{ inventory_hostname }}
IP: {{ ansible_default_ipv4.address }}

{% for user in users if user != 'root' %}
- Utente {{ loop.index }}: {{ user }}
{% endfor %}
```

---

 
