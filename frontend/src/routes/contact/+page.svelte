<script>
	let formData = {
		name: '',
		email: '',
		subject: '',
		message: ''
	};
	let submitted = false;

	function handleSubmit() {
		submitted = true;
		alert('感謝您的留言，我們會盡快回覆！');
	}
</script>

<svelte:head>
	<title>聯絡我們 - Shopwise</title>
</svelte:head>

<div class="contact-page">
	<div class="container">
		<div class="breadcrumb">
			<a href="/">首頁</a>
			<span> > </span>
			<span>聯絡我們</span>
		</div>

		<h1>聯絡我們</h1>

		<div class="contact-content">
			<div class="contact-info">
				<h2>聯絡資訊</h2>
				<div class="info-item">
					<strong>電話：</strong>
					<span>123-456-7890</span>
				</div>
				<div class="info-item">
					<strong>Email：</strong>
					<span>info@shopwise.com</span>
				</div>
				<div class="info-item">
					<strong>地址：</strong>
					<span>台北市信義區信義路五段7號</span>
				</div>
				<div class="info-item">
					<strong>營業時間：</strong>
					<span>週一至週五 9:00 - 18:00</span>
				</div>
			</div>

			<div class="contact-form-section">
				<h2>留言給我們</h2>
				<form on:submit|preventDefault={handleSubmit}>
					<div class="form-group">
						<label for="name">姓名 *</label>
						<input type="text" id="name" bind:value={formData.name} required />
					</div>
					<div class="form-group">
						<label for="email">Email *</label>
						<input type="email" id="email" bind:value={formData.email} required />
					</div>
					<div class="form-group">
						<label for="subject">主旨 *</label>
						<input type="text" id="subject" bind:value={formData.subject} required />
					</div>
					<div class="form-group">
						<label for="message">訊息 *</label>
						<textarea id="message" bind:value={formData.message} rows="6" required></textarea>
					</div>
					<button type="submit" class="submit-btn">送出</button>
				</form>
			</div>
		</div>
	</div>
</div>

<style>
	.contact-page {
		background-color: #f8f8f8;
		min-height: calc(100vh - 300px);
		padding: 2rem 0;
	}

	.container {
		max-width: 1200px;
		margin: 0 auto;
		padding: 0 2rem;
	}

	.breadcrumb {
		margin-bottom: 1rem;
		color: #666;
	}

	.breadcrumb a {
		color: #e74c3c;
		text-decoration: none;
	}

	h1 {
		margin-bottom: 2rem;
		font-size: 2rem;
	}

	.contact-content {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 3rem;
	}

	.contact-info,
	.contact-form-section {
		background-color: white;
		padding: 2rem;
		border-radius: 8px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	h2 {
		margin-top: 0;
		margin-bottom: 1.5rem;
		font-size: 1.5rem;
		border-bottom: 2px solid #e74c3c;
		padding-bottom: 0.5rem;
	}

	.info-item {
		margin-bottom: 1.5rem;
		line-height: 1.8;
	}

	.info-item strong {
		display: inline-block;
		min-width: 100px;
		color: #333;
	}

	.form-group {
		margin-bottom: 1.5rem;
	}

	.form-group label {
		display: block;
		margin-bottom: 0.5rem;
		font-weight: 500;
	}

	.form-group input,
	.form-group textarea {
		width: 100%;
		padding: 0.75rem;
		border: 1px solid #ddd;
		border-radius: 4px;
		font-family: inherit;
		font-size: 1rem;
	}

	.form-group textarea {
		resize: vertical;
	}

	.submit-btn {
		width: 100%;
		padding: 1rem 2rem;
		background-color: #e74c3c;
		color: white;
		border: none;
		border-radius: 4px;
		font-size: 1.1rem;
		font-weight: bold;
		cursor: pointer;
		transition: background-color 0.2s;
	}

	.submit-btn:hover {
		background-color: #c0392b;
	}

	@media (max-width: 768px) {
		.contact-content {
			grid-template-columns: 1fr;
		}
	}
</style>

