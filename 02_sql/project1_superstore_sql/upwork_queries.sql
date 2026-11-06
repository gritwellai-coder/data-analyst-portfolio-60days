
-- Q1: Top 5 customers by sales
SELECT customer_name, SUM(sales) as total_sales
FROM orders WHERE customer_name IS NOT NULL
GROUP BY customer_name ORDER BY total_sales DESC LIMIT 5;

-- Q2: Which region has highest profit margin?
SELECT region, SUM(profit) as profit, SUM(sales) as sales, 
       ROUND(SUM(profit)*100.0/SUM(sales),2) as margin_pct
FROM orders GROUP BY region ORDER BY margin_pct DESC;

-- Q3: Loss-making orders where discount > 20%
SELECT order_id, customer_name, category, sub_category, sales, discount, profit
FROM orders WHERE discount > 0.2 AND profit < 0
ORDER BY profit ASC LIMIT 10;

-- Q4: Yearly sales trend
SELECT substr(order_date, -4) as year, SUM(sales) as yearly_sales
FROM orders GROUP BY year ORDER BY year;

-- Q5: Most discounted sub-category losing money
SELECT sub_category, AVG(discount) as avg_discount, SUM(profit) as total_profit
FROM orders GROUP BY sub_category HAVING avg_discount > 0.3 ORDER BY total_profit;
