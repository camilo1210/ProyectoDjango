document.addEventListener("DOMContentLoaded", () => {
  fetch("/reporte_tende/productos_mas_fabricados/")
    .then((response) => {
      if (!response.ok) throw new Error("Error al obtener los datos");
      return response.json();
    })
    .then((data) => {
      const contenedor = document.getElementById("lista-productos");

      if (data.length === 0) {
        contenedor.innerHTML = "<p>No hay productos fabricados aún.</p>";
        return;
      }

      // Crear encabezados
      const encabezado = document.createElement("div");
      encabezado.classList.add("fila", "encabezado");
      encabezado.innerHTML = `
        <div class="columna">Nombre</div>
        <div class="columna">Categoría</div>
        <div class="columna">Precio</div>
        <div class="columna">Stock</div>
        <div class="columna">Total fabricado</div>
      `;
      contenedor.appendChild(encabezado);
    console.log(data);
      // Crear filas para cada producto
      data.productos.forEach((producto) => {
        const fila = document.createElement("div");
        fila.classList.add("fila");
        fila.innerHTML = `
          <div class="columna">${producto.nombre}</div>
          <div class="columna">${producto.categoria}</div>
          <div class="columna">$${producto.precio}</div>
          <div class="columna">${producto.stock}</div>
          <div class="columna">${producto.total_fabricado}</div>
        `;
        contenedor.appendChild(fila);
      });
    })
    .catch((error) => {
      console.error("Error:", error);
      document.getElementById("lista-productos").innerHTML =
        "<p>Error al cargar los productos.</p>";
    });
});
