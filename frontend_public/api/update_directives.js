import { createClient } from '@supabase/supabase-js';

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).send('Method Not Allowed');

  const { id, contenuto } = req.body;
  const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_ANON_KEY);

  try {
    // 1. SALVATAGGIO DIRETTO (Priorità assoluta)
    const { error } = await supabase
      .from('direttive_ai')
      .update({ 
        contenuto: contenuto, 
        ultima_modifica: new Date().toISOString() 
      })
      .eq('id', id);

    if (error) throw error;

    // 2. INVIO A HUGGING FACE (In background)
    // Non usiamo "await" qui per la risposta, così restituiamo subito successo all'utente
    const hfPayload = {
      id,
      contenuto,
      source: "vercel_app",
      notes: "Async relay from Vercel"
    };

    // Lanciamo la chiamata a HF "a perdere" (fire and forget)
    // o con un leggero delay gestito via codice
    fetch("https://theridel-orchestratore.hf.space/webhook", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(hfPayload)
    }).catch(err => console.error("HF Relay failed:", err));

    // 3. RISPOSTA IMMEDIATA AL FRONTEND
    return res.status(200).json({ 
      success: true, 
      message: 'Database aggiornato. Relay HF avviato.' 
    });

  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}
