

function Primero(props) {
    const suma = 10 + 10;
    if (props.nombre == "Martina") {
        var nombre = "Mar";
    } else {
        var nombre = "No Mar"
    }
    return (
        <>
            <h1 className="shadow p-3 mb-5 bg-white rounded border border-success">
                Hola!!!! {nombre}/{props.nombre} {props.apellido}, ¿cómo estás?, tu edad es {suma}
            </h1>
        </>
    );

}


export default Primero;