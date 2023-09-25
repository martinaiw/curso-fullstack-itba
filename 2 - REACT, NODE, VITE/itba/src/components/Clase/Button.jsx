




function Button({primary, text}) {

    return (
        <>
            <button className = { primary ? 'boton-primario' : 'boton-secundario' }>
                {text}
            </button>
        </>
    )
}
export default Button;