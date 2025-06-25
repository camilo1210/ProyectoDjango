document.addEventListener("DOMContentLoaded", function () {
  const formularioProducto = document.getElementById("recuadro-ingreso");
  const entradaNombre = document.getElementById("campo-nombre");
  const entradaCategoria = document.getElementById("campo-categoria");
  const entradaPrecio = document.getElementById("campo-precio");
  const entradaCantidad = document.getElementById("campo-cantidad");
  const botonGuardar = document.getElementById("control-envio");

  botonGuardar.addEventListener("click", function (evento) {
    evento.preventDefault();

    const datosProducto = {
      nombre: entradaNombre.value.trim(),
      categoria: entradaCategoria.value.trim(),
      precio: parseFloat(entradaPrecio.value),
      cantidad: parseInt(entradaCantidad.value),
    };

    fetch("/reporte_stock/api/crear_producto/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(datosProducto),
    })
      .then((respuesta) => {
        if (!respuesta.ok) {
          throw new Error("Error en la solicitud");
        }
        return respuesta.json();
      })
      .then((datos) => {
        if (datos.exito) {
          alert("✅ Producto guardado correctamente");
          const formulario = document.getElementById("formulario-producto");
          if (formulario) {
            formulario.reset(); // ✅ Solo se ejecuta si existe
          }
        } else {
          alert("⚠️ Error: " + datos.mensaje);
        }
      })
      .catch((error) => {
        alert("❌ Error al enviar: " + error.message);
      });
  });
});
