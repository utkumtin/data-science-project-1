# Preparations:
  1. İlk olarak aşağıdaki tabloları Postgres veritabanında oluşturunuz.
    - CREATE TABLE customers (customer_id SERIAL PRIMARY KEY,customer_name VARCHAR(100),email VARCHAR(100),country VARCHAR(50),signup_date DATE);
    - CREATE TABLE orders (order_id SERIAL PRIMARY KEY,customer_id INTEGER REFERENCES customers(customer_id),order_date DATE,total_amount NUMERIC(10,2));
    - CREATE TABLE products (product_id SERIAL PRIMARY KEY,product_name VARCHAR(100),price NUMERIC(8,2),stock_quantity INTEGER);
  2. İkinci olarak tablolara ilgili verileri eklemek için aşağıdaki sorugları da çalıştırınız.
    - INSERT INTO customers (customer_name, email, country, signup_date) VALUES
        ('Ali Veli', 'ali.veli@example.com', 'Turkey', '2022-01-10'),
        ('Ayşe Yılmaz', 'ayse.yilmaz@example.com', 'Turkey', '2021-05-03'),
        ('John Doe', 'john.doe@example.com', 'USA', '2020-11-15'),
        ('Emma Brown', 'emma.b@example.co.uk', 'UK', '2023-02-21'),
        ('Carlos Mendez', 'carlos.m@example.com', 'Mexico', '2022-07-12'),
        ('Merve Demir', 'merve.d@example.com', 'Turkey', '2021-09-30');
    - INSERT INTO products (product_name, price, stock_quantity) VALUES
        ('Wireless Mouse', 199.90, 30),
        ('Gaming Keyboard', 499.99, 15),
        ('USB-C Cable', 49.95, 100),
        ('27" Monitor', 1899.00, 8),
        ('Laptop Stand', 329.50, 20),
        ('Noise-Cancelling Headphones', 1250.75, 5);

    - INSERT INTO orders (customer_id, order_date, total_amount) VALUES
        (1, '2022-01-15', 249.90),
        (2, '2022-06-10', 499.99),
        (3, '2023-01-05', 1250.75),
        (1, '2023-03-12', 199.90),
        (4, '2023-05-01', 329.50),
        (5, '2023-06-18', 1899.00),
        (6, '2021-10-10', 49.95);
    
    3. 3 tabloyada birer SELECT sorgusu atarak tablolara tanımaya çalışın daha sonra aşağıdaki 10 soru için ilgili sql leri yazmaya çalışınız. 

# Questions
1. customers tablosundan tüm müşterilerin adlarını ve ülkelerini getir.
2. orders tablosunda en yüksek tutarlı 5 siparişi listele (tüm sütunlarla birlikte).
3. products tablosundan fiyatı en düşük 3 ürünü, sadece adları ve fiyatları ile getir.
4. customers tablosundaki en eski kayıtlı 10 müşteriyi signup_date'e göre sırala.
5. products tablosunda en fazla stoğa sahip ürünü sadece adı ve stock_quantity ile getir.
6. orders tablosunda son siparişi (tarihi en güncel olanı) listele.
7. products tablosunda sadece product_name sütununu alfabetik sırada göster.
8. customers tablosundan email sütunu olan ilk 5 müşteriyi customer_id'ye göre sırala.
9. orders tablosunda tutarı en düşük 3 siparişi ve bunların order_id'lerini getir.
10. customers tablosundan sadece Türkiye'deki (country = 'Turkey') müşterileri alfabetik sırala.