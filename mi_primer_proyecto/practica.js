// import isodd from "is-odd";
// Froma de importar librerias, y funcionalidades de otros archivos usando el formato CommonJs
// https://nodejs.org/api/esm.html

// import isodd from require("is-odd");
const isodd = require("is-odd")
const informacion = require("./info-adicional");

const esPar = isodd(15);

console.log("hola");
console.log(esPar);

// ahora utilizamos lo que hemos exportado desde el otro archivo
console.log(informacion.edad);
const saludo  = informacion.saludar("Rigoberto");
console.log(saludo);