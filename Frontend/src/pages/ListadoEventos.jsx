import React, { useState } from "react";

const eventos = [
  { id: 101, ubicacion: "Córdoba", magnitud: "M4.5", fecha: "2025-04-21" },
  { id: 102, ubicacion: "Salta", magnitud: "M3.8", fecha: "2025-04-20" },
  { id: 103, ubicacion: "San Juan", magnitud: "M5.2", fecha: "2025-04-19" },
  { id: 104, ubicacion: "Mendoza", magnitud: "M4.0", fecha: "2025-04-18" }
];

export default function ListadoEventos() {
  const [eventoSeleccionado, setEventoSeleccionado] = useState(null);

  const handleSelectChange = (e) => {
    const idSeleccionado = parseInt(e.target.value);
    const evento = eventos.find(ev => ev.id === idSeleccionado);
    setEventoSeleccionado(evento || null);
  };

  return (
    <div>
      <header className="bg-dark text-white text-center py-4">
        <h1>🌍 Red Sísmica</h1>
        <img src="/image.png" alt="Sismograma" className="img-fluid w-100" style={{ height: "200px", objectFit: "cover", borderBottom: "4px solid #133636" }} />
      </header>

      <div className="container my-5 p-4 bg-white rounded shadow">
        <h2 className="text-center text-dark">Eventos no revisados</h2>

        <select className="form-select mt-3" onChange={handleSelectChange} defaultValue="">
          <option value="">Seleccione un evento...</option>
          {eventos.map(evento => (
            <option key={evento.id} value={evento.id}>
              Evento {evento.id} - {evento.ubicacion} ({evento.magnitud})
            </option>
          ))}
        </select>

        {eventoSeleccionado && (
          <div className="mt-4 p-3 border rounded bg-light">
            <p><strong>Magnitud:</strong> {eventoSeleccionado.magnitud}</p>
            <p><strong>Ubicación:</strong> {eventoSeleccionado.ubicacion}</p>
            <p><strong>Fecha:</strong> {eventoSeleccionado.fecha}</p>
            <button className="btn btn-dark w-100 mt-3">✅ Marcar como revisado</button>
          </div>
        )}
      </div>

      <footer className="text-center text-muted mt-5 mb-3">
        Sistema de monitoreo sísmico - 2025
      </footer>
    </div>
  );
}