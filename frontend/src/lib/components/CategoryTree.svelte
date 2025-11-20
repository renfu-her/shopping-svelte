<script>
	import { goto } from '$app/navigation';
	import CategoryNode from './CategoryNode.svelte';

	export let categories = [];
	export let currentSlug = null;

	function handleCategoryClick(event) {
		const category = event.detail;
		if (category && category.level === 3) {
			goto(`/product/${category.slug}`);
		}
	}
</script>

<div class="category-tree">
	<h3>產品分類</h3>
	{#each categories as category}
		<CategoryNode {category} {currentSlug} on:click={handleCategoryClick} />
	{/each}
</div>

<style>
	.category-tree {
		background-color: #f9f9f9;
		padding: 1rem;
		border-radius: 8px;
	}

	.category-tree h3 {
		margin-top: 0;
		margin-bottom: 1rem;
	}
</style>

<style>
	.category-tree {
		background-color: #f9f9f9;
		padding: 1rem;
		border-radius: 8px;
	}

	.category-tree h3 {
		margin-top: 0;
		margin-bottom: 1rem;
	}

	.category-group {
		margin-bottom: 0.5rem;
	}

	.category-item {
		padding: 0.5rem;
		cursor: pointer;
		border-radius: 4px;
		transition: background-color 0.2s;
	}

	.category-item.level-1 {
		font-weight: bold;
		font-size: 1.1rem;
	}

	.category-item.level-2 {
		padding-left: 1.5rem;
		font-weight: 500;
	}

	.category-item.level-3 {
		padding-left: 2.5rem;
		color: #3498db;
	}

	.category-item.level-3:hover,
	.category-item.level-3.active {
		background-color: #e3f2fd;
	}

	.children {
		margin-left: 0.5rem;
	}
</style>

