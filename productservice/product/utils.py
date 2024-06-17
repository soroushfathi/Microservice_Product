from typing import Any, Dict, Optional


def format_response(
    success: bool, 
    data: Optional[Any] = None, 
    message: Optional[str] = None, 
    error_code: Optional[int] = None, 
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    response = {
        'success': success,
        'data': data,
        'message': message,
        'error_code': error_code,
        'metadata': metadata
    }
    return {k: v for k, v in response.items() if v is not None}
