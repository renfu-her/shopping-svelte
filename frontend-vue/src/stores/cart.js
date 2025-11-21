import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { getCart, addToCart as addToCartAPI, updateCartItem, deleteCartItem } from '@/services/api.js';

export const useCartStore = defineStore('cart', () => {
	const items = ref([]);
	const total_amount = ref(0);
	const loading = ref(false);

	const itemCount = computed(() => {
		return items.value.reduce((sum, item) => sum + item.quantity, 0);
	});

	async function load() {
		loading.value = true;
		try {
			const cart = await getCart();
			items.value = cart.items || [];
			total_amount.value = cart.total_amount || 0;
		} catch (error) {
			console.error('Failed to load cart:', error);
		} finally {
			loading.value = false;
		}
	}

	async function addItem(productId, quantity = 1) {
		try {
			await addToCartAPI(productId, quantity);
			await load();
		} catch (error) {
			console.error('Failed to add item:', error);
			throw error;
		}
	}

	async function updateItem(itemId, quantity) {
		try {
			await updateCartItem(itemId, quantity);
			await load();
		} catch (error) {
			console.error('Failed to update item:', error);
			throw error;
		}
	}

	async function removeItem(itemId) {
		try {
			await deleteCartItem(itemId);
			await load();
		} catch (error) {
			console.error('Failed to remove item:', error);
			throw error;
		}
	}

	return {
		items,
		total_amount,
		loading,
		itemCount,
		load,
		addItem,
		updateItem,
		removeItem
	};
});

