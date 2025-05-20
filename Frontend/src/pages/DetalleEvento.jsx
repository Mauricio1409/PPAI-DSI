import React from "react";

const evento = {
    titulo: "Concierto de Rock",
    fecha: "2024-07-15",
    hora: "20:00",
    lugar: "Teatro Municipal",
    descripcion: "Disfruta de una noche inolvidable con las mejores bandas de rock.",
    imagen: "https://via.placeholder.com/600x300?text=Evento",
    organizador: "Producciones XYZ",
};

export default function DetalleEvento() {
    return (
        <div className="container mt-5">
            <div className="card mb-3">
                <img src={evento.imagen} className="card-img-top" alt={evento.titulo} />
                <div className="card-body">
                    <h2 className="card-title">{evento.titulo}</h2>
                    <p className="card-text">
                        <strong>Fecha:</strong> {evento.fecha}
                    </p>
                    <p className="card-text">
                        <strong>Hora:</strong> {evento.hora}
                    </p>
                    <p className="card-text">
                        <strong>Lugar:</strong> {evento.lugar}
                    </p>
                    <p className="card-text">{evento.descripcion}</p>
                    <p className="card-text">
                        <small className="text-muted">Organizado por {evento.organizador}</small>
                    </p>
                    <a href="#" className="btn btn-primary">
                        Comprar entradas
                    </a>
                </div>
            </div>
        </div>
    );
}