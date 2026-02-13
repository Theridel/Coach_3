# ROADMAP

    ## Fase 1a — Heartbeat (in corso)
    - [x] Definire architettura generale
    - [x] Creare cron job github per monitorare sistema (e tenerlo 'on')
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
