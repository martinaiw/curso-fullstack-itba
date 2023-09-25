import { createContext, useContext, useState } from "react";
import { TasksContext } from "../App";

function AddTask() {
    const list = useContext(TasksContext);

    const [newTask, setNewTask] = useState({ text: "", state: 0 })

    const addTask = () => {
        const updatedList = [...list, newTask];
        console.log("Tarea agregada")
        setNewTask({ text: "", state: 0 });
    }
    return (
        <>
            <form>
                <input
                    type="text"
                    placeholder="Producto"
                    value={newTask.text}
                    onChange={(e) => setNewTask({ ...newTask, text: e.target.value })}
                />
                <button onClick={() => addTask({})}>Agregar nueva tarea</button>
            </form>
        </>
    );
}
export default AddTask;