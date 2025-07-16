# Come controllare se un task fallisce in base all'exit code 

```yaml
- name: Run user creation script
  ansible.builtin.shell: /usr/local/bin/create_users.sh
  register: command_result
  failed_when: command_result.rc != 0
```


# NB Puoi anche specificare più condizioni in AND per controllare se un task è failed: 

```yaml
- name: Run user creation script
  ansible.builtin.shell: /usr/local/bin/create_users.sh
  register: command_result
  failed_when:
    - "'Password missing' in command_result.stdout"
    - command_result.rc != 0
```

# o anche in OR:

```yaml
failed_when: "'Password missing' in command_result.stdout or command_result.rc != 0"
```
