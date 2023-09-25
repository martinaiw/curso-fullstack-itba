import React, { useState } from "react";

function ToDoList() {
  // Estado para almacenar la lista de tareas
  const [tasks, setTasks] = useState([]);
  // Estado para almacenar el valor del campo de entrada del formulario
  const [taskText, setTaskText] = useState("");

  // Función para manejar el envío del formulario y agregar una nueva tarea
  const addTask = (e) => {
    e.preventDefault(); // Evita que la página se recargue al enviar el formulario
    if (taskText.trim() === "") {
      return; // Evita agregar tareas vacías
    }

    // Crea una nueva tarea con un ID único
    const newTask = {
      id: Date.now(),
      text: taskText,
      completed: false,
    };

    // Agrega la nueva tarea al estado de tareas
    setTasks([...tasks, newTask]);

    // Limpia el campo de entrada del formulario
    setTaskText("");
  };

  // Función para marcar una tarea como completada
  const toggleTaskCompletion = (taskId) => {
    const updatedTasks = tasks.map((task) => {
      if (task.id === taskId) {
        return { ...task, completed: !task.completed };
      }
      return task;
    });
    setTasks(updatedTasks);
  };

  return (
    <div>
      <h2>ToDo List</h2>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => toggleTaskCompletion(task.id)}
            />
            {task.text}
          </li>
        ))}
      </ul>
      <form onSubmit={addTask}>
        <input
          type="text"
          placeholder="Nueva tarea"
          value={taskText}
          onChange={(e) => setTaskText(e.target.value)}
        />
        <button type="submit">Agregar</button>
      </form>
    </div>
  );
}

export default ToDoList;
