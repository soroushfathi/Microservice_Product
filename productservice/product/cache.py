from django.core.cache import cache
import logging


logger = logging.getLogger(__name__)


def get_cached_product_list():
    logger.info(f":: {cache.get('product_list')}")
    return cache.get('product_list')


def set_cached_product_list(data):
    logger.info("Setting product list to the chache...")
    logger.info(data)
    cache.set('product_list', data, timeout=60*15)  # Cache timeout of 15 minutes


def get_cached_product(product_id):
    return cache.get(f'product_{product_id}')


def set_cached_product(product_id, data):
    cache.set(f'product_{product_id}', data, timeout=60*15)  # Cache timeout of 15 minutes


def delete_cached_product(product_id):
    cache.delete(f'product_{product_id}')


def delete_cached_product_list():
    cache.delete('product_list')
