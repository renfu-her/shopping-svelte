import { writable } from 'svelte/store';
import { getCart, addToCart as addToCartAPI, updateCartItem, deleteCartItem } from '../api.js';

function createCartStore() {
	const { subscribe, set, update } = writable({
		items: [],
		total_amount: 0,
		loading: false,
	});

	return {
		subscribe,
		load: async () => {
			update(state => ({ ...state, loading: true }));
			try {
				const cart = await getCart();
				set({ ...cart, loading: false });
			} catch (error) {
				console.error('Failed to load cart:', error);
				update(state => ({ ...state, loading: false }));
			}
		},
		addItem: async (productId, quantity = 1) => {
			try {
				await addToCartAPI(productId, quantity);
				await cartStore.load();
			} catch (error) {
				console.error('Failed to add item:', error);
			}
		},
		updateItem: async (itemId, quantity) => {
			try {
				await updateCartItem(itemId, quantity);
				await cartStore.load();
			} catch (error) {
				console.error('Failed to update item:', error);
			}
		},
		removeItem: async (itemId) => {
			try {
				await deleteCartItem(itemId);
				await cartStore.load();
			} catch (error) {
				console.error('Failed to remove item:', error);
			}
		},
	};
}

export const cartStore = createCartStore();

