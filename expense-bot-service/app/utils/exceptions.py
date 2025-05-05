class UserNotFoundError(Exception):
    """Raised when a user is not found in the whitelist"""
    pass

class ExpenseCategoryError(Exception):
    """Raised when there's an error categorizing an expense"""
    pass