/*Escribí una función en JavaScript llamada sumaNumerosPares que reciba 
un arreglo de números como argumento y devuelva la suma de todos los 
números pares presentes en el arreglo. */

var arreglo = [2, 6, 9, 1, 2, 0, 13]
function sumaNumerosPares(arr) {
    var suma = 0;
    for (var i = 0; i < arr.length; i++){
        if(arr[i] % 2 === 0){
            suma += arr[i];
        }
    }
    return suma;
}
var arreglo = [2, 6, 9, 1, 2, 0, 13];
var sumaPares = sumaNumerosPares(arreglo);
console.log("La suma de los números pares es:", sumaPares);