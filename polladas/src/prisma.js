import prisma from "@prisma/client";
// La conexion a nuestra base de datos
// Usando el patro singleton solamente generamos una conexion para todo nuestro pr proyecto
export const Prisma = new prisma.PrismaClient();