/*Debes crear un componente de React llamado TodoList que renderice una lista de tareas pendientes.
El componente debe seguir las siguientes especificacione
El componente TodoList recibe una prop llamada todos, que es un arreglo de objetos con la 
siguiente estructura: { id, task }. 
Cada objeto representa una tarea con un identificador único (id) y el nombre de la tarea (task).
Renderiza un elemento ul (lista desordenada).
Utiliza el método map() para iterar sobre el arreglo todos y renderizar un elemento li (elemento 
de lista) por cada objeto de la lista.
Cada li debe mostrar el nombre de la tarea.
Asigna un atributo key único a cada li utilizando el valor de id de cada objeto de la lista.
Tu tarea consiste en completar el componente TodoList para que cumpla con las especificaciones 
mencionadas y renderice correctamente la lista de tareas pendientes. */


function TodoList(props) {
    const todos = [
        { id: 1, task: 'Hacer la compra' },
        { id: 2, task: 'Llamar al médico' },
        { id: 3, task: 'Enviar el informe' },
        { id: 4, task: 'Enviar el informe' },
        { id: 5, task: 'Enviar el informe' },
        { id: 6, task: 'Enviar el informe' },
        { id: 7, task: 'Enviar el informe' },
    ];
    const listItems = todos.map(tarea => <li>{tarea.id} - {tarea.task}</li>);
    const evenIds = todos.filter(tarea => tarea.id % 2 === 0);
    const listEvenItems = evenIds.map(tarea => <li>{tarea.id} - {tarea.task}</li>);
    return (
        <>
            <ul>
                {listItems}
            </ul>
            <ul>
                <p>Tareas con Id par</p>
                {listEvenItems}
            </ul>
        </>

    );
}

export default TodoList;