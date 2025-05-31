fetch("/reporte_caduci/api/data/")
  .then((response) => response.json())
  .then((data) => {
    const contenedor = document.getElementById("contenedor-tablas");

    for (const fecha in data) {
      const materias = data[fecha];

      const contenedorFecha = document.createElement("div");
      contenedorFecha.classList.add("reporte-caducidad"); // Contenedor estilizado

      const titulo = document.createElement("h2");
      titulo.classList.add("titulo-fecha"); // Para estilo personalizado si lo deseas
      titulo.textContent = "Fecha de Vencimiento: " + fecha;
      contenedorFecha.appendChild(titulo);

      const tabla = document.createElement("table");
      tabla.classList.add("tabla-caducidad"); // Aplica estilos CSS
      tabla.innerHTML = `
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Categoría</th>
            <th>Marca</th>
            <th>Cantidad</th>
            <th>Unidad</th>
          </tr>
        </thead>
        <tbody>
          ${materias
            .map(
              (m) => `
              <tr>
                <td>${m.nombre}</td>
                <td>${m.categoria}</td>
                <td>${m.marca}</td>
                <td>${m.cantidad}</td>
                <td>${m.unidad}</td>
              </tr>
            `
            )
            .join("")}
        </tbody>
      `;
      contenedorFecha.appendChild(tabla);
      contenedor.appendChild(contenedorFecha);
    }
  })
  .catch((error) => {
    console.error("Error al cargar los datos:", error);
  });
