# Test minimi che puoi già implementare (oggi)
Questi test sono semplici, concreti e non richiedono infrastruttura complessa.

## 1) Test di validazione JSON (agenti → orchestratore)
Ogni payload ricevuto deve essere validato contro uno schema.
### Test:
• 	invia JSON malformato,
• 	invia JSON con campi mancanti,
• 	invia JSON con campi extra,
• 	invia JSON con tipi sbagliati.
### Obiettivo:
• 	l’orchestratore deve rispondere con errore controllato,
• 	non deve crashare,
• 	non deve scrivere nulla su Supabase.

## 2) Test di permessi Supabase
### Crea una chiave read-only e prova:
• 	lettura → deve funzionare,
• 	scrittura → deve fallire,
• 	update → deve fallire,
• 	delete → deve fallire.
### Obiettivo:
• 	verificare che nessun agente possa scrivere direttamente.

## 3) Test di resilienza dell’orchestratore
### Simula errori:
• 	input vuoto,
• 	input enorme,
• 	input con caratteri strani,
• 	input con cicli,
• 	input con payload annidati.
### Obiettivo:
• 	l’orchestratore deve restare vivo,
• 	deve loggare l’errore,
• 	deve ignorare l’input.

## 4) Test di caduta dell’orchestratore
### Spegni l’orchestratore HF e verifica:
• 	GitHub Action → cosa fa?
• 	Vercel → cosa fa?
• 	Agenti esterni → cosa fanno?
• 	Supabase → registra l’assenza?
## Obiettivo:
• 	capire se il sistema degrada in modo sicuro.

## 5) Test di chiavi compromesse
### Simula l’uso di una chiave Supabase sbagliata:
• 	chiave scaduta,
• 	chiave revocata,
• 	chiave con permessi insufficienti.
### Obiettivo:
• 	capire se gli agenti falliscono in modo chiaro,
• 	verificare che non ci siano fallback pericolosi.

## 6) Test di isolamento degli agenti
### Prova a far fare a un agente qualcosa che non dovrebbe:
• 	scrivere su Supabase,
• 	leggere tabelle non autorizzate,
• 	inviare comandi non previsti.
### Obiettivo:
• 	verificare che l’orchestratore blocchi tutto
