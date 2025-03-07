### Bug #1 Не открывается пользовательское меню из каталога

**Приоритет**: high

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com

**Ожидание:**
На любой странице доски объявления при нажатии на картинку профиля сверху слева ожидается что откроется выпадающее меню или список.

**Фактически:**
Меню или список не открывается.

Данная ошибка была замечена по тегу aria-haspopup="menu" и id="menu-button-:r2:" самой кнопки пользователя.

### Bug #2 Отстутсвует подтверждение после создания объявления

**Приоритет**: medium

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com

**Шаги**
1. Открыть страницу
2. Нажать на кнопку "Создать"
3. Ввести валидные данные
4. Нажать на кнопку "Сохранить"

**Ожидание:**
После создания объявления всплывает подтверждающее окно или переход на страницу с объявлением.

**Фактически:**
Оповещение или перенаправление не происходит.

### Bug #3 Плохо читаются элементы на узких устройствах в каталоге

**Приоритет**: low

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197
- Ширина страницы 1085 или меньше

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com
Кнопки: "Предыдущая", "Следующая", "Создать"

**Ожидание:**
Надписи на кнопках будут читаться без "вылетания" за границы самой кнопки.

**Фактически:**
Надписи на кнопках выходят за их границы из-за чего становятся неудобочитаемыми.

### Bug #4 Плохо читаются элементы на узких устройствах в каталоге

**Приоритет**: low

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197
- Ширина страницы с 850 дор 768, а также с 596 до 479

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com

**Ожидание:**
Карточки будут идти ровно в своих границах.

**Фактически:**
Карточки объявлений с уменьшением ширина экрана начинают находить друг на друга, мешая четаемости.


### Bug #5 Ширина страницы больше ширины экрана в каталоге

**Приоритет**: low

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197
- Устройство iPhone SE

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com
Кнопки: "Предыдущая", "Следующая", "Создать"

**Ожидание:**
Ширина страницы и ее элементы будут не больше устройства.

**Фактически:**
Ширина страницы больше устройства из-за чего появляется горизонтальный скролл.

### Bug #6 Несоответсвие сортировки в заказах

**Приоритет**: low

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com/orders/

**Ожидание:**
При сортировке "по убыванию" заказы будут отсортированы соответственно, чтобы сверху были самые дорогие, а снизу дешевые и наоборот.

**Фактически:**
При сортировке "по убыванию" показывается сортировка "по возрастанию" и наоборот.

Данная ошибка исходит из предположения, что сортировка работает по стоимости заказа.


### Bug #7 Несоответсвие сортировки в каталоге

**Приоритет**: medium

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com/

**Ожидание:**
При сортировке "по убыванию" заказы будут отсортированы соответственно, чтобы сверху слева были самые дорогие, а снизу справа дешевые и наоборот.

**Фактически:**
При сортировке "по убыванию", как и "по возрастанию" товары перемещаются, но расположены не в отсортированном порядке.

### Bug #8 Отсутсвие валидации параметров при создании объявления

**Приоритет**: hight

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197

**Шаги**
1. Открыть страницу
2. Нажать на кнопку "Создать"
3. Ввести невалидные данные
4. Нажать на кнопку "Сохранить"

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com/

**Ожидание:**
При вводе любых не валидных данных, в том числе пустых появляется ошибка ввода в указанном поле.

**Фактически:**
Не валидные данные, кроме пустоты проходят проверку и сохраняются.

Прошедние не валидные данные: 
Название - содержащие спец. симвлолы, искажающие читаемость.
Цена - отрициательная.
URL изображения - может быть любой текст, не обязательно ссылка.

### Bug #9 Отсутсвие валидации параметров при редактировании объявления

**Приоритет**: hight

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197

**Шаги**
1. Открыть страницу
2. Открыть любое объявление 
3. Нажать на кнопку редактирования

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com/

**Ожидание:**
При вводе не валиждных данных, в том числе пустоты будет появляться ошибка ввоода в указанном поле и нельзя будет сохранить без исправления или отмены.

**Фактически:**
Можно ввести любые данные в любое поле и оно сохранится будь то пустое или не валидное значение. Однако, в стоимости все также можно вводить только число, хотя все также не валидируется.


### Bug #10 Отсутсвие подсказки, при редактировании объявления

**Приоритет**: medium

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197

**Шаги**
1. Открыть страницу
2. Открыть любое объявление 
3. Нажать на кнопку редактирования

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com/

**Ожидание:**
После стирания данных будут видны подсказки или лейблы чтобы понимать какие данные необходимо вводить в соответсвующем поле.

**Фактически:**
После стирания не появляется подсказка или лейбл. 

Если стиреть все данные, то становится совершенно неясно что было до этого, визуально страница кажется очень пустой.

### Bug #11 Не меняется счетчик просмотров

**Приоритет**: medium

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197


**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com/
Любое объявление в каталоге.

**Ожидание:**
Поле с количеством просмотров должно увеличиваться с посещением.

**Фактически:**
Кол-во просморов не меняется.

### Bug #12 Не работает фильтр в каталоге

**Приоритет**: medium

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com/

**Ожидание:**
При нажати на фильтр с любым из параметров "Цена", "Просмотры" или "Лайки" будут отображаться поля для выбранной фильтрации.

**Фактически:**
Не отображаются поля ни для одного праметра фильтрации будь то "Цена", "Просмотры" или "Лайки".

### Bug #13 Не правильно суммируется кол-во найденных объявлений

**Приоритет**: low

**Окружение**: 
- OS Windows 11 Home
- Браузер Google Chrome 132.0.6834.197

**Описание**
Страница: http://tech-avito-intern.jumpingcrab.com/

**Шаги**
1. Открыть страницу
2. Ввести в поле "Поиск по объявлениям" текст "Объявление"
3. Нажать на кнопку "Найти"

**Ожидание:**
Кол-во найденных в поле "Найдено:" будет правильно суммироваться по всем страницам.

**Фактически:**
В поле "Найдено:" отображается максимальное кол-во на странице (items on page) или столько, сколько найдено, если это меньше.