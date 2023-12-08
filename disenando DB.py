#disenando Db

CREATE TABLE Categoria (
    id INT PRIMARY KEY,
    nombre VARCHAR(255)
    id INTEGER PRIMARY KEY,
    nombre TEXT
);

CREATE TABLE Producto (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    marca VARCHAR(255),
    categoria_id INT,
    precio_unitario DECIMAL(10, 2),
   );

CREATE TABLE Sucursal (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    direccion VARCHAR(255),
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    direccion TEXT,
);

CREATE TABLE Stock (
    id INT PRIMARY KEY,
    sucursal_id INT,
    producto_id INT,
    cantidad INT,
    UNIQUE KEY unique_stock (sucursal_id, producto_id),
    id INTEGER PRIMARY KEY,
    sucursal_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    UNIQUE (sucursal_id, producto_id),
    
);

CREATE TABLE Cliente (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    telefono VARCHAR(20)
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    telefono TEXT,
);

CREATE TABLE Orden (
    id INT PRIMARY KEY,
    cliente_id INT,
    sucursal_id INT,
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    sucursal_id INTEGER,
    fecha DATE,
     total DECIMAL(10, 2),
     total NUMERIC(10, 2),
     );

CREATE TABLE Item (
    id INT PRIMARY KEY,
    orden_id INT,
    producto_id INT,
    cantidad INT,
    monto_venta NUMERIC(10, 2),
    
);
    
