<script>
	import { createEventDispatcher } from 'svelte';
	import CategoryNode from './CategoryNode.svelte';

	export let category;
	export let currentSlug = null;

	const dispatch = createEventDispatcher();

	function handleClick() {
		if (category.level === 3) {
			dispatch('click', category);
		}
	}
</script>

<div class="category-group">
	<div
		class="category-item level-{category.level}"
		class:active={category.slug === currentSlug}
		class:clickable={category.level === 3}
		on:click={handleClick}
		on:keydown={(e) => category.level === 3 && (e.key === 'Enter' || e.key === ' ') && handleClick()}
		role={category.level === 3 ? 'button' : 'presentation'}
		tabindex={category.level === 3 ? 0 : -1}
	>
		{category.name}
	</div>
	{#if category.children && category.children.length > 0}
		<div class="children">
			{#each category.children as child}
				<CategoryNode category={child} {currentSlug} on:click={(e) => dispatch('click', e.detail)} />
			{/each}
		</div>
	{/if}
</div>

<style>
	.category-group {
		margin-bottom: 0.5rem;
	}

	.category-item {
		padding: 0.5rem;
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

	.category-item.clickable {
		cursor: pointer;
	}

	.category-item.level-3:hover,
	.category-item.level-3.active {
		background-color: #e3f2fd;
	}

	.children {
		margin-left: 0.5rem;
	}
</style>

