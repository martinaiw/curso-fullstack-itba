import React, { useState } from "react";

function Counter() {
    const [count, setCounter] = useState(0);
    return (  
        <>
        <p>Contador: {count} </p>
        <button onClick={() => setCounter(count + 1)}>Suma 1</button>
        <button onClick={() => setCounter(count - 1)}>Resta 1</button>
        <button onClick={() => setCounter(0)}>Reset</button>

        </>
    );
}

export default Counter;