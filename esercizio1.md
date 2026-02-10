## Assignment

Realizza un playbook Ansible chiamato **play.yml** che utilizzi un inventory composto da due gruppi:

| Gruppo | Host |
|--------|-------|
| prod   | servera |
| dev    | serverb |

Obiettivi:

- Gli host del gruppo **prod** devono creare un file `/home/student/log` contenente:
  ```
  server prod
  ```
- Gli host del gruppo **dev** devono creare un file `/tmp/log` contenente:
  ```
  server dev
  ```
- Nel playbook inserisci due play. Un play scriverà sul gruppo **prod** ed un altro play sul gruppo **dev**
- Usa il modulo **ansible.builtin.copy** che è in grado di creare automaticamente le directory mancanti e scrivere il contenuto del file attraverso l'attributo **content**.



---

## Suggerimenti

- Il capitolo 2 del Bookshelf contiene esempi di play con più playbooks
- Con il comando `ansible-navigator doc ansible.builtin.copy` si può vedere la documentazione del comando copy
