const API_BASE = '/api';

/**
 * @param {string} endpoint
 * @param {RequestInit} [options={}]
 */
export async function fetchAPI(endpoint, options = {}) {
	const sessionId = getSessionId();
	
	const response = await fetch(`${API_BASE}${endpoint}`, {
		...options,
		headers: {
			'Content-Type': 'application/json',
			'X-Session-Id': sessionId,
			...(options.headers || {}),
		},
	});

	if (!response.ok) {
		throw new Error(`API error: ${response.statusText}`);
	}

	return response.json();
}

function getSessionId() {
	let sessionId = localStorage.getItem('session_id');
	if (!sessionId) {
		sessionId = generateSessionId();
		localStorage.setItem('session_id', sessionId);
	}
	return sessionId;
}

function generateSessionId() {
	return 'session_' + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
}

// Categories
export async function getCategories() {
	return fetchAPI('/categories');
}

// Products
export async function getProducts(page = 1, perPage = 12, categorySlug = null) {
	const params = new URLSearchParams({ page: page.toString(), per_page: perPage.toString() });
	if (categorySlug) {
		params.append('category_slug', categorySlug);
	}
	return fetchAPI(`/products?${params}`);
}

export async function getFeaturedProducts() {
	return fetchAPI('/products/featured');
}

export async function getProduct(slug) {
	return fetchAPI(`/product/${slug}`);
}

// Cart
export async function getCart() {
	return fetchAPI('/cart');
}

export async function addToCart(productId, quantity = 1) {
	return fetchAPI('/cart/items', {
		method: 'POST',
		body: JSON.stringify({ product_id: productId, quantity }),
	});
}

export async function updateCartItem(itemId, quantity) {
	return fetchAPI(`/cart/items/${itemId}`, {
		method: 'PUT',
		body: JSON.stringify({ quantity }),
	});
}

export async function deleteCartItem(itemId) {
	return fetchAPI(`/cart/items/${itemId}`, {
		method: 'DELETE',
	});
}

// Orders
export async function createOrder(shippingAddress) {
	return fetchAPI('/orders', {
		method: 'POST',
		body: JSON.stringify({ shipping_address: shippingAddress }),
	});
}

// Ads
export async function getAds() {
	return fetchAPI('/ads');
}

// News
export async function getNews() {
	return fetchAPI('/news');
}

// About
export async function getAbout() {
	return fetchAPI('/about');
}

// FAQ
export async function getFAQ() {
	return fetchAPI('/faq');
}

