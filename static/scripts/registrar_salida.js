fetch("/registrar_salida/api/productos/")
  .then((response) => response.json())
  .then((productos) => {
    const contenedor = document.getElementById("contenedor-productos");

    // Agrupar por categoría
    const agrupados = productos.reduce((acc, prod) => {
      if (!acc[prod.categoria]) acc[prod.categoria] = [];
      acc[prod.categoria].push(prod);
      return acc;
    }, {});

    // Recorrer categorías
    for (const categoria in agrupados) {
      const productosCategoria = agrupados[categoria];

      // Título de categoría
      const titulo = document.createElement("h2");
      titulo.textContent = categoria;
      titulo.classList.add("titulo-categoria");
      contenedor.appendChild(titulo);

      // Tabla
      const tabla = document.createElement("table");
      tabla.classList.add("tabla-productos");
      console.log(productosCategoria); // Verifica que cada objeto tenga id_producto

      tabla.innerHTML = `
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Precio</th>
            <th>Cantidad</th>
            <th>Contador</th>
          </tr>
        </thead>
        <tbody>
          ${productosCategoria
            .map(
              (p) => `
    <tr>
      <td>${p.nombre}</td>
      <td>${p.precio.toFixed(2)}</td>
      <td>${p.cantidad}</td>
      <td>
      <input type="number" class="contador-input" data-id="${
        p.id_producto
      }" value="0" min="0">

      </td>
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
const fechaDiv = document.getElementById("fecha-actual");

const diasSemana = [
  "domingo",
  "lunes",
  "martes",
  "miércoles",
  "jueves",
  "viernes",
  "sábado",
];
const meses = [
  "enero",
  "febrero",
  "marzo",
  "abril",
  "mayo",
  "junio",
  "julio",
  "agosto",
  "septiembre",
  "octubre",
  "noviembre",
  "diciembre",
];

const hoy = new Date();
const nombreDia = diasSemana[hoy.getDay()];
const dia = hoy.getDate();
const nombreMes = meses[hoy.getMonth()];
const anio = hoy.getFullYear();

const fechaFormateada = `${
  nombreDia.charAt(0).toUpperCase() + nombreDia.slice(1)
}, ${dia} de ${nombreMes} de ${anio}`;

fechaDiv.textContent = fechaFormateada;
document.getElementById("guardar-salida").addEventListener("click", () => {
  const contadores = document.querySelectorAll(".contador-input");

  const cantidades = [];
  const ids = [];

  contadores.forEach((input) => {
    const cantidad = parseInt(input.value) || 0;
    const id = input.dataset.id;

    cantidades.push(cantidad);
    ids.push(id);
  });

  const datos = {
    productos: ids.join(","),
    cantidad: cantidades.join(","),
  };
  console.log("Datos enviados:", datos);

  fetch("/registrar_salida/guardar/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify(datos),
  })
    .then((response) => {
      if (!response.ok) throw new Error("Error al guardar");
      return response.json();
    })
    .then((data) => {
      alert("Salida guardada correctamente.");
    })
    .catch((error) => {
      console.error("Error al guardar salida:", error);
      alert("Hubo un error al guardar la salida.");
    });
});

// Utilidad para obtener el token CSRF desde las cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
