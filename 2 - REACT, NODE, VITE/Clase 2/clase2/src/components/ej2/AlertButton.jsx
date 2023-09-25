

function showAlert() {
    alert('¡Hola! Esto es una alerta.');
}
function AlertButton() {
    const showAlert = () => { alert('¡Hola! Esto es una alerta.'); }
    return (
        <button onClick={showAlert}>Mostrar Alerta</button>
    );
}

export default AlertButton;