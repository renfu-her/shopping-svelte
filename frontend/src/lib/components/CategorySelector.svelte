<script>
	import { createEventDispatcher } from 'svelte';

	export let categories = [];
	let selectedLevel1 = null;
	let selectedLevel2 = null;
	let selectedLevel3 = null;

	const dispatch = createEventDispatcher();

	$: level2Categories = selectedLevel1 ? selectedLevel1.children || [] : [];
	$: level3Categories = selectedLevel2 ? selectedLevel2.children || [] : [];

	function handleLevel1Change() {
		selectedLevel2 = null;
		selectedLevel3 = null;
	}

	function handleLevel2Change() {
		selectedLevel3 = null;
	}

	function handleLevel3Change() {
		if (selectedLevel3) {
			dispatch('select', selectedLevel3);
		}
	}
</script>

<div class="category-selector">
	<select bind:value={selectedLevel1} on:change={handleLevel1Change}>
		<option value={null}>選擇第一層分類</option>
		{#each categories as category}
			<option value={category}>{category.name}</option>
		{/each}
	</select>

	{#if selectedLevel1 && level2Categories.length > 0}
		<select bind:value={selectedLevel2} on:change={handleLevel2Change}>
			<option value={null}>選擇第二層分類</option>
			{#each level2Categories as category}
				<option value={category}>{category.name}</option>
			{/each}
		</select>
	{/if}

	{#if selectedLevel2 && level3Categories.length > 0}
		<select bind:value={selectedLevel3} on:change={handleLevel3Change}>
			<option value={null}>選擇第三層分類</option>
			{#each level3Categories as category}
				<option value={category}>{category.name}</option>
			{/each}
		</select>
	{/if}
</div>

<style>
	.category-selector {
		display: flex;
		gap: 1rem;
		margin: 1rem 0;
	}

	select {
		padding: 0.5rem 1rem;
		font-size: 1rem;
		border: 1px solid #ccc;
		border-radius: 4px;
		min-width: 200px;
	}
</style>

