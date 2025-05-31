document.addEventListener("DOMContentLoaded", () => {
  // Header
  const headerContainer = document.getElementById("header");
  const today = new Date();
  const options = { day: "2-digit", month: "long", year: "numeric" };
  const formattedDate = today.toLocaleDateString("es-ES", options);
  headerContainer.innerHTML = `
    <h1 style="text-align: center;">Pan y Arte</h1>
    <p style="text-align: center; font-weight: bold;">Fecha: ${formattedDate}</p>
    <hr>
  `;

  // Proveedores
  fetch("/reporte_provee/api/proveedores/")
    .then((response) => response.json())
    .then((data) => {
      console.log("Datos recibidos:", data);
      const container = document.getElementById("proveedores-container");

      data.forEach((proveedor) => {
        const card = document.createElement("div");
        card.classList.add("card-proveedor");

        card.innerHTML = `
        <h2 class="titulo-proveedor">Proveedor: ${proveedor.nombre}</h2>
        <p><strong>ID:</strong> ${proveedor.id}</p>
        <p><strong>Dirección:</strong> ${proveedor.direccion}</p>
        <p><strong>Teléfono:</strong> ${proveedor.telefono}</p>
        <div id="materias-${proveedor.id}" class="contenedor-materias"></div>
        <hr>
      `;
        container.appendChild(card);

        fetch(`/reporte_provee/api/proveedor/${proveedor.id}/materias/`)
          .then((response) => response.json())
          .then((materias) => {
            const materiasDiv = document.getElementById(
              `materias-${proveedor.id}`
            );
            if (materias.length === 0) {
              materiasDiv.innerHTML =
                "<p class='sin-materias'>No hay materias primas registradas para este proveedor.</p>";
            } else {
              let tablaHTML = `
              <table class="tabla-materias">
                <thead>
                  <tr>
                    <th>Nombre</th>
                    <th>Costo</th>
                    <th>Cantidad</th>
                    <th>Unidad</th>
                    <th>Categoría</th>
                    <th>Marca</th>
                    <th>Fecha Llegada</th>
                    <th>Fecha Vencimiento</th>
                  </tr>
                </thead>
                <tbody>
            `;
              materias.forEach((m) => {
                tablaHTML += `
                <tr>
                  <td>${m.nombre}</td>
                  <td>${m.costo}</td>
                  <td>${m.cantidad}</td>
                  <td>${m.unidadMedida}</td>
                  <td>${m.categoria}</td>
                  <td>${m.marca}</td>
                  <td>${m.fechaLlegada}</td>
                  <td>${m.fechaVencimiento}</td>
                </tr>
              `;
              });
              tablaHTML += "</tbody></table>";
              materiasDiv.innerHTML = tablaHTML;
            }
          })
          .catch((error) => {
            console.error("Error cargando materias primas:", error);
            const materiasDiv = document.getElementById(
              `materias-${proveedor.id}`
            );
            materiasDiv.innerHTML =
              '<p class="error-carga">Error cargando materias primas.</p>';
          });
      });
    })
    .catch((error) => {
      console.error("Error cargando proveedores:", error);
    });
});
