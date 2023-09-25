import { useContext } from "react";
import { TasksContext } from "../App";


function DeleteTask() {
    const list = useContext(TasksContext);

    const handleDeleteClick = () => {
        onDeleteProduct(productName);
    };

    return (

        <button onClick={handleDeleteClick}>Eliminar</button>
    );
}




function TasksList() {
    const list = useContext(TasksContext);

    const handleDeleteTask = (taskD) => {
        const updatedList = list.filter((task) => task.text !== taskD);
        console.log("Tarea eliminada");
    };

    return (
        <>
            <ul>
                {list.map((task, index) => (
                    <div className="list-display">
                        <li key={index}>
                            {task.text}
                        </li>
                        <DeleteTask taskName={task.text} onDeleteTask={handleDeleteTask}/>
                    </div>
                ))}
            </ul>


        </>
    );
}

export default TasksList;