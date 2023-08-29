

function Segundo(props) {
    const saludar = () => {
        alert("Hello everynyan, " + props.nombre)
    };
return (
    <div>
        <h1 className="shadow p-3 mb-5 bg-white rounded border border-success">
            Hola {props.nombre}, tu cumple fue
            el {+(props.numero1) + +(props.numero2)} de agosto
            <button onClick={saludar} className="btn btn-success">Dar beso</button>
        </h1>
    </div>
)

}
export default Segundo;
