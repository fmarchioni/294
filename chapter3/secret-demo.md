### 🏁 Obiettivo della Demo

Nascondere una password segreta (`"PippoPlutoPaperino!"`) dentro un file cifrato e farla leggere ad Ansible durante l'esecuzione.

---

### FASE 1: Prepariamo le "Chiavi di Casa"

1. Crea un file contenente la password che userai per cifrare/decifrare:
```bash
echo "la_mia_password_segreta" > .vault_pass

```


*(Nota: In produzione questo file non va MAI committato su Git! Aggiungilo al `.gitignore`)*.

---

### FASE 2: Creiamo il file Cifrato 

Ora usiamo `ansible-vault` per creare un file di variabili cifrato, usando la password appena creata.

1. Lancia il comando di creazione:
```bash
ansible-vault create secrets.yml --vault-password-file .vault_pass

```


2. Ti si aprirà l'editor (vi/nano). Scrivi dentro questo contenuto:
```yaml
db_password: "PippoPlutoPaperino!"
api_key: "XYZ-999-000"

```


3. Salva ed esci (`Esc` + `:wq` su vi, o `Ctrl+O`, `Invio`, `Ctrl+X` su nano).
4. **La Prova:** Prova a leggere il file con `cat`.
```bash
cat secrets.yml

```


*Risultato:* Vedrai solo spazzatura cifrata (`$ANSIBLE_VAULT;1.1;AES256...`). Il segreto è al sicuro.

---

### FASE 3: Il Playbook (L'Utilizzatore)

Creiamo un playbook che usa queste variabili. Ansible le decifrerà "al volo" in memoria.

File: `demo_vault.yml`

```yaml
---
- name: Demo Ansible Vault
  hosts: localhost
  connection: local
  gather_facts: false

  # IMPORTANTE: Carichiamo il file cifrato
  vars_files:
    - secrets.yml

  tasks:
    - name: 1. Dimostrazione (Non farlo in prod!)
      debug:
        msg: 
          - "Sto accedendo al database..."
          - "La password decifrata è: {{ db_password }}"
          - "La API Key è: {{ api_key }}"

```

---

### FASE 4: L'Esecuzione

Ora lanciamo il playbook. Dobbiamo dire a `ansible-navigator` dove trovare la chiave per aprire il file.

```bash
ansible-navigator run demo_vault.yml --mode stdout --vault-password-file .vault_pass

```

**Cosa succede:**

1. Ansible legge `demo_vault.yml`.
2. Trova `vars_files: secrets.yml`.
3. Vede che `secrets.yml` è cifrato.
4. Usa la password contenuta in `.vault_pass` per decifrarlo.
5. Stampa le variabili in chiaro nel log.

---

### 🔧 Comandi Utili per la gestione (Cheat Sheet)

Se devi modificare il file cifrato in futuro, non puoi usare `nano` o `vim` direttamente (romperesti il file). Devi usare i comandi vault:

* **Modificare il file (Edit):** Apre, decifra temporaneamente, ti fa modificare, e ricifra quando salvi.
```bash
ansible-vault edit secrets.yml --vault-password-file .vault_pass

```


* **Vedere il contenuto (View):** Solo lettura decifrata.
```bash
ansible-vault view secrets.yml --vault-password-file .vault_pass

```


* **Cambiare la password (Rekey):** Se la password "la_mia_password_segreta" è compromessa.
```bash
ansible-vault rekey secrets.yml --vault-password-file .vault_pass

```

