from classes.db_manager import DBManager


def method_choice():
    method = DBManager("course_work_5")
    choice = input("""1 - Cписок всех компаний и количество вакансий у каждой компании
      2 - Cписок всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
      3 - Cреднюю зарплату по вакансиям
      4 - Cписок всех вакансий, у которых зарплата выше средней по всем вакансиям
      5 - Cписок всех вакансий, в названии которых содержатся переданные в метод слова, например python
      Выберите, что вы хотите получить:""")
    if choice == "1":
        print(method.companies_and_vacancies_count())
    elif choice == "2":
        print(method.get_all_vacancies())
    elif choice == "3":
        print(method.get_avg_salary())
    elif choice == "4":
        print(method.get_vacancies_with_higher_salary())
    elif choice == "5":
        word = input("Выберите слово, по которому будет производиться поиск:")
        print(method.get_vacancies_with_keyword(f"{word}"))


if __name__ == "__main__":
    method_choice()
