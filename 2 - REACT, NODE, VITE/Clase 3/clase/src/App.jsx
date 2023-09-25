import { createContext, useContext, useState } from "react";
import AddTask from "./Ej2/AddTask";

/*
Desarrolla  una  aplicación  de  gestión  de  tareas  utilizando  React  Context.  Crea  un 
contexto de tareas que permita compartir y administrar el estado de las tareas en toda 
la aplicación. 
Implementa componentes para 
mostrar la lista de tareas, 
agregar nuevas tareas, 
marcar tareas como completadas y 
eliminar tareas. 
Utiliza React Context para compartir  el  estado  de  las  tareas  entre  los  
componentes  y  asegúrate  de  que  las actualizaciones  en  las  tareas  se  reflejen  
correctamente  en  todos  los  componentes consumidores.  Además,  agrega  la  funcionalidad  
de  filtrado  para  mostrar  tareas completadas y pendientes. 

*/
export const TasksContext = createContext();

function App() {
    const list = [
        { text: "Task 1", state: true, id: 0 },
        { text: "Task 2", state: false, id: 1 },
    ];
    const [task, setTask] = useState(list);

    return (
        <>
            <TasksContext.Provider value={list}>
                <AddTask />
            </TasksContext.Provider>
        </>
    );
}

export default App;

