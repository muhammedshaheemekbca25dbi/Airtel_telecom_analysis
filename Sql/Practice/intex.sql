CREATE INDEX IF NOT EXISTS IX_order_customer
  on shop_orders (customer_id);