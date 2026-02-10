## Capitolo 3 - quiz veloce

1. In quale situazione è più utile usare una variabile invece di un valore fisso?  
   A. Quando il valore non cambia mai  
   B. Quando il valore dipende dall’ambiente o dall’host  
   C. Quando si scrive un playbook molto corto  
   D. Quando si usa un solo modulo  

2. Cosa succede se una variabile è definita in più punti con priorità diversa?  
   A. Ansible genera un errore  
   B. Viene usato il valore definito per primo  
   C. Viene usato il valore con priorità più alta  
   D. Dipende da come è scritto il playbook 

3. Cosa succede se una stessa variabile è definita sia in *group_vars* che in *host_vars* per un host?  
   A. Ansible genera un errore  
   B. Viene usato il valore di *group_vars*  
   C. I due valori vengono uniti  
   D. Viene usato il valore definito in *host_vars*  

4. In Ansible, a cosa servono i facts?  
   A. A memorizzare password in modo sicuro  
   B. A descrivere informazioni raccolte automaticamente sugli host  
   C. A definire i task da eseguire  
   D. A sostituire le variabili utente  

5. In quale caso potresti usare un fact in una condizione?  
   A. Per scegliere quale modulo installare Ansible  
   B. Per eseguire un task solo su certi sistemi operativi  
   C. Per criptare un file  
   D. Per definire l’inventario  

6. Cosa implica il fatto che i facts vengano raccolti automaticamente?  
   A. Che devono essere definiti manualmente dall’utente  
   B. Che Ansible interroga gli host prima di eseguire i task  
   C. Che funzionano solo in locale  
   D. Che sono sempre criptati  

7. A cosa serve Ansible Vault?  
   A. A eseguire playbook più velocemente  
   B. A proteggere dati sensibili come password e chiavi  
   C. A raccogliere facts dagli host  
   D. A gestire l’inventario  

8. Cosa cambia per l’utente quando un file è cifrato con Ansible Vault?  
   A. Non può più essere usato nei playbook  
   B. Deve fornire una password o una chiave per leggerlo  
   C. Viene eseguito automaticamente  
   D. Non può contenere variabili  

9. Qual è un vantaggio di Ansible Vault rispetto alla cifratura manuale dei file?  
   A. Non richiede alcuna password  
   B. È integrato direttamente nel flusso di Ansible  
   C. Funziona solo su sistemi Linux  
   D. Cripta solo i facts  

10. Perché Ansible Vault non elimina completamente il rischio di sicurezza?  
    A. Perché non funziona con i facts  
    B. Perché la sicurezza dipende anche dalla gestione delle password  
    C. Perché rallenta Ansible  
    D. Perché cripta solo una parte dei file  
