function modifyQuantity(productId, amount) {
    let quantityInput = document.getElementById('quantity_' + productId);
    let quantity = parseInt(quantityInput.value) + amount;
    if (quantity < 1) quantity = 1;
    quantityInput.value = quantity;
    // Actualizar el valor total si es necesario
}

function addToCart(productId) {
    let quantity = parseInt(document.getElementById('quantity_' + productId).value);
    // Añadir lógica para agregar al carrito
    alert(productId + ' agregado al carrito con cantidad ' + quantity);
}

function checkout() {
    // Lógica para realizar el pago mediante la API
    alert('Realizando pago...');
}

var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
        rotate: 15,
        strech: 0,
        depth: 300,
        modifier: 1,
        slideShadows: true,
    },
    loop: true,
});