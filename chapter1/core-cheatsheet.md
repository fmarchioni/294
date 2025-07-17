# 🧰 Ansible Core Cheatsheet

A quick reference guide for using Ansible Core (community edition) from the CLI.

---

## 🔧 Running Ad-Hoc Commands

```bash
ansible all -i inventory.ini -m ping
ansible webservers -i inventory.ini -m yum -a "name=httpd state=present" --become
```

## 📜 Running a Playbook

```bash
ansible-playbook -i inventory.ini playbook.yml
ansible-playbook -i inventory.ini playbook.yml --check --diff
```

## 🗂️ Inventory Examples

### INI format
```ini
[webservers]
web1.example.com
web2.example.com

[dbservers]
db1.example.com ansible_user=admin
```

### YAML format
```yaml
all:
  children:
    webservers:
      hosts:
        web1.example.com:
        web2.example.com:
    dbservers:
      hosts:
        db1.example.com:
          ansible_user: admin
```

## 🔐 Privilege Escalation

```yaml
# In playbook
- hosts: all
  become: true
```

```ini
# In ansible.cfg
[defaults]
become = true
```

## 📁 Project Structure (Best Practice)

```
project/
├── ansible.cfg
├── inventory.ini
├── playbook.yml
├── roles/
│   └── web/
│       ├── tasks/
│       │   └── main.yml
│       └── templates/
```

## 🔐 Encrypting Secrets with Vault

```bash
ansible-vault create secrets.yml
ansible-vault edit secrets.yml
ansible-vault view secrets.yml
ansible-playbook playbook.yml --ask-vault-pass
```

## 🧪 Useful Options

```bash
ansible-playbook playbook.yml --syntax-check
ansible-playbook playbook.yml --list-tasks
ansible-playbook playbook.yml --start-at-task="Install packages"
```

## 🛠️ ansible-core CLI Tools

These tools are standalone in Ansible Core but are accessed via `ansible-navigator` in AAP:

| Tool             | Description                               | Example Usage                      |
|------------------|-------------------------------------------|------------------------------------|
| `ansible-doc`    | Show documentation for modules/plugins     | `ansible-doc yum`                  |
| `ansible-galaxy` | Manage roles and collections               | `ansible-galaxy install <name>`    |
| `ansible-config` | View/validate configuration                | `ansible-config list`              |
| `ansible-inventory` | Inspect and validate inventory         | `ansible-inventory --list`         |
| `ansible-playbook` | Run playbooks                           | `ansible-playbook site.yml`        |
| `ansible-vault`  | Encrypt/decrypt/edit secrets               | `ansible-vault encrypt file.yml`   |

## 📦 Installing Ansible Core (if not available)

```bash
python3 -m venv venv
source venv/bin/activate
pip install ansible
```

---

✅ **Tip:** Use `--limit`, `--tags`, and `--check` often when developing!
