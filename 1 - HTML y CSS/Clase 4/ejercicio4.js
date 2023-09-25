let nombre = prompt('Ingrese su nombre: ');

alert("Hola " + nombre);

let confirmacion = confirm("¿Deseas continuar?");

if(confirmacion){
    console.log("Continuando");
}else{
    console.log("Operación cancelada")
}