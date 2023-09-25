/*Tenés un arreglo de objetos llamado empleados, donde cada objeto 
representa a un empleado y tiene las propiedades "nombre" y "salario". 
Convertí el arreglo de objetos a una cadena JSON y mostrá el resultado en 
la consola.  */

var empleados = [
    {
        nombre: "Juan",
        salario: 120
    } , 
    {
        nombre: "Pepe",
        salario: 320
    },
    {
        nombre: "Rocio",
        salario: 420
    },
    {
        nombre: "Malena",
        salario: 380
    }
];

var jsonString = JSON.stringify(empleados);
console.log(jsonString);
var antijsonString = JSON.parse(jsonString);