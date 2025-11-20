<script>
	import { onMount, onDestroy } from 'svelte';

	export let ads = [];
	let currentIndex = 0;
	let intervalId;

	onMount(() => {
		if (ads.length > 1) {
			intervalId = setInterval(() => {
				currentIndex = (currentIndex + 1) % ads.length;
			}, 5000);
		}
	});

	onDestroy(() => {
		if (intervalId) {
			clearInterval(intervalId);
		}
	});

	function goToSlide(index) {
		currentIndex = index;
		if (intervalId) {
			clearInterval(intervalId);
		}
		if (ads.length > 1) {
			intervalId = setInterval(() => {
				currentIndex = (currentIndex + 1) % ads.length;
			}, 5000);
		}
	}
</script>

<div class="banner-carousel">
	<div class="slides">
		{#each ads as ad, index}
			<div class="slide" class:active={index === currentIndex}>
				{#if ad.link_url}
					<a href={ad.link_url}>
						<img src={ad.image_url} alt={ad.title} />
					</a>
				{:else}
					<img src={ad.image_url} alt={ad.title} />
				{/if}
			</div>
		{/each}
	</div>

	{#if ads.length > 1}
		<div class="indicators">
			{#each ads as _, index}
				<button
					class="indicator"
					class:active={index === currentIndex}
					on:click={() => goToSlide(index)}
					aria-label="Go to slide {index + 1}"
				></button>
			{/each}
		</div>
	{/if}
</div>

<style>
	.banner-carousel {
		position: relative;
		width: 100%;
		height: 400px;
		overflow: hidden;
		margin-bottom: 2rem;
	}

	.slides {
		position: relative;
		width: 100%;
		height: 100%;
	}

	.slide {
		position: absolute;
		width: 100%;
		height: 100%;
		opacity: 0;
		transition: opacity 0.5s ease-in-out;
	}

	.slide.active {
		opacity: 1;
	}

	.slide img {
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	.slide a {
		display: block;
		width: 100%;
		height: 100%;
	}

	.indicators {
		position: absolute;
		bottom: 1rem;
		left: 50%;
		transform: translateX(-50%);
		display: flex;
		gap: 0.5rem;
	}

	.indicator {
		width: 12px;
		height: 12px;
		border-radius: 50%;
		border: 2px solid white;
		background-color: transparent;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	.indicator.active {
		background-color: white;
	}
</style>

