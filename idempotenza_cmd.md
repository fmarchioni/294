# Questo playbook dimostra idempotenza del modulo cmd

```yaml
---
- name: Verifica Idempotenza comando cmd
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Initialize the database
      ansible.builtin.command:
        cmd: /home/student/makedb.sh
        creates: database.db
```

In questo caso, lo script makedb.sh potrebbe contenere:

```shell
touch database.db
```

Questo script verrà eseguito una volta sola. Ora commenta *creates* e verifica che viene sempre rieseguito:

```yaml
---
- name: Verifica Idempotenza comando cmd
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Initialize the database
      ansible.builtin.command:
        cmd: /home/student/makedb.sh
        #creates: database.db
```
