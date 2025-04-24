from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def main():

    browser = webdriver.Firefox()
    query = input("Введите ваш запрос для поиска в Википедии: ")
    browser.get(f"https://ru.wikipedia.org/wiki/{query}")
    if "Википедия" in browser.title and "Страница отсутствует" not in browser.title:
        browse_article(browser)
    else:
        print("Статья не найдена. Попробуйте другой запрос.")
        browser.quit()


def get_paragraphs(browser):
    """Получить все параграфы текущей статьи"""
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    return [p.text for p in paragraphs if p.text.strip()]


def get_related_links(browser):
    """Получить все связанные ссылки из hatnotes"""
    hatnotes = []
    for element in browser.find_elements(By.CLASS_NAME, "hatnote"):
        if element.is_displayed():
            hatnotes.append(element)

    links = []
    for hatnote in hatnotes:
        try:
            link = hatnote.find_element(By.TAG_NAME, "a")
            links.append((link.text, link.get_attribute("href")))
        except:
            continue
    return links


def browse_article(browser):
    """Функция для просмотра статьи"""
    while True:
        print("\nТекущая статья:", browser.title)
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Ваш выбор (1-3): ")

        if choice == "1":
            paragraphs = get_paragraphs(browser)
            for i, p in enumerate(paragraphs, 1):
                print(f"\nПараграф {i}:")
                print(p)
                if i % 3 == 0:  # Показываем по 3 параграфа за раз
                    cont = input("\nПродолжить чтение? (y/n): ")
                    if cont.lower() != 'y':
                        break

        elif choice == "2":
            links = get_related_links(browser)
            if not links:
                print("Нет связанных страниц для перехода.")
                continue

            print("\nДоступные связанные страницы:")
            for i, (text, _) in enumerate(links, 1):
                print(f"{i}. {text}")

            link_choice = input("Выберите страницу для перехода (номер) или 0 для отмены: ")
            if link_choice == "0":
                continue

            try:
                idx = int(link_choice) - 1
                if 0 <= idx < len(links):
                    browser.get(links[idx][1])
                else:
                    print("Неверный выбор.")
            except ValueError:
                print("Пожалуйста, введите число.")

        elif choice == "3":
            print("Выход из программы...")
            browser.quit()
            return

        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")



if __name__ == "__main__":
    main()
