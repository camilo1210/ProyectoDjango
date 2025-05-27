function toggleEdicion(button, id) {
  const icon = button.querySelector("i");
  const nombremateriaprimaInput = document.getElementById(
    `nombremateriaprima-${id}`
  );
  const costoInput = document.getElementById(`costo-${id}`);
  const proveedorInput = document.getElementById(`proveedor-${id}`);
  const cantidadInput = document.getElementById(`cantidad-${id}`);
  const unidadmedidaInput = document.getElementById(`unidadmedida-${id}`);
  const categoriaInput = document.getElementById(`categoria-${id}`);
  const marcaInput = document.getElementById(`marca-${id}`);
  const fechallegadaInput = document.getElementById(`fechallegada-${id}`);
  const fechavencimientoInput = document.getElementById(
    `fechavencimiento-${id}`
  );
  const esModoEdicion = !nombremateriaprimaInput.disabled;

  if (!esModoEdicion) {
    // Cambiar a modo edición
    nombremateriaprimaInput.disabled = false;
    costoInput.disabled = false;
    proveedorInput.disabled = false;
    cantidadInput.disabled = false;
    unidadmedidaInput.disabled = false;
    categoriaInput.disabled = false;
    marcaInput.disabled = false;
    fechallegadaInput.disabled = false;
    fechavencimientoInput.disabled = false;
    icon.classList.remove("zmdi-refresh");
    icon.classList.add("zmdi-check");
  } else {
    // Guardar cambios
    const data = {
      id: id,
      nombre: nombremateriaprimaInput.value,
      costo: costoInput.value,
      proveedor: proveedorInput.value,
      cantidad: cantidadInput.value,
      unidad: unidadmedidaInput.value,
      categoria: categoriaInput.value,
      marca: marcaInput.value,
      llegada: fechallegadaInput.value,
      vencimiento: fechavencimientoInput.value,
      // Agrega los demás campos aquí
    };
    console.log("Datos enviados:", data); // 👈 Esto es clave para depurar

    console.log(data);
    fetch(`/inventario/actualizar/${id}/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({
        id: id,
        nombremateriaprima: document.getElementById(`nombremateriaprima-${id}`)
          .value,
        costo: document.getElementById(`costo-${id}`).value,
        proveedor: document.getElementById(`proveedor-${id}`).value,
        cantidad: document.getElementById(`cantidad-${id}`).value,
        unidadmedida: document.getElementById(`unidadmedida-${id}`).value,
        categoria: document.getElementById(`categoria-${id}`).value,
        marca: document.getElementById(`marca-${id}`).value,
        fechallegada: document.getElementById(`fechallegada-${id}`).value,
        fechavencimiento: document.getElementById(`fechavencimiento-${id}`)
          .value,
      }),
    })
      .then((res) => res.json()) // 👈 Captura JSON con el error
      .then((responseData) => {
        if (responseData.success) {
          alert("Cambios guardados");
          location.reload();
        } else {
          console.error("Error en servidor:", responseData.error); // 👈 Muestra el error exacto
          alert("Error al guardar: " + responseData.error);
        }
      })
      .catch((error) => {
        console.error("Error en fetch:", error);
        alert("Error inesperado");
      });
  }
}

// Obtener el CSRF token
function getCookie(name) {
  const cookieValue = document.cookie
    .split("; ")
    .find((row) => row.startsWith(name + "="));
  return cookieValue ? decodeURIComponent(cookieValue.split("=")[1]) : null;
}
