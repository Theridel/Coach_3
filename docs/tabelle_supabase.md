### Tabella: agents

| Campo         | Tipo         | Descrizione |
|---------------|--------------|-------------|
| id            | uuid (PK)    | Identificatore univoco dell’agente. |
| name          | text         | Nome leggibile (es. `hf-planner-1`). |
| type          | text         | Categoria: `orchestrator`, `cervello`, `operativo`, `supervisor`, `frontend`, `microservice`. |
| provider      | text         | Dove vive: `huggingface`, `github`, `deta`, `vercel`, `colab`, `sagemaker`, `firebase`. |
| role          | text         | Ruolo specifico: `planner`, `rag-reader`, `generator`, `analyst`, `runtime`, `cron`, `ui`. |
| status        | text         | Stato: `online`, `offline`, `busy`, `error`, `unknown`. |
| last_seen     | timestamptz  | Ultimo heartbeat ricevuto. |
| capabilities  | jsonb        | Funzioni dichiarate (modelli, tool, limiti). |
| permissions   | jsonb        | Permessi: `read_rag`, `propose_write`, `execute_task`, `write_db` (solo orchestratore). |
| version       | text         | Commit o versione del codice. |
| metadata      | jsonb        | Info aggiuntive (endpoint, note, configurazioni). |
| created_at    | timestamptz  | Timestamp creazione. |
| updated_at    | timestamptz  | Timestamp aggiornamento. |

### Tabella: agent_heartbeat

| Campo       | Tipo         | Descrizione |
|-------------|--------------|-------------|
| id          | uuid (PK)    | Identificatore del record. |
| agent_id    | uuid (FK)    | Riferimento a `agents.id`. |
| timestamp   | timestamptz  | Momento del ping. |
| status      | text         | Stato riportato dall’agente. |
| load        | jsonb        | Info opzionali (CPU, queue, job in corso). |

### Tabella: agent_events

| Campo        | Tipo         | Descrizione |
|--------------|--------------|-------------|
| id           | uuid (PK)    | Evento univoco. |
| agent_id     | uuid (FK)    | Agente che ha generato l’evento. |
| event_type   | text         | `intent`, `proposal`, `task_start`, `task_end`, `error`. |
| payload      | jsonb        | Contenuto dell’evento. |
| validated    | boolean      | Se il BUS ha approvato l’azione. |
| created_at   | timestamptz  | Timestamp. |

### Tabella: tasks

| Campo         | Tipo         | Descrizione |
|---------------|--------------|-------------|
| id            | uuid (PK)    | Identificatore del task. |
| parent_id     | uuid (FK)    | Task padre (per piani multi-step). |
| created_by    | uuid (FK)    | Agente che ha creato il task. |
| assigned_to   | uuid (FK)    | Agente operativo assegnato. |
| status        | text         | `pending`, `running`, `done`, `failed`. |
| priority      | int          | Priorità del task. |
| payload       | jsonb        | Parametri del task. |
| result        | jsonb        | Risultato finale. |
| created_at    | timestamptz  | Timestamp creazione. |
| updated_at    | timestamptz  | Timestamp aggiornamento. |

### Tabella: task_events

| Campo        | Tipo         | Descrizione |
|--------------|--------------|-------------|
| id           | uuid (PK)    | Evento univoco. |
| task_id      | uuid (FK)    | Riferimento a `tasks.id`. |
| agent_id     | uuid (FK)    | Agente che ha generato l’evento. |
| event_type   | text         | `start`, `progress`, `end`, `error`. |
| payload      | jsonb        | Dettagli dell’evento. |
| created_at   | timestamptz  | Timestamp. |

### Tabella: intents

| Campo        | Tipo         | Descrizione |
|--------------|--------------|-------------|
| id           | uuid (PK)    | Intent univoco. |
| agent_id     | uuid (FK)    | Cervello che ha generato l’intento. |
| intent_type  | text         | Tipo di azione proposta. |
| payload      | jsonb        | Dati dell’intento. |
| approved     | boolean      | Se l’orchestratore ha approvato. |
| applied      | boolean      | Se è stato applicato al DB. |
| created_at   | timestamptz  | Timestamp. |
| updated_at   | timestamptz  | Timestamp. |

### Tabella: agent_permissions

| Campo        | Tipo         | Descrizione |
|--------------|--------------|-------------|
| id           | uuid (PK)    | Record univoco. |
| agent_id     | uuid (FK)    | Agente. |
| permission   | text         | Permesso singolo (es. `read_rag`). |
| created_at   | timestamptz  | Timestamp. |

### Tabella: agent_capabilities

| Campo        | Tipo         | Descrizione |
|--------------|--------------|-------------|
| id           | uuid (PK)    | Record univoco. |
| agent_id     | uuid (FK)    | Agente. |
| capability   | text         | Capacità (es. `summarize`, `classify`, `generate`). |
| metadata     | jsonb        | Info aggiuntive. |
| created_at   | timestamptz  | Timestamp. |

### Tabella: direttive_ai
### Tabella: contesto_progetto
### Tabella: sessioni_cpaching
### Tabella: heartbeat (da sostituire con agent_heartbeat)
