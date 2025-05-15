function toggleEdicion(button, id) {
  const icon = button.querySelector("i");
  const nombreInput = document.getElementById(`nombre-${id}`);
  const costoInput = document.getElementById(`costo-${id}`);
  const proveedorInput = document.getElementById(`proveedor-${id}`);
  const cantidadInput = document.getElementById(`cantidad-${id}`);
  const unidadInput = document.getElementById(`unidad-${id}`);
  const categoriaInput = document.getElementById(`categoria-${id}`);
  const marcaInput = document.getElementById(`marca-${id}`);
  const llegadaInput = document.getElementById(`llegada-${id}`);
  const vencimientoInput = document.getElementById(`vencimiento-${id}`);
  const esModoEdicion = !nombreInput.disabled;

  if (!esModoEdicion) {
    // Cambiar a modo edición
    nombreInput.disabled = false;
    costoInput.disabled = false;
    proveedorInput.disabled = false;
    cantidadInput.disabled = false;
    unidadInput.disabled = false;
    categoriaInput.disabled = false;
    marcaInput.disabled = false;
    llegadaInput.disabled = false;
    vencimientoInput.disabled = false;
    icon.classList.remove("zmdi-refresh");
    icon.classList.add("zmdi-check");
  } else {
    // Guardar cambios
    const data = {
      id: id,
      nombre: nombreInput.value,
      costo: costoInput.value,
      proveedor: proveedorInput.value,
      cantidad: cantidadInput.value,
      unidad: unidadInput.value,
      categoria: categoriaInput.value,
      marca: marcaInput.value,
      llegada: llegadaInput.value,
      vencimiento: vencimientoInput.value,
      // Agrega los demás campos aquí
    };
console.log(data);
    fetch(`/inventario/actualizar/${id}/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({
        id: id,
        nombremateriaprima: document.getElementById(`nombre-${id}`).value,
        costo: document.getElementById(`costo-${id}`).value,
        proveedor: document.getElementById(`proveedor-${id}`).value,
        cantidad: document.getElementById(`cantidad-${id}`).value,
        unidadmedida: document.getElementById(`unidad-${id}`).value,
        categoria: document.getElementById(`categoria-${id}`).value,
        marca: document.getElementById(`marca-${id}`).value,
        fechallegada: document.getElementById(`llegada-${id}`).value,
        fechavencimiento: document.getElementById(`vencimiento-${id}`).value,
      }),
    }).then((res) => {
      if (res.ok) {
        alert("Cambios guardados");
        location.reload();
      } else {
        alert("Error al guardar");
      }
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
