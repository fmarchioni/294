## 🔎 Come utilizzare lo script `search_facts.py`

Lo script `search_facts.py` consente di cercare **chiavi o valori** all'interno di un file JSON contenente i facts raccolti da Ansible (tipicamente l'output del modulo `setup`).

### 📥 Esecuzione base

```bash
python3 search_facts.py facts.json <termine_da_cercare>
```

- `<termine_da_cercare>` può essere:
  - una **chiave** (es. `ipv4`, `network`)
  - oppure un **valore** contenuto nei facts (es. `eth0`, `lo`)

---

### 🧪 Esempi d'uso

#### ✅ Cerca tutte le chiavi o valori corrispondenti a `network`:

```bash
$ python3 search_facts.py facts.json network
🔍 Found 3 match(es) for 'network':

ansible_facts['default_ipv4']['network']
ansible_facts['eth0']['ipv4']['network']
ansible_facts['lo']['ipv4']['network']
```

#### ✅ Cerca la chiave o valore `ipv4`:

```bash
$ python3 search_facts.py facts.json ipv4
🔍 Found 2 match(es) for 'ipv4':

ansible_facts['eth0']['ipv4']
ansible_facts['lo']['ipv4']
```

---

### ℹ️ Suggerimenti

- Il file `facts.json` può essere generato con:
  ```bash
  ansible -m setup <host> -o --tree ./output/
  ```
  oppure
  ```bash
  ansible -m setup <host> --out facts.json
  ```

- Il percorso restituito dallo script è già nel formato compatibile con Ansible Jinja2, utile per usarlo direttamente in playbook o template.
