# Questo playbook dimostra idempotenza del modulo shell (stesso per cmd)

```yaml
---
- name: Verifica Idempotenza comando shell
  hosts: all
  gather_facts: false

  tasks:
    - name: Initialize the database
      ansible.builtin.shell:
        cmd: touch database.db
        #creates: database.db
```

In questo caso, lo script makedb.sh potrebbe contenere:

```shell
ansible-navigator run -i inventory.ini -m stdout idem.yml
```

Questo script verrà sempre eseguito. Ora scommenta *creates* e verifica che lo stato non è più changed:

```yaml
---
- name: Verifica Idempotenza comando shell
  hosts: all
  gather_facts: false

  tasks:
    - name: Initialize the database
      ansible.builtin.shell:
        cmd: touch database.db
        creates: database.db
```
