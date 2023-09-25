import Link from 'next/link';

function PaginaInicio({ tareas }) {
    return (
        <div>
            <h1>Lista de Tareas</h1>
            <Link href="/create">Crear Tarea</Link>
            <ul>
                {tareas.map(tarea => (
                    <li key={tarea.id}>{tarea.title}</li>
                ))}
            </ul>
        </div>
    );
}

export async function getServerSideProps() {
    const res = await fetch('https://jsonplaceholder.typicode.com/todos');
    const tareas = await res.json();

    return {
        props: { tareas }
    };
}

export default PaginaInicio;