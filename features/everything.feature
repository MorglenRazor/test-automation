#Укажем что это за фича
Feature: Checking search
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Сheck some text in search results
#И используем наши шаги.
  Given website "https://yandex.ru/"
  Then insert text in search 'расчет расстояний между городами'
  Then push button with text 'Найти'
  Then find href avtodispetcher 'https://www.avtodispetcher.ru/distance/'
  Then Checking URl 'https://www.avtodispetcher.ru/distance/'
  Then Input value from 'Тула'
  Then Input value to 'Санкт-Петербург'
  Then Set value gas '9'
  Then Set value price on gas '46'
  Then Click on button with value 'Рассчитать'
  Then Checking total distance '897'
  Then Checking total price '3726'