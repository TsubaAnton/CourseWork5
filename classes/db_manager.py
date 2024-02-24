import psycopg2
from utils.config import config


class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def execute_query(self, query) -> list:
        """Возвращает результат запроса"""
        conn = psycopg2.connect(dbname=self.db_name, **config())
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
        conn.close()

        return result

    def companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        return self.execute_query("""SELECT e.name, COUNT(v.name) FROM employers e
                                    LEFT JOIN vacancies v ON e.id = v.employer
                                    GROUP BY e.name""")

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
        вакансию"""
        return self.execute_query("""SELECT e.name, v.name, v.salary_from, v.salary_to, v.url FROM employers e 
                                    INNER JOIN vacancies v ON e.id = v.employer""")

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        result = self.execute_query("""SELECT AVG(salary_from + salary_to) / 2 FROM vacancies""")
        return result[0][0] if result else None

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        return self.execute_query("""SELECT * FROM vacancies WHERE (salary_from + salary_to) > (SELECT AVG(
                                    salary_from + salary_to) / 2 FROM vacancies)""")

    def get_vacancies_with_keyword(self, keyword):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""
        return self.execute_query(f"""SELECT * FROM vacancies
                    WHERE name LIKE '%{keyword}%'""")



