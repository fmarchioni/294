## With file example

```yaml

---
- hosts: localhost
  tasks:
    - name: create a file number 1 for this example
      blockinfile:
        path: "{{playbook_dir}}/first.txt"
        block: "first file"
        create: True

    - name: create a file number 2 for this example
      blockinfile:
        path: "{{playbook_dir}}/second.txt"
        block: "second file"
        create: True

    # emit a debug message containing the content of each file.
    - name: loop through files and print out the content
      debug:
        msg: "{{ item }}"
      with_file:
        - first.txt
        - second.txt
```


     
## With sequence example

```yaml
- name: Create and build test
  gather_facts: False
  hosts: localhost
  connection: local
  tasks:
    - command: "oc new-project {{ item }}"
      with_sequence: start=0 end=9 format=bs%02x
      ignore_errors: True
    - command: "oc -n {{ item }} new-build --name generic -D 'FROM centos\nRUN yum install wget -y'"
      with_sequence: start=0 end=9 format=bs%02x
    - command: "oc -n {{ item }} patch buildconfig generic -p '{\"spec\":{\"resources\": {\"requests\":{\"cpu\":\"1000m\",\"memory\":\"4Gi\"}}}}'"
      with_sequence: start=0 end=9 format=bs%02x
    - command: "oc -n {{ item }} cancel-build bc/generic"
      with_sequence: start=0 end=9 format=bs%02x
    - command: "oc -n {{ item }} start-build bc/generic"
      with_sequence: start=0 end=9 format=bs%02x
```
