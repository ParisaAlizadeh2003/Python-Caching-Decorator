# Caching Decorator in Python

This project implements a **Caching Decorator** in Python. The decorator stores the results of a function's computation. When the function is called again with the same arguments, it returns the cached result instead of recalculating it, improving performance.

## How It Works

1. **Caching Decorator**: The `Caching` decorator wraps the original function and stores its results in a dictionary.
2. **Argument Handling**: The arguments passed to the function are converted into a tuple because lists are not hashable and can't be used as dictionary keys.
3. **Caching Logic**:
   - When the function is called with certain arguments, the decorator first checks if the result for those arguments already exists in the cache (dictionary).
   - If the result is found in the cache, it is returned immediately.
   - If the result is not found, the function is executed, and the result is stored in the cache for future use.

## Example Usage

```python
@Caching
def Sum(*args):
    return sum(*args)

print(Sum([1, 4]))  # Computed and cached
print(Sum([2, 4]))  # Computed and cached
print(Sum([1, 4]))  # Cached result returned
print(Sum([3, 4]))  # Computed and cached
