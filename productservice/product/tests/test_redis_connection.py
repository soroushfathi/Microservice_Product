import pytest
from django.core.cache import cache
from redis.exceptions import ConnectionError

@pytest.mark.django_db
def test_redis_connection():
    try:
        # Set a value in the cache
        cache.set('test_key', 'test_value', timeout=30)
        
        # Retrieve the value from the cache
        value = cache.get('test_key')
        
        # Assert the value is what we expect
        assert value == 'test_value'
    except ConnectionError:
        pytest.fail("Could not connect to Redis")
