import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate();

  const manejarClick = () => {
    navigate('/eventos');
  };

  return (
    <div className="home-container">
      <h1>Bienvenido Analista</h1>
      <p>Presione el botón para registrar un resultado de revisión manual.</p>
    <button className='btn btn-primary' onClick={manejarClick}>Registrar</button>
    </div>
  );
}