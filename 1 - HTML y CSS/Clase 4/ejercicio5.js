let num1 = prompt("Ingrese el primer numero: ");
let num2 = prompt("Ingrese el segundo numero: ");

function sumarNumeros(num1, num2) {
    return +num1 + +num2;
}

console.log("El resultado de la suma es: " + sumarNumeros(num1, num2));