const API = '/api/servidores/';

async function cargarServidores() {
    const res = await fetch(API);
    const servidores = await res.json();
    renderTabla(servidores);
    renderStats(servidores);
}

function renderStats(servidores) {
    document.getElementById('count-activo').textContent = servidores.filter(s => s.estado === 'activo').length;
    document.getElementById('count-inactivo').textContent = servidores.filter(s => s.estado === 'inactivo').length;
    document.getElementById('count-mantenimiento').textContent = servidores.filter(s => s.estado === 'mantenimiento').length;
}

function renderTabla(servidores) {
    const tbody = document.getElementById('tabla-servidores');
    tbody.innerHTML = servidores.map(s => `
        <tr>
            <td>${s.nombre}</td>
            <td>${s.ip}</td>
            <td><span class="badge badge-${s.estado}">${s.estado}</span></td>
            <td>${s.descripcion}</td>
            <td>${new Date(s.fecha_ultimo_chequeo).toLocaleString('es-AR')}</td>
            <td>
                <button class="btn btn-activo" onclick="cambiarEstado(${s.id}, 'activo')">Activo</button>
                <button class="btn btn-inactivo" onclick="cambiarEstado(${s.id}, 'inactivo')">Inactivo</button>
                <button class="btn btn-mantenimiento" onclick="cambiarEstado(${s.id}, 'mantenimiento')">Mant.</button>
            </td>
        </tr>
    `).join('');
}

async function cambiarEstado(id, nuevoEstado) {
    const csrfToken = document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];

    await fetch(`${API}${id}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ estado: nuevoEstado })
    });
    cargarServidores();
}

cargarServidores();