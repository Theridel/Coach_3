# ROADMAP (valido)

    ## Fase 1a — Heartbeat 
    - [x] Definire architettura generale  
    - [x] Creare cron job github per monitorare sistema (e tenerlo 'on')  

    (in corso)
    
    - [x] Salvare su Supabase il log di Github
    - [x] Salvare su Supabase il log di Github tramite orchestrator HF
    - [ ] Sanificare il json di comunicazione
    - [ ] Ripulire comunicazione diretta github-supabase e tabella heartbeat

    ## Fase 1a — interfaccia Vercel
    - [x] Salvare e leggere stringhe con Supabase
    - [ ] Rendere privato orchestrator HF e verificare heartbeat
    - [ ] Sanificare il json di comunicazione
    
    ## Fase 2 — Pipelines di orchestrazione
    - [ ] Aggiornare script 0 e script 1 per HF/Colab
    
    - [ ] Integrità dependences (pip check + versioni)
    - [ ] Stabilire schema Firestore
    
    ## Fase 3 — Hard Compute
    - [ ] Colab: moduli orchestratore + import moduli .py
    - [ ] Sagemaker Studio Lab: GPU tasks

    ## Fase 4 — Ottimizzazione
    - [ ] Ridurre i range package prudenziali
    - [ ] Automatizzare sincronizzazione GitHub → HF

Nuovo

Roadmap di Sistema — Multi‑Agente con Orchestratore HF

• 	[x] Salvare su Supabase il log di GitHub
• 	[x] Salvare su Supabase il log di GitHub tramite orchestrator HF
• 	[ ] aggiornare Actions a @v4
• 	[ ] Sanificare il JSON di comunicazione
• 	[ ] Ripulire comunicazione diretta GitHub → Supabase e tabella heartbeat
• 	[ ] Normalizzare identità dell’agente GitHub ()
• 	[ ] Definire permessi minimi dell’agente GitHub
• 	[ ] Implementare tabelle
• 	[ ] Validazione heartbeat lato BUS (anti‑allucinazione)

Fase 1b — Interfaccia Vercel
• 	[x] Salvare e leggere stringhe con Supabase
• 	[ ] Rendere privato orchestrator HF e verificare heartbeat
• 	[ ] Sanificare il JSON di comunicazione
• 	[ ] Spostare ogni chiamata Vercel → Supabase sotto il BUS
• 	[ ] Definire schema minimo degli intenti lato interfaccia
• 	[ ] Implementare rate‑limit e throttling sul BUS

Fase 2 — Pipelines di orchestrazione
• 	[ ] Aggiornare script 0 e script 1 per HF/Colab
• 	[ ] Integrità dependences (pip check + versioni)
• 	[ ] Stabilire schema Firestore
• 	[ ] Definire protocollo degli intenti (cervelli → BUS)
• 	[ ] Implementare primo cervello: Planner
• 	[ ] Implementare secondo cervello: RAG Reader (solo lettura)
• 	[ ] Implementare BUS come unico writer su Supabase
• 	[ ] Introdurre SQLite locale per stato effimero (opzionale)
• 	[ ] Definire pipeline di validazione (BUS → Supabase)

Fase 3 — Hard Compute
• 	[ ] Colab: moduli orchestratore + import moduli .py
• 	[ ] Sagemaker Studio Lab: GPU tasks
• 	[ ] Definire protocollo di job asincroni (BUS → compute)
• 	[ ] Implementare task queue locale (SQLite o in‑memory)
• 	[ ] Logging strutturato dei job in 

Fase 4 — Ottimizzazione
• 	[ ] Ridurre i range package prudenziali
• 	[ ] Automatizzare sincronizzazione GitHub → HF
• 	[ ] Introdurre caching RAG locale (solo lettura)
• 	[ ] Pulizia automatica dello stato effimero
• 	[ ] Ottimizzare schema Supabase per query frequenti

Fase 5 — Sicurezza e Robustezza
• 	[ ] Implementare firewall semantico nel BUS
• 	[ ] Validazione degli intenti prima della scrittura
• 	[ ] Shadow mode per nuove capacità dei cervelli
• 	[ ] Logging completo degli intenti rifiutati
• 	[ ] Policy per agenti effimeri (GitHub, Deta)

Fase 6 — Multicervello
• 	[ ] Planner
• 	[ ] RAG Reader
• 	[ ] Analista
• 	[ ] Generatore
• 	[ ] Routing intelligente nel BUS
• 	[ ] Composizione asincrona delle risposte
