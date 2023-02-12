loginVelvetBtn = "//button[text()='Войти в аккаунт']"
processOrderBtn = "//button[text()='Оформить заказ']"
constructorTitle = "//h1[text()='Соберите бургер']"

# для выбора табов
tabToppings = "//span[text()='Начинки']"
tabSauces = "//span[text()='Соусы']"
tabBreads = "//span[text()='Булки']"

# для проверки выбранности табов
selectedBreads = "//div[contains(@class, 'current') and child::span[text()='Булки']]"
selectedSauces = "//div[contains(@class, 'current') and child::span[text()='Соусы']]"
selectedToppings = "//div[contains(@class, 'current') and child::span[text()='Начинки']]"