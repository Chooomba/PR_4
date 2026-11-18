# Учебный проект: каталог книг (вариант 2)

Проект подготовлен для практической работы по GitHub Actions (CI/CD).

## Требования варианта
- Контейнер для jobs: `python:3.11.10-slim`.
- Проверка наличия `README.md` и непустого `app.py`.
- Поиск автора выполняется без учета регистра.
- Переменная приложения: `APP_PORT=8102`.
- Ветка `docs/*` запускает только `validate`.
- Артефакт содержит `books.py`, `README.md`, `Dockerfile`, `books.json.example` и `manifest.txt`.
- Срок хранения артефакта: 7 дней.
- Ручное учебное развертывание доступно из `main`.

## Локальный запуск
```bash
python books.py --help
python books.py --data books.json.example search-author булгаков
```

## Локальный запуск тестов
```bash
python -m unittest discover -s tests -v
```

## Загрузка в GitHub
1. Создайте пустой репозиторий на GitHub.
2. Загрузите в него все файлы проекта, включая скрытую папку `.github/workflows/`.
3. Основную ветку назовите `main`.
4. Откройте вкладку **Actions** и проверьте запуск workflow `Python CI/CD`.

## Настройка секретной переменной
Откройте **Settings → Secrets and variables → Actions → New repository secret**:
- Name: `DEPLOY_TOKEN`
- Secret: учебное значение, выданное преподавателем или созданное для этой работы.

Не помещайте секрет в репозиторий и не выводите его значение в журнал. Workflow проверяет только наличие секрета.

Переменная `APP_PORT=8102` задаётся в workflow.

## Правила запуска
- Pull request в `main`: `validate` и `unit_tests`.
- Push в `main`: `validate`, `unit_tests`, `package`.
- Push в `docs/*`: только `validate`.
- Push тега: `package` (также запускается `validate`).
- Ручной запуск workflow из `main`: `validate`, `package`, затем ручной по смыслу job `deploy_test` как часть отдельно запущенного workflow_dispatch.

## Отрицательный эксперимент (задание 2)
1. Отправьте исправную версию и убедитесь, что `unit_tests` проходит.
2. Временно измените в `books.py` поиск так, чтобы он учитывал регистр: замените `casefold()` на обычное сравнение.
3. Отправьте изменение в `main` или создайте Pull Request. Тест `test_author_search_ignores_case` должен завершиться ошибкой.
4. Верните `casefold()` в `search_by_author`, создайте новый commit и push.
5. Убедитесь, что workflow снова проходит.

Не оставляйте намеренный дефект в итоговой версии.
