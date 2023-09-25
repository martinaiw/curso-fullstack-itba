import React, { useState, useEffect } from "react";
import { Orbit } from '@uiball/loaders';

function Hooks() {
    const [perritos, setPerritos] = useState("nada");
    //useState ->
    //useEffect ->
    //las variables se componen de
    //1) Nombre de variable
    //2) Funcion de actualizacion
    //3) Valor inicial

    const [contador, setContador] = useState(0);
    //const [nombre, setNombre] = useState("Sin nombre");
    //const arr = ["Carlos", "Lourdes", "Sofia", "Julian", "Martina"];

    useEffect(() => {
        fetch("https://dog.ceo/api/breeds/image/random")
            .then((response) => response.json())
            .then((dog) => {
                setPerritos(dog);
                console.log(perritos);
            });
    }, [])


    // vacio se ejecuta todo el timpo, [] se ejecuta por primera vez cuando arranca el componente, 
    //o puede tener una variable de estado




    return (
        <>
            <h1>Look how cute they are</h1>
            {
                perritos.message ?
                    <>
                        <img src={perritos.message} alt="foto de un mauser" style={{ height: '502px' }}/>
                        <h2>{perritos.status}</h2>
                    </>
                    :
                    <img src="./loading.gif" alt="" style={{ height: '50px' }}/>
            }
        </>
    );
}

export default Hooks;







{/* <h2>La variable contador es igual a {contador}</h2>
<button onClick={() => setContador(contador + 1)}>Sumar +1</button>
<button onClick={() => setContador(contador - 1)}>Restar -1</button>
<button onClick={() => setContador(0)}>Reiniciar la variable contador</button> */}



{/* <h2>El nombre actual es: {nombre}</h2>
            <input type="text" onChange={e => setNombre(e.target.value)} />
            <button onClick={() => setNombre(arr[i])}>Cambiar nombre</button> */}
