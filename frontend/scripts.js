const productListElement = document.getElementById('productList');
const searchInputElement = document.getElementById('searchInput');
let products = [];


async function fetchProducts() {
    try {
        const response = await fetch('http://localhost:8000/products');
        if (!response.ok) {
            throw new Error('Failed to fetch products');
        }
        products = await response.json(); 
    } catch (error) {
        console.error(error);
        products = []; 
    }
}


async function displayProducts(filteredProducts = []) {
    const productsToDisplay = filteredProducts.length > 0 ? filteredProducts : products;
    productListElement.innerHTML = '';
    productsToDisplay.forEach(product => {
        const productElement = document.createElement('div');
        productElement.innerHTML = `
            <p><strong>Name:</strong> ${product.name}</p>
            <p><strong>Category:</strong> ${product.category}</p>
            <p><strong>Price:</strong> $${product.price}</p>
            <p><strong>Description:</strong> ${product.description}</p>
            <hr>
        `;
        productListElement.appendChild(productElement);
    });
}


function searchProducts() {
    const searchTerm = searchInputElement.value.toLowerCase();
    const filteredProducts = products.filter(product =>
        product.name.toLowerCase().includes(searchTerm) ||
        product.category.toLowerCase().includes(searchTerm)
    );
    displayProducts(filteredProducts);
}


searchInputElement.addEventListener('input', searchProducts);


fetchProducts().then(() => displayProducts());
