#Укажем что это за фича
Feature: Checking search
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Сheck some text in search results
#И используем наши шаги.
  Given website "https://yandex.ru/"
  Then insert text in search 'расчет расстояний между городами'
  Then push button with text 'Найти'
  Then find href avtodispetcher 'https://www.avtodispetcher.ru/distance/'
  Then Checking our URl 'https://www.avtodispetcher.ru/distance/'