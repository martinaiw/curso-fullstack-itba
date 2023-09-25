export function Butono(props) {
    return (
        <button onClick={props.onClick}>
            {props.text}
        </button>
    );
}