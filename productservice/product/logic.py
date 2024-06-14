import logging
from .cache import get_cached_product
from .selectors import (
    get_all_products as get_all_products_selector,
    get_product_by_id as get_product_by_id_selector,
)

logger = logging.getLogger(__name__)


def get_product_by_id(product_id):
    cache_product = get_cached_product(product_id)
    if cache_product:
        logger.info(f"Get {cache_product} product detail from cache")
        return cache_product

    prodcut = get_product_by_id_selector(product_id)

    if not product:
        return None

    logger.info("Get {product} product detail from db and set the cache.")
    set_cached_product(product_id, product)

    return product
