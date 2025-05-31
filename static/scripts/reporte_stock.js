fetch("/reporte_stock/api/productos/")
  .then((response) => response.json())
  .then((productos) => {
    const contenedores = document.getElementsByClassName("contenedor-productos");

    if (contenedores.length === 0) {
      console.error("No se encontró ningún contenedor con la clase 'contenedor-productos'");
      return;
    }

    // Para este ejemplo, vamos a usar solo el primero
    const contenedor = contenedores[0];

    // Agrupar productos por nombre
    const agrupados = productos.reduce((acc, prod) => {
      if (!acc[prod.nombre]) acc[prod.nombre] = [];
      acc[prod.nombre].push(prod);
      return acc;
    }, {});

    // Crear contenido para cada grupo
    for (const nombre in agrupados) {
      const listaProductos = agrupados[nombre];

      // Título
      const titulo = document.createElement("h2");
      titulo.classList.add("titulo-producto");
      titulo.textContent = nombre;
      contenedor.appendChild(titulo);

      // Tabla
      const tabla = document.createElement("table");
      tabla.classList.add("tabla-productos");
      tabla.innerHTML = `
        <thead>
          <tr>
            <th>Categoría</th>
            <th>Precio</th>
            <th>Cantidad</th>
          </tr>
        </thead>
        <tbody>
          ${listaProductos
            .map(
              (p) => `
            <tr>
              <td>${p.categoria}</td>
              <td>${p.precio.toFixed(2)}</td>
              <td>${p.cantidad}</td>
            </tr>
          `
            )
            .join("")}
        </tbody>
      `;
      contenedor.appendChild(tabla);
    }
  })
  .catch((error) => {
    console.error("Error al cargar productos:", error);
  });
