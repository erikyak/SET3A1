# График, который отображает, как меняется приближенное значение площади в зависимости от указанных параметров алгоритма:
![Figure_1.png](Figure_1.png)
# График, который отображает, как меняется величина относительного отклонения приближенного значения площади от ее точной оценки в зависимости от указанных параметров алгоритма:
![Figure_2.png](Figure_2.png)


# Результаты экспериментов:

При малом числе точек (N ≤ 20000) приближенное значение площади сильно отклоняется от точной площади, отклонение большое.

С ростом числа точек (N ≥ 40000) приближение становится значительно точнее, отклонение уменьшается и стабилизируется.

# Выводы:

Алгоритм Монте-Карло обеспечивает эффективное приближенное вычисление площади пересечения кругов.

Точность сильно зависит от числа сгенерированных точек и размера ограничивающей области.

При увеличении количества сгенерированных точек в среднем точность вычислений улучшается, хоть и существуют некоторые резкие отклонения, этим самым случайные алгоритмы показывают
свой вероятностный характер, где качество результата зависит от случайного распределения точек,
однако при достаточно большом количестве точек эти отклонения становятся незначительными.


<details>
  <summary>Бонус</summary>
   <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f6e5f327-1c1b-4b17-96d7-587e5f0de844/d2lfsl4-c66eaab4-f612-4a79-8477-907292359384.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Y2ZTVmMzI3LTFjMWItNGIxNy05NmQ3LTU4N2U1ZjBkZTg0NFwvZDJsZnNsNC1jNjZlYWFiNC1mNjEyLTRhNzktODQ3Ny05MDcyOTIzNTkzODQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.dVkHBz7AgXXXQ5HPJmqOxHt93lgGIX7g29eVEsNXyGk" width="500"/>
</details>
