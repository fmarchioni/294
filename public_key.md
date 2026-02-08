
## 📁 Copiare la chiave SSH nella cartella corretta

```cmd
copy C:\Users\UTENTE\Downloads\rht_classroom.rsa C:\Users\UTENTE\.ssh\rht_classroom.rsa
```

> Copia la chiave privata nella cartella SSH dell’utente Windows

---

## 🔐 Sistemare i permessi della chiave (da **cmd.exe**, non PowerShell)

```cmd
icacls "%USERPROFILE%\.ssh\rht_classroom.rsa" /inheritance:r
```

> Rimuove l’ereditarietà dei permessi

```cmd
icacls "%USERPROFILE%\.ssh\rht_classroom.rsa" /grant:r "%USERNAME%:R"
```

> Concede accesso in sola lettura solo all’utente corrente (richiesto da SSH)

---

## 🔗 Connessione SSH funzionante con jump host (senza config)

```cmd
ssh -i "C:\Users\UTENTE\.ssh\rht_classroom.rsa" ^
-o ProxyCommand="ssh -i C:\Users\UTENTE\.ssh\rht_classroom.rsa -p 22022 cloud-user@146.177.78.58 -W %h:%p" ^
student@workstation
```

> Connessione a `student@workstation` passando dal bastion `cloud-user`
> Metodo compatibile e affidabile su Windows

---

## ⚙️ Configurazione pulita (opzionale) — `~/.ssh/config`

📄 File: `C:\Users\UTENTE\.ssh\config`

```sshconfig
Host bastion
  HostName 146.177.78.58
  User cloud-user
  Port 22022
  IdentityFile C:\Users\UTENTE\.ssh\rht_classroom.rsa

Host workstation
  User student
  IdentityFile C:\Users\UTENTE\.ssh\rht_classroom.rsa
  ProxyCommand ssh bastion -W %h:%p
```

> Definisce il bastion e la workstation come alias SSH

---

## 🚀 Connessione finale (con config)

```cmd
ssh workstation
```

> Connessione semplice usando la configurazione SSH

---
