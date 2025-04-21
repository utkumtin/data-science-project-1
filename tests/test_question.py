import datetime
from decimal import Decimal
import sys
import os
from unittest.mock import MagicMock, patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from data.questions import question_10_query, question_1_query, question_2_query, question_3_query, question_4_query, question_5_query, question_6_query, question_7_query, question_8_query, question_9_query

def run_common_test(expected_data, tested_func, query):
    result = tested_func()
    assert result == expected_data

def test_question_1_query():
    # Fake data
    expected_data = [
        ('Ali Veli', 'Turkey'),
        ('Ayşe Yılmaz', 'Turkey'),
        ('John Doe', 'USA'),
        ('Emma Brown', 'UK'),
        ('Carlos Mendez', 'Mexico'),
        ('Merve Demir', 'Turkey')
    ]
    run_common_test(expected_data, question_1_query, 'SELECT customer_name, country FROM customers;')
    

def test_question_2_query():
    expected = [
        (6, 5, datetime.date(2023, 6, 18), Decimal('1899.00')),
        (3, 3, datetime.date(2023, 1, 5), Decimal('1250.75')),
        (2, 2, datetime.date(2022, 6, 10), Decimal('499.99')),
        (5, 4, datetime.date(2023, 5, 1), Decimal('329.50')),
        (1, 1, datetime.date(2022, 1, 15), Decimal('249.90'))
    ]
    run_common_test(expected, question_2_query, 'SELECT * FROM orders ORDER BY total_amount DESC LIMIT 5;')
   

def test_question_3_query():
    expected = [('USB-C Cable', Decimal('49.95')), ('Wireless Mouse', Decimal('199.90')), ('Laptop Stand', Decimal('329.50'))]
    run_common_test(expected, question_3_query, 'SELECT product_name, price FROM products ORDER BY price ASC LIMIT 3;')


def test_question_4_query():
    expected = [(3, 'John Doe', 'john.doe@example.com', 'USA', datetime.date(2020, 11, 15)), (2, 'Ayşe Yılmaz', 'ayse.yilmaz@example.com', 'Turkey', datetime.date(2021, 5, 3)), (6, 'Merve Demir', 'merve.d@example.com', 'Turkey', datetime.date(2021, 9, 30)), (1, 'Ali Veli', 'ali.veli@example.com', 'Turkey', datetime.date(2022, 1, 10)), (5, 'Carlos Mendez', 'carlos.m@example.com', 'Mexico', datetime.date(2022, 7, 12)), (4, 'Emma Brown', 'emma.b@example.co.uk', 'UK', datetime.date(2023, 2, 21))]
    run_common_test(expected, question_4_query, 'SELECT * FROM customers ORDER BY signup_date ASC LIMIT 10;')
    

def test_question_5_query():
    expected = [('USB-C Cable', 100)]
    run_common_test(expected, question_5_query, 'SELECT product_name, stock_quantity FROM products ORDER BY stock_quantity DESC LIMIT 1;')


def test_question_6_query():
    expected = [(6, 5, datetime.date(2023, 6, 18), Decimal('1899.00'))]
    run_common_test(expected, question_6_query, 'SELECT * FROM orders ORDER BY order_date DESC LIMIT 1;')


def test_question_7_query():
    expected = [('27" Monitor',), ('Gaming Keyboard',), ('Laptop Stand',), ('Noise-Cancelling Headphones',), ('USB-C Cable',), ('Wireless Mouse',)]
    run_common_test(expected, question_7_query, 'SELECT product_name FROM products ORDER BY product_name ASC;')
    

def test_question_8_query():
    expected = [(1, 'ali.veli@example.com'), (2, 'ayse.yilmaz@example.com'), (3, 'john.doe@example.com'), (4, 'emma.b@example.co.uk'), (5, 'carlos.m@example.com')]
    run_common_test(expected, question_8_query, 'SELECT customer_id, email FROM customers ORDER BY customer_id ASC LIMIT 5;')

def test_question_9_query():
    expected = [(7, Decimal('49.95')), (4, Decimal('199.90')), (1, Decimal('249.90'))]
    run_common_test(expected, question_9_query, 'SELECT order_id, total_amount FROM orders ORDER BY total_amount ASC LIMIT 3;')


def test_question_10_query():
    expected = [(1, 'Ali Veli', 'ali.veli@example.com', 'Turkey', datetime.date(2022, 1, 10)), (2, 'Ayşe Yılmaz', 'ayse.yilmaz@example.com', 'Turkey', datetime.date(2021, 5, 3)), (6, 'Merve Demir', 'merve.d@example.com', 'Turkey', datetime.date(2021, 9, 30))]
    run_common_test(expected, question_10_query, 'SELECT * FROM customers WHERE country = \'Turkey\' ORDER BY customer_name ASC;')


class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1

def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")

if __name__ == "__main__":
    run_tests()