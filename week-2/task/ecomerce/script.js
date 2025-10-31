const products = [
  { id: 1, name: "laptop", price: 3000, category: "electronics", img: "/asserts/ele-1.jpg" },
  { id: 2, name: "headphones", price: 1500, category: "electronics", img: "/asserts/ele-2.jpg" },
  { id: 3, name: "speakers", price: 5000, category: "electronics", img: "/asserts/ele-3.jpg" },
  { id: 4, name: "Book 1", price: 4000, category: "books", img: "/asserts/book-1.webp" },
  { id: 5, name: "Book 2", price: 3500, category: "books", img: "/asserts/book-2.webp" },
  { id: 6, name: "Book 3", price: 6000, category: "books", img: "/asserts/book-3.png" },
  { id: 7, name: "jackets 1", price: 1200, category: "clothing", img: "/asserts/cloth_1.jpg" },
  { id: 8, name: "jacket 2", price: 4500, category: "clothing", img: "/asserts/cloth_2.jpg" },
  { id: 9, name: "jacket 3", price: 4500, category: "clothing", img: "/asserts/cloth_3.jpg" },
  { id: 10, name: "Engine Oil", price: 4500, category: "automobile", img: "/asserts/auto_1.jpg" },
  { id: 11, name: "Tool Set", price: 4500, category: "automobile", img: "/asserts/auto_2.jpg" },
  { id: 12, name: "Gear Set", price: 4500, category: "automobile", img: "/asserts/auto_3.jpg" },
];

let cart = JSON.parse(localStorage.getItem("cart")) || [];

function saveCart() {
  localStorage.setItem("cart", JSON.stringify(cart));
}

const product_container = document.getElementById("product_containers");
const cart_container = document.getElementById("cart_container");

function renderProducts(list) {
  if (!product_container) return;
  product_container.innerHTML = "";
  if (list.length === 0) {
    product_container.innerHTML = `<div class="text-center text-danger py-5">No products found</div>`
    return
  }
  list.forEach(product => {
    product_container.innerHTML += `
      <div class="col-md-3 mb-4">
      <a herf="/product.html">
        <div class="card">
          <img src="${product.img}" class="card-img-top " height="200" alt="${product.name}">
          <div class="card-body text-center">
            <h5 class="card-title">${product.name}</h5>
            <p class="card-text text-success">₹${product.price}</p>
          </div>
          <div class="card-footer p-0 text-center d-flex flex-row align-items-center ">
            <button class="btn btn-success w-75 m-1" onclick="viewProduct(${product.id})">View</button>
            <button class="btn btn-primary w-75 m-1" onclick="addToCart(${product.id})">Add</button>
          </div>
        </div>
        </a>
      </div>
    `;
  });
}

function viewProduct(id) {
  const product = products.find(p => p.id === id);
  localStorage.setItem("viewProduct", JSON.stringify(product));
  window.location.href = "/product.html";
}
function renderProduct() {
  const product = JSON.parse(localStorage.getItem("viewProduct"));
  product_display = document.getElementById("product_display");
  product_display.innerHTML = `
    <div class="row h-100">
      <div class="col-md-6">
        <img src="${product.img}" class="img img-fluid h-75" alt="${product.name}">
      </div>
      <div class="col-md-6">
        <p class="text-muted">
            <span id="info" class="text-success"></span>
            <span id="error" class="text-danger"></span>
        </p>
        <h2>${product.name}</h2>
        <p class="text-success h4">₹${product.price}</p>
        <p class="card-text"></p>
          <span class="fw-bold">Category:</span> <span id="product_category">${product.category}</span>
        </p>
        <input type="hidden" id="product_id" value="${product.id}">
        <button class="btn btn-primary add_to_cart">Add to Cart</button>
      </div>
    </div>
  `;
  const add = document.querySelectorAll('.add_to_cart');
  add.forEach(button => {
    button.addEventListener('click', () => {
      addToCart(product.id);
    });
  });
}

function renderCart() {
  if (!cart_container) {
    return;
  }
  cart_container.innerHTML = "";
  if (cart.length === 0) {
    cart_container.innerHTML = "<p class='text-center text-danger py-5'>Your cart is empty</p>";
    return;
  }
  cart.forEach(item => {
    cart_container.innerHTML += `
      <div class="col-md-12 px-3">
        <div class=" d-flex flex-row align-items-center gap-3">
          <img src="${item.img}" class="img img-fluid" width="100" alt="${item.name}">
          <div class="card-body">
            <h5 class="card-title">${item.name}</h5>
            <p class="card-text">₹${item.price}</p>
          </div>
          <div class="text-center">
            <button class="btn btn-danger w-100" onclick="removeFromCart(${item.id})">Remove</button>
          </div>
        </div>
        <hr>
      </div>
    `;
  });
}

function addToCart(id) {
  const product = products.find(p => p.id === id);
  const info = document.getElementById("info");
  const error = document.getElementById("error");
  if (!cart.find(item => item.id === id)) {
    cart.push(product);
    if (info) {
      info.innerText = `${product.name} added to cart`;
      error.innerText = "";
    }
  } else {
    if (error) {
      error.innerText = `${product.name} is already in the cart`;
      info.innerText = "";
    }
  }
  saveCart();
  updateCartTotal();
  renderCart();
}

function removeFromCart(id) {
  const info = document.getElementById("info");
  cart = cart.filter(item => item.id !== id);

  info.innerText = "Item removed from cart";
  saveCart();
  updateCartTotal();
  renderCart();
}

function clearCart() {
  const info = document.getElementById("info");
  cart = [];
  info.innerText = "Cart cleared";
  // info.innerText = "";
  saveCart();
  updateCartTotal();
  renderCart();
}

function updateCartTotal() {
  const total = cart.reduce((sum, item) => sum + item.price, 0);
  const t = document.getElementById("cart-total");
  const c = document.getElementById("cart-count");
  if (t) {
    t.innerText = total;
  }
  if (c) {
    c.innerText = cart.length;
  }
}

const categorySelect = document.getElementById("categoryFilter");
if (categorySelect) {
  categorySelect.addEventListener("change", (e) => {
    const category = e.target.value;
    // console.log(category);
    if (category === "all") {
      renderProducts(products);
    } else {
      const filtered = products.filter(p => p.category === category);
      renderProducts(filtered);
    }
  });
}

function confirmOrder() {
  const info = document.getElementById("info");
  const error = document.getElementById("error");
  if (cart.length === 0) {
    info.innerText = "Your cart is empty";
    error.innerText = "";
    return;
  } else {
    error.innerText = "Order placed successfully";
    info.innerText = "";
    cart = [];
    saveCart();
    updateCartTotal();
    renderCart();
  }
}

$(document).ready(function () {
  $('#categoryFilter').select2({
    placeholder: 'Select a category',
    allowClear: true,
    width: '100%',
    theme: 'classic',
    maximunSelectionLength: 4,
    tags: true
  });

  $('#categoryFilter').on('change', function () {
    const selected = $(this).val();
    if (!selected || selected.includes('all')) {
      renderProducts(products);
    } else {
      const filtered = products.filter(p => selected.includes(p.category.toLowerCase()));
      renderProducts(filtered);
    }
  });
});

renderProducts(products);
renderCart();
updateCartTotal();
renderProduct();