// ?Debes crear un componente de React que renderice un mensaje diferente según una condición dada. 
// ?El componente debe seguir las siguientes especificaciones:
// ?El componente se llama ConditionalRendering.
// *Tiene un estado interno llamado showMessage que es un booleano y se inicia en false.
// *Renderiza un elemento div que contiene un título h1.
// *Si showMessage es true, el título debe mostrar el mensaje "¡Mensaje mostrado!".
// *Si showMessage es false, el título debe mostrar el mensaje "Haz clic para mostrar el mensaje".
// *Debajo del título, agrega un botón que al hacer clic cambie el estado de showMessage a su 
// *valor opuesto.

import { useState } from "react";

useState
function ConditionalRendering() {
    const [showMessage, setShowMessage] = useState(false);
    const toggleMessage = () => {
        setShowMessage(!showMessage);
      };
    return (  
        
        <div>
         {showMessage ? <h1>¡Mensaje mostrado!</h1> : <p>Haz clic para mostrar el mensaje</p>}
         <button onClick={toggleMessage}>Click</button>
        </div>

    );
}

export default ConditionalRendering;