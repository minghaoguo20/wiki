## lambda functino

[lambda - Medium](https://martinxpn.medium.com/lambda-functions-in-python-a-comprehensive-guide-to-understanding-and-using-anonymous-functions-fedcb98c999f)

```python
# lambda function
lambda arguments: expression
```

example

```python
add = lambda x, y: x + y
result = add(5, 3)
print(result) # 8
```

### Using Lambda Functions with map

使用 Lambda 函数与 map 。

The map function is a built-in Python function that takes a function and an iterable as arguments and returns a new iterable with the function applied to each element. For example, to square all the elements of a list of numbers using a lambda function and map, we would write the following code:

map 函数是 Python 内置函数之一，它接受一个函数和一个可迭代对象作为参数，并返回一个新的可迭代对象，其中每个元素都应用了该函数。例如，使用 lambda 函数和 map 来对数字列表中的所有元素进行平方，我们可以编写以下代码：

```python
numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, numbers))
print(square) # [1, 4, 9, 16, 25]
```

### Using Lambda Functions with filter

使用 Lambda 函数与 filter 。

The filter function is another built-in Python function that takes a function and an iterable as arguments and returns a new iterable with only the elements for which the function returns True. For example, to get a list of even numbers from a list of numbers using a lambda function and filter, we would write the following code:

filter 函数是另一个内置的 Python 函数，它接受一个函数和一个可迭代对象作为参数，并返回一个仅包含函数返回 True 的元素的新可迭代对象。例如，使用 lambda 函数和 filter 从数字列表中获取偶数列表，我们可以编写以下代码：

```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # [2, 4]
```

### Using Lambda Functions with reduce

使用 Lambda 函数与 reduce 。

The reduce function is a built-in function from the functools module that takes a function and an iterable as arguments and returns a single value that is the result of applying the function cumulatively to the elements of the iterable. For example, to find the product of all the elements of a list of numbers using a lambda function and reduce, we would write the following code:

reduce 函数是 functools 模块中的内置函数，它接受一个函数和一个可迭代对象作为参数，并返回一个单一的值，该值是将函数累积应用于可迭代对象的元素的结果。例如，使用 lambda 函数和 reduce 查找数字列表中所有元素的乘积，我们可以编写以下代码：

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product) # 120
```

### Limitations of Lambda Functions Lambda

函数的限制

While lambda functions are incredibly useful, they do have a few limitations that are important to keep in mind. One of the main limitations of lambda functions is that they can only contain a single expression. This means that they cannot contain statements or multiple lines of code. Additionally, the expression must be a valid expression in Python and must return a value. Another limitation is that lambda functions cannot contain any annotations or type hints.

虽然 lambda 函数非常有用，但它们确实有一些限制需要牢记。lambda 函数的主要限制之一是
1. 它们只能包含单个表达式。这意味着它们不能包含语句或多行代码。
2. 表达式必须是 Python 中的有效表达式，并且必须返回一个值。
3. 另一个限制是 lambda 函数不能包含任何注释或类型提示。



## Enumerate

[Enumerate Medium](https://medium.com/towards-data-science/python-enumerate-built-in-function-acccf988d096)

```python
for i, layer in enumerate(self.layers):
    x = self.act(layer(x))
    if i in self.skip:
        x = torch.cat([x, x_input], dim=-1)
```

## ... 三个点的省略号

[... zhihu](https://zhuanlan.zhihu.com/p/264896206)

1. 等同于`pass`
2. Numpy中可以用来选数据
