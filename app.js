const categoryFilter = document.getElementById('categoryFilter');
    const restaurants = document.getElementById('restaurantContainer').getElementsByClassName('box');

    categoryFilter.addEventListener('change', function() {
        const selectedCategory = this.value;

        // Показываем/скрываем рестораны в зависимости от выбранной категории
        for (let i = 0; i < restaurants.length; i++) {
            const restaurantCategories = restaurants[i].getAttribute('data-categories');

            if (selectedCategory === 'all' || restaurantCategories.includes(selectedCategory)) {
                restaurants[i].style.display = 'block'; // Показываем ресторан
            } else {
                restaurants[i].style.display = 'none'; // Скрываем ресторан
            }
        }
    });