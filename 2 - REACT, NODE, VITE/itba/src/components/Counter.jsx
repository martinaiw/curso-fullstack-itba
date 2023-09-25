import React, { useState } from "react";

export function Counter() {
    const [count, setCount] = useState(0);
    const incrementarContador = () => setCount(count + 1 );
    return (
        <div>
            <p>Contador: {count}</p>
            <button onClick={incrementarContador}>Incrementar</button>
        </div>
    );
}

