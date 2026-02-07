# Esempio di dynamic inventory

>Crea file aws.py:
>
```py
#!/usr/bin/env python3
import json
import sys

# Simuliamo un database dinamico o una risposta API
# In uno scenario reale, qui ci sarebbero chiamate boto3 (AWS) o azure sdk.
mock_infrastructure = {
    "webservers": {
        "hosts": ["web-app-01", "web-app-02"],
        "vars": {
            "http_port": 80,
            "proxy_timeout": 30
        }
    },
    "databases": {
        "hosts": ["db-master", "db-slave-01"],
        "vars": {
            "db_port": 5432
        }
    },
    # Il blocco _meta evita che Ansible chiami lo script separatamente per ogni host
    "_meta": {
        "hostvars": {
            "web-app-01": {"ip": "10.0.0.1", "region": "us-east"},
            "web-app-02": {"ip": "10.0.0.2", "region": "us-east"},
            "db-master":  {"ip": "10.0.0.3", "region": "us-west"},
            "db-slave-01": {"ip": "10.0.0.4", "region": "us-west"}
        }
    }
}

# Ansible chiama lo script con l'argomento --list per ottenere tutto
if len(sys.argv) == 2 and sys.argv[1] == '--list':
    print(json.dumps(mock_infrastructure))
# Ansible chiama con --host <hostname> per dettagli specifici (se non usiamo _meta)
elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    print(json.dumps({})) # Ritorna vuoto perché usiamo _meta sopra
else:
    # Fallback default
    print(json.dumps(mock_infrastructure))
```

>Dai permessi:
```
chmod +x finto_cloud.py
```

>Usa il file per generare un inventory dinamico:

```
ansible-inventory -i aws.py --graph
@all:
  |--@ungrouped:
  |--@webservers:
  |  |--web-app-01
  |  |--web-app-02
  |--@databases:
  |  |--db-master
  |  |--db-slave-01
```

In alternativa, esistono plugin diretti per ottenere l'Inventory da una sorgente. Es:
https://docs.ansible.com/projects/ansible/latest/collections/amazon/aws/aws_ec2_inventory.html
