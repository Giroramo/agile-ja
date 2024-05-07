# ----これらの関数を変更する必要はありません----

names = ["Nick", "Lewis", "Nikos"]

def contains(name, list_of_names):
    if name not in list_of_names:
        return False
    else:
        return True

def get_name(name, list_of_names):
    if name in list_of_names:
        return name
    else:
        return -1

def add_name(name, list_of_names):
    list_of_names.append(name)
    return name

def add_two(num):
    return num + 2

def divide_by_two(num):
    return num / 2

def greeting(name, num):
    message = f"Hello, {name}. It is {num} degrees warmer today than yesterday"
    print(message)
    return message
# ----ここにコードを書いてください----*/
# ----難易度: 富士----
# `my_assert` をここに定義し、以降のテストに使用してください。
def my_assert(expr, msg="AssertionError: Assertion failed"):
    if not expr:
        raise AssertionError(msg)
    
# `contains` 用のテスト `test_contains` を作成してください
def test_contains():
    my_assert(contains("Nick", names) == True, "Test failed: contains")
    my_assert(contains("Lewis", names) == True, "Test failed: contains")
    my_assert(contains("Nikos", names) == True, "Test failed: contains")    
    my_assert(contains("John", names) == False, "Test failed: contains")

# `add_name` 用のテスト `test_add_name` を作成してください
def test_add_name():
    original_length = len(names)
    add_name("John", names)
    my_assert(len(names) == original_length + 1, "Test failed: add_name")

# `add_two` 用のテスト `test_add_two` を作成してください
def test_add_two():
    my_assert(add_two(3) == 5, "Test failed: add_two")

# `divide_by_two` 用のテスト `test_divide_by_two` を作成してください
def test_divide_by_two():
    my_assert(divide_by_two(8) == 4, "Test failed: divide_by_two")

# `greeting` 用のテスト `test_greeting` を作成してください
def test_greeting():
    my_assert(greeting("Nick", 10) == "Hello, Nick. It is 10 degrees warmer today than yesterday", "Test failed: greeting")

# テストの実行
test_contains()
test_add_name()
test_add_two()
test_divide_by_two()
test_greeting()
