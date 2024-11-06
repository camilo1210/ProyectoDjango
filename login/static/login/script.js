const container = document.querySelector(".container");
const btnSignIn = document.getElementById ("btn-sign-in");
const btnSignUp = document.getElementById ("btn-sign-up");
const fallingLeaves = document.getElementById ('falling-leaves')
btnSignIn.addEventListener("click", ()=>{
    container.classList.remove ("toggle");
})
btnSignUp.addEventListener("click", ()=>{
    container.classList.add ("toggle");

})
function createLeaf() {
    const leaf = document.createElement('div');
    leaf.className = 'leaf';

    // Posición aleatoria en la pantalla
    leaf.style.left = Math.random() * 100 + 'vw';
    
    // Duración y opacidad aleatorias para la animación de caída
    leaf.style.animationDuration = Math.random() * 5 + 4 + 's';
    leaf.style.opacity = Math.random();

    //Desplazamiento horizontal aleatorio
    const randomHorizontalOffset = (Math.random()* 200 - 100) + 'px';
    leaf.style.setProperty('--horizontal-offset',randomHorizontalOffset);

    // Agrega la hoja al contenedor de hojas que caen
    fallingLeaves.appendChild(leaf);

    // Eliminar la hoja después de que termine la animación
    leaf.addEventListener('animationend', () => {
        leaf.remove();
    });
}

// Llama a la función createLeaf cada cierto tiempo para generar más hojas
setInterval(createLeaf, 300);
