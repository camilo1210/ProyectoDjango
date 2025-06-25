fetch("/reporte_stock/api/productos/")
  .then((response) => response.json())
  .then((productos) => {
    const contenedores = document.getElementsByClassName(
      "contenedor-productos"
    );

    if (contenedores.length === 0) {
      console.error(
        "No se encontró ningún contenedor con la clase 'contenedor-productos'"
      );
      return;
    }

    const contenedor = contenedores[0];

    const agrupados = productos.reduce((acc, prod) => {
      if (!acc[prod.nombre]) acc[prod.nombre] = [];
      acc[prod.nombre].push(prod);
      return acc;
    }, {});

    for (const nombre in agrupados) {
      const listaProductos = agrupados[nombre];

      const titulo = document.createElement("h2");
      titulo.classList.add("titulo-producto");
      titulo.textContent = nombre;
      contenedor.appendChild(titulo);

      const tabla = document.createElement("table");
      tabla.classList.add("tabla-productos");

      const cuerpo = listaProductos
        .map((p) => {
          return `
            <tr data-id="${p.id}">
              <td class="celda-categoria">${p.categoria}</td>
              <td class="celda-precio">${p.precio.toFixed(2)}</td>
              <td class="celda-cantidad">${p.cantidad}</td>
              <td>
                <button class="boton-editar zmdi zmdi-refresh"></button>
              </td>
            </tr>
          `;
        })
        .join("");

      tabla.innerHTML = `
        <thead>
          <tr>
            <th>Categoría</th>
            <th>Precio</th>
            <th>Cantidad</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>${cuerpo}</tbody>
      `;

      contenedor.appendChild(tabla);

      // Agregar funcionalidad a los botones de edición
      tabla.querySelectorAll(".boton-editar").forEach((btn) => {
        btn.addEventListener("click", () => {
          const fila = btn.closest("tr");

          const precioTd = fila.querySelector(".celda-precio");
          const cantidadTd = fila.querySelector(".celda-cantidad");

          // Detectar si ya estamos editando
          const yaEditando = btn.classList.contains("zmdi-check");

          if (!yaEditando) {
            // Inicia edición
            const precioActual = parseFloat(precioTd.textContent);
            const cantidadActual = parseInt(cantidadTd.textContent);

            precioTd.innerHTML = `<input type="number" step="0.01" value="${precioActual}">`;
            cantidadTd.innerHTML = `<input type="number" value="${cantidadActual}">`;

            btn.classList.remove("zmdi-refresh");
            btn.classList.add("zmdi-check");
          } else {
            // Guardar cambios
            const precioInput = fila.querySelector(".celda-precio input");
            const cantidadInput = fila.querySelector(".celda-cantidad input");

            const nuevoPrecio = parseFloat(precioInput?.value);
            const nuevaCantidad = parseInt(cantidadInput?.value);

            const precioSeguro = !isNaN(nuevoPrecio) ? nuevoPrecio : 0;
            const cantidadSegura = !isNaN(nuevaCantidad) ? nuevaCantidad : 0;

            const productoId = parseInt(fila.dataset.id);

            fetch("/reporte_stock/api/actualizar_producto/", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
              },
              body: JSON.stringify({
                id: productoId,
                precio: precioSeguro,
                cantidad: cantidadSegura,
              }),
            })
              .then((response) => {
                if (!response.ok) throw new Error("Error al guardar");
                return response.json();
              })
              .then((data) => {
                console.log("Guardado con éxito", data);
                location.reload();
              })
              .catch((error) => {
                console.error("Error al guardar:", error);
                alert("Hubo un error al guardar los cambios.");
              });
          }
        });
      });
    }
  })
  .catch((error) => {
    console.error("Error al cargar productos:", error);
  });

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
