from src.models import db, Order

def create_order(customer_id, product_id, quantity):
    """Функція для створення замовлення."""
    order = Order(customer_id=customer_id, product_id=product_id, quantity=quantity, status='pending')
    db.session.add(order)
    db.session.commit()
    return order

def get_order(order_id):
    """Функція для отримання інформації про замовлення за ID."""
    order = Order.query.get(order_id)
    return order if order else None

def update_order_status(order_id, status):
    """Функція для оновлення статусу замовлення."""
    order = Order.query.get(order_id)
    if order:
        order.status = status
        db.session.commit()
        return order
    return None

def get_all_orders():
    """Функція для отримання списку всіх замовлень."""
    orders = Order.query.all()
    return orders
