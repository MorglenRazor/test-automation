@logging
@capture
Feature: Checking avtodispetcher

  Scenario: Сheck the construction of the route on the site www.avtodispetcher.ru

    Given Website "https://yandex.ru/"
    Then Insert text in search 'расчет расстояний между городами'
    Then Push button with text 'Найти'
    Then Find href avtodispetcher 'https://www.avtodispetcher.ru/distance/'
    Then Checking URl 'https://www.avtodispetcher.ru/distance/'
    Then Input value from 'Тула'
    Then Input value to 'Санкт-Петербург'
    Then Set value gas '9'
    Then Set value price on gas '46'
    Then Click on button with value 'Рассчитать'
    Then Checking total distance '897'
    Then Checking total price '3726'
    Then Change route 'Настроить маршрут'
    Then Find field between city and input city 'Великий Новгород'
    Then Wait 30 second and click btn 'Рассчитать'
    Then Checking new total distance '966'
    Then Checking new total price '4002'