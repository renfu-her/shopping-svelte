<script>
	import { goto } from '$app/navigation';
	import CategoryNode from './CategoryNode.svelte';

	export let categories = [];
	export let currentSlug = null;
	export let useQueryParam = false; // 是否使用查詢參數而非路徑參數

	function handleCategoryClick(event) {
		const category = event.detail;
		if (category && category.level === 3) {
			if (useQueryParam) {
				goto(`/product?category=${category.slug}`);
			} else {
				goto(`/product/${category.slug}`);
			}
		}
	}
</script>

<div class="category-tree">
	{#each categories as category}
		<CategoryNode {category} {currentSlug} on:click={handleCategoryClick} />
	{/each}
</div>

<style>
	.category-tree {
		background-color: transparent;
	}
</style>

