


*   **Vercel** → Sito pubblico / API leggere. → Interfaccia col sistema
*   **Supabase** → SQL + Vector Store. → Storage e RAG
*   **GitHub** → Repository + Actions.
*   **Hugging Face Space A** → Orchestratore dei moduli 
*   (da verificare)  
*   **Hugging Face Space** → Interfaccia AI + runtime controllato.  
*   **Firebase Spark** → Authentication, Firestore (o RTDB), Functions (free), Hosting, Storage.
*   **Colab / Sagemaker SL** → Orchestrazione e lavori pesanti.
*   **Neo4j AuraDB Free** → Knowledge graph.
*   **Deta Space** → Microservizi + Cron.

### **b) Come comunicano** (da verificare)

Un semplice schema ASCII nel markdown:

                ┌──────────┐
                │   Vercel │  Interfaccia
                └─────┬────┘
                      │ REST
                      ┼─────────────┐
                      │             │
    ┌──────────┐  ┌───▼───────┐  ┌──▼──────────┐
    │ Github   │──│ HF Space  │  │ Deta Space  │
    │Cron Jobs │  │ SQL+Vec   │  │ AI runtime  │Deta Space
    └────┬─────┘  └────┬──────┘  └────┬────────┘
         │             │              │
         │             │ Storage/     │ Jobs
         │             │ functions    │
    ┌────▼──────────┐  │          ┌───▼─────────┐Firebase
    │ Supabase      │◄─┘          │ Colab/SMSL  │
    │ AI runtime    │             │ Orchestrator│ Spark
    └───────────────┘             └──────────────┘

### **a) Componenti e ruolo** 

Livello 1 — Interfaccia e Accesso
Componenti che ricevono input dall’utente o da sistemi esterni e li inoltrano al BUS.
• 	Vercel — Sito pubblico, API leggere, punto di ingresso del sistema.
• 	Hugging Face Space (UI) — Interfaccia AI controllata, eventuale chat o pannello operativo.
• 	Firebase Spark (Auth + Hosting) — Autenticazione utenti, hosting statico, eventuali funzioni leggere.

Livello 2 — Orchestrazione e BUS centrale
Componenti che decidono, validano, coordinano e controllano tutto il traffico interno.
• 	Hugging Face Space A (Orchestratore / BUS)
• 	unico punto autorizzato a scrivere su Supabase
• 	valida gli intenti
• 	smista i messaggi
• 	applica policy e sicurezza
• 	compone risposte da più cervelli
• 	GitHub Actions (Supervisor Agent)
• 	cron, health‑check, manutenzione
• 	comunica solo con il BUS
• 	Deta Space (Microservizi + Cron)
• 	agenti autonomi che parlano solo con il BUS
• 	funzioni leggere, servizi di supporto

Livello 3 — Cervelli e Ragionamento
Moduli cognitivi specializzati, attivati dal BUS solo quando serve.
Tutti in sola lettura verso RAG e database, mai scrittura diretta.
• 	HF Space – Planner — decomposizione obiettivi, generazione piani.
• 	HF Space – RAG Reader — interrogazione Supabase/Vector, sintesi contesto.
• 	HF Space – Analista — classificazioni, valutazioni, trasformazioni.
• 	HF Space – Generatore — generazione testo, risposte, contenuti.
• 	(altri cervelli futuri: reasoning, code, tool‑use, ecc.)

Livello 4 — Agenti Operativi (Compute)
Eseguono lavoro pesante o specializzato, su richiesta del BUS.
• 	Colab — compute gratuito, batch, modelli pesanti.
• 	SageMaker Serverless — inferenze scalabili, job asincroni.
• 	HF Runtime Spaces — modelli leggeri, funzioni veloci.

Livello 5 — Memoria e Conoscenza
Unico livello che conserva lo stato del sistema.
Scrittura solo tramite BUS, lettura da cervelli e agenti tramite BUS o endpoint dedicati.
• 	Supabase SQL — stato del sistema, agenti, heartbeat, task, configurazioni.
• 	Supabase Vector Store — memoria semantica, RAG.
• 	Neo4j AuraDB Free — knowledge graph strutturato.
• 	Firebase Firestore/RTDB — eventuale memoria volatile o user‑specific

                         ┌──────────────────────┐
                         │      INTERFACCIA      │
                         │  (Vercel / HF UI /    │
                         │   Firebase Auth)      │
                         └───────────┬───────────┘
                                     │  REST/API
                                     ▼
                     ┌──────────────────────────────────┐
                     │      HF ORCHESTRATOR / BUS       │
                     │  - unico punto che scrive su DB  │
                     │  - valida, filtra, compone       │
                     │  - smista messaggi               │
                     └───────┬──────────┬──────────────┘
                             │          │
                             │          │
                             │          │
               ┌─────────────▼───┐   ┌──▼────────────────┐
               │   CERVELLO 1     │   │    CERVELLO 2      │
               │   (Planner)      │   │   (RAG Reader)     │
               │   - reasoning    │   │   - sola lettura   │
               │   - piani        │   │   - contesto RAG   │
               └──────────┬──────┘   └──────────┬─────────┘
                          │                     │
                          │                     │
               ┌──────────▼────────┐   ┌────────▼─────────┐
               │   CERVELLO 3       │   │   CERVELLO 4      │
               │   (Analista)       │   │   (Generatore)    │
               │   - classificazioni│   │   - output testo  │
               └──────────┬────────┘   └────────┬──────────┘
                          │                     │
                          │                     │
                          ▼                     ▼
                     ┌──────────────────────────────────┐
                     │        AGENTI OPERATIVI          │
                     │  (HF Runtime / Deta / GitHub /   │
                     │   Colab / SageMaker SL)          │
                     │  - esecuzione task               │
                     │  - compute pesante               │
                     └───────────┬──────────────────────┘
                                 │
                                 │  solo tramite BUS
                                 ▼
                     ┌──────────────────────────────────┐
                     │            MEMORIA                │
                     │        (Supabase SQL + Vector)    │
                     │        (Neo4j AuraDB)             │
                     │  - stato del sistema              │
                     │  - RAG in sola lettura            │
                     │  - scrittura SOLO via BUS         │
                     └──────────────────────────────────┘
