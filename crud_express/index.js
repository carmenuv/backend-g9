import express, { json } from "express";

const servidor = express();

// use > sirve para agregar un middleware que validará la información dependiendo el orden en el que lo coloquemos
// llegue información en formato JSON este middleware lo pueda cnovertir en una información legible yl o almacene en el req.body
servidor.use(json());

const productos = [
  {
    nombre: 'pollada',
    precio: 15.50,
    disponible: true,
  },
  {
    nombre: 'adobada',
    precio: 15.5,
    disponible: true,
  },
  {
    nombre: 'chicharronada',
    precio: 17.5,
    disponible: true,
  },
  {
    nombre: 'chuleteada',
    precio: 12.5,
    disponible: false,
  }
]

servidor.get("/", (req, res) => {
  console.log("Entro aquí");

  res.status(200).json({
    "mensaje": "Bienvenido a mi API de express",
  });
});

servidor.route('/productos')
.get((req, res)=>{
  // devuelve todos los productos
  const productoDisponibles = productos.filter((producto) => producto.disponible === true );

  res.status(200).json({
    content: productoDisponibles,
  });
})
.post((req, res)=>{
  console.log(req.body);
  const data = req.body;

  productos.push(data);

  res.status(201).json({
    message: "Producto creado exitosamente",
  });
});


servidor.listen(5000, ()=>{
  console.log(`Servidor corriendo exitosamente en el puerto 5000`)
})