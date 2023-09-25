import { useEffect } from "react";


function GetPokemon() {
    
    useEffect(() => {
        fetch("https://pokeapi.co/api/v2/pokemon?limit=100")
            .then((response) => response.json())
            .then((allpokemon) => console.log("Traje 100 pokemones"))
            .catch(error => console.error("El error es "+ error));
    }, [])
    return (  
        <h1>Hola probando</h1>



    );
}

export default GetPokemon;


