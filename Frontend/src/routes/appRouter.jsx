import { Routes, Route } from 'react-router-dom';
import Home from '../pages/home';
import ListadoEventos from '../pages/ListadoEventos';
import DetalleEvento from '../pages/DetalleEvento';

export default function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/eventos" element={<ListadoEventos />} />
      <Route path="/evento/:id" element={<DetalleEvento />} />
    </Routes>
  );
}