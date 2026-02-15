/**
 * main.js - Gestione del Frontend
 * Pulito da caratteri invisibili e ottimizzato.
 */

async function loadAllDirectives() {
    const container = document.getElementById('dynamic-directives-container');
    if (!container) return; // Sicurezza: evita errori se l'elemento non esiste

    try {
        const response = await fetch('/api/get_directives');
        if (!response.ok) throw new Error('Impossibile recuperare i dati dalle API');

        const data = await response.json();
        container.innerHTML = ''; 

        data.forEach(item => {
            const sectionDiv = document.createElement('div');
            sectionDiv.className = 'directive-block';
            sectionDiv.style.border = '1px solid #ccc';
            sectionDiv.style.padding = '15px';
            sectionDiv.style.marginBottom = '20px';
            
            sectionDiv.innerHTML = `
                <h3>${item.sezione}</h3>
                <textarea id="text-${item.id}" style="width:100%; min-height:100px;">${item.contenuto}</textarea>
                <br>
                <button id="btn-${item.id}" class="save-btn">Salva Modifiche</button>
            `;
            container.appendChild(sectionDiv);

            // Listener per il salvataggio
            document.getElementById(`btn-${item.id}`).addEventListener('click', () => updateDirective(item.id));
        });
    } catch (err) {
        console.error('Errore:', err.message);
        container.innerHTML = `<p style="color:red;">Errore di connessione: ${err.message}</p>`;
    }
}

async function updateDirective(id) {
    const textarea = document.getElementById(`text-${id}`);
    const btn = document.getElementById(`btn-${id}`);
    
    if (!textarea || !btn) return;

    const nuovoContenuto = textarea.value;
    btn.disabled = true;
    btn.innerText = 'Salvataggio in corso...';

    try {
        const response = await fetch('/api/update_directives', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id, contenuto: nuovoContenuto })
        });

        if (!response.ok) throw new Error('Errore durante il salvataggio');
        alert('Database aggiornato con successo!');
    } catch (err) {
        alert('Errore nel salvataggio: ' + err.message);
    } finally {
        btn.disabled = false;
        btn.innerText = 'Salva Modifiche';
    }
}

// Inizializzazione
document.addEventListener('DOMContentLoaded', loadAllDirectives);
