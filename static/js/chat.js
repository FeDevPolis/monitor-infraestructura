function toggleChat() {
    const panel = document.getElementById('chat-panel');
    panel.classList.toggle('abierto');
}

async function analizarInfraestructura() {
    const btn = document.getElementById('btn-analizar');
    const messages = document.getElementById('chat-messages');

    btn.disabled = true;
    btn.textContent = 'Analizando...';
    messages.innerHTML = '⏳ Consultando al asistente de IA...';

    try {
        const res = await fetch('/api/servidores/');
        const servidores = await res.json();

        const response = await fetch('/api/analizar/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ servidores })
        });

        const data = await response.json();

        if (data.respuesta) {
            const formateado = data.respuesta
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/\n\n/g, '<br><br>')
                .replace(/\n/g, '<br>')
                .replace(/(\d+)\./g, '<br><span class="numero-item">$1.</span>')
                .replace(/\* /g, '• ');
            messages.innerHTML = `<div class="mensaje-ia">🤖<br><br>${formateado}</div>`;
        } else {
            messages.innerHTML = `<span class="mensaje-error">❌ Error: ${data.error}</span>`;
        }
    } catch (error) {
        messages.innerHTML = `<span class="mensaje-error">❌ Error de conexión</span>`;
    } finally {
        btn.disabled = false;
        btn.textContent = 'Analizar servidores';
    }
}