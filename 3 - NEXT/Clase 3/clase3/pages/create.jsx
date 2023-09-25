import { useState } from 'react';

function CrearNuevaTarea() {
  const [titulo, setTitulo] = useState('');

  const crearTarea = async () => {
    await fetch('https://jsonplaceholder.typicode.com/todos', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        title: titulo,
        completed: false
      })
    });
    window.location.href = '/';
  };

  return (
    <div>
      <h1>Crear Nueva Tarea</h1>
      <input
        type="text"
        value={titulo}
        onChange={e => setTitulo(e.target.value)}
      />
      <button onClick={crearTarea}>Crear Tarea</button>
    </div>
  );
}

export default CrearNuevaTarea;