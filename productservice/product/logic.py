import logging
from .cache import (
    get_cached_product, set_cached_product,
    delete_cached_product_list,
)
from .selectors import (
    get_all_products as get_all_products_selector,
    get_product_by_id as get_product_by_id_selector,
)
from .services import (
    create_product as create_product_service,
)
logger = logging.getLogger(__name__)


def get_product_by_id(product_id):
    cache_product = get_cached_product(product_id)
    if cache_product:
        logger.info(f"Get {cache_product} product detail from cache")
        return cache_product

    product = get_product_by_id_selector(product_id)

    if not product:
        return None

    logger.info("Get {product} product detail from db and set the cache.")
    set_cached_product(product_id, product)

    return product


def create_product(data):
    product = create_product_service(data)
    set_cached_product(product.id, product)
    delete_cached_product_list()
    logger.info(f"Product {product} has been created.")
    logger.info(f"\tSet new Produt cache, thenDelete product list from cache.")
    return product

