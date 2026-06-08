def add(a: float, b: float) -> float:
    return a + b


def main() -> None:
    try:
        x = float(input("请输入第一个数字："))
        y = float(input("请输入第二个数字："))
        result = add(x, y)
        print(f"结果：{result}")
    except ValueError:
        print("输入有误：请输入数字。")


if __name__ == "__main__":
    main()
