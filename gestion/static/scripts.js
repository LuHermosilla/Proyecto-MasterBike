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

let productos = [];
let proveedores = [
    { id: 1, nombre: 'Proveedor 1', telefono: '123456789' },
    { id: 2, nombre: 'Proveedor 2', telefono: '987654321' }
];

document.addEventListener('DOMContentLoaded', function() {
    loadProveedores();
    loadProductos();
    document.getElementById('productForm').addEventListener('submit', saveProduct);
});

function loadProveedores() {
    let proveedorSelect = document.getElementById('id_proveedor');
    proveedorSelect.innerHTML = '';
    proveedores.forEach(proveedor => {
        let option = document.createElement('option');
        option.value = proveedor.id;
        option.text = proveedor.nombre;
        proveedorSelect.add(option);
    });
}

function loadProductos() {
    let productTable = document.getElementById('productTable');
    productTable.innerHTML = '';
    productos.sort((a, b) => a.nombre.localeCompare(b.nombre));
    productos.forEach(producto => {
        let row = document.createElement('tr');
        row.innerHTML = `
            <td>${producto.nombre}</td>
            <td>${producto.categoria}</td>
            <td>${producto.precio_unitario}</td>
            <td>${producto.impuesto}</td>
            <td>${producto.stock_actual}</td>
            <td>${proveedores.find(p => p.id == producto.id_proveedor).nombre}</td>
            <td>${proveedores.find(p => p.id == producto.id_proveedor).telefono}</td>
            <td>
                <button class="btn btn-warning btn-sm" onclick="editProduct(${producto.id_producto})">Editar</button>
                <button class="btn btn-danger btn-sm" onclick="deleteProduct(${producto.id_producto})">Eliminar</button>
            </td>
        `;
        productTable.appendChild(row);
    });
}

function saveProduct(event) {
    event.preventDefault();
    let id_producto = document.getElementById('id_producto').value;
    let nombre = document.getElementById('nombre').value;
    let categoria = document.getElementById('categoria').value;
    let precio_unitario = document.getElementById('precio_unitario').value;
    let impuesto = document.getElementById('impuesto').value;
    let stock_actual = document.getElementById('stock_actual').value;
    let id_proveedor = document.getElementById('id_proveedor').value;

    if (id_producto) {
        let producto = productos.find(p => p.id_producto == id_producto);
        producto.nombre = nombre;
        producto.categoria = categoria;
        producto.precio_unitario = precio_unitario;
        producto.impuesto = impuesto;
        producto.stock_actual = stock_actual;
        producto.id_proveedor = id_proveedor;
    } else {
        let newProduct = {
            id_producto: Date.now(),
            nombre: nombre,
            categoria: categoria,
            precio_unitario: precio_unitario,
            impuesto: impuesto,
            stock_actual: stock_actual,
            id_proveedor: id_proveedor
        };
        productos.push(newProduct);
    }

    resetForm();
    loadProductos();
}

function editProduct(id_producto) {
    let producto = productos.find(p => p.id_producto == id_producto);
    document.getElementById('id_producto').value = producto.id_producto;
    document.getElementById('nombre').value = producto.nombre;
    document.getElementById('categoria').value = producto.categoria;
    document.getElementById('precio_unitario').value = producto.precio_unitario;
    document.getElementById('impuesto').value = producto.impuesto;
    document.getElementById('stock_actual').value = producto.stock_actual;
    document.getElementById('id_proveedor').value = producto.id_proveedor;
}

function deleteProduct(id_producto) {
    productos = productos.filter(p => p.id_producto != id_producto);
    loadProductos();
}

function resetForm() {
    document.getElementById('id_producto').value = '';
    document.getElementById('nombre').value = '';
    document.getElementById('categoria').value = 'Bicicleta';
    document.getElementById('precio_unitario').value = '';
    document.getElementById('impuesto').value = '';
    document.getElementById('stock_actual').value = '';
    document.getElementById('id_proveedor').value = '';
}
