from .rabbitmq_consumer import RabbitMQConsumer
import logging
import json
from .models import Product

logger = logging.getLogger(__name__)

def handle_message(ch, method, properties, body):
    message = json.loads(body)
    action = message.get('action')

    if action == 'get_product':
        product_id = message.get('product_id')
        product = Product.objects.filter(id=product_id).first()
        if product:
            product_data = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'stock': product.stock
            }
            response = json.dumps(product_data)
        else:
            response = json.dumps({'error': 'Product not found'})
        
        if properties.reply_to:
            ch.basic_publish(
                exchange='',
                routing_key=properties.reply_to,
                properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                body=response
            )
        logger.info(f"Processed get_product action for {product_id}")

    elif action == 'update_stock':
        product_id = message.get('product_id')
        quantity = message.get('quantity')
        product = Product.objects.filter(id=product_id).first()
        if product:
            product.stock -= quantity
            product.save()
            logger.info(f"Updated stock for product {product_id} by {quantity}.")
        else:
            logger.info(f"Product with id {product_id} not found.")

if __name__ == '__main__':
    consumer = RabbitMQConsumer(queue_name='product_queue', callback=handle_message)
    try:
        consumer.start_consuming()
    except KeyboardInterrupt:
        consumer.stop_consuming()

