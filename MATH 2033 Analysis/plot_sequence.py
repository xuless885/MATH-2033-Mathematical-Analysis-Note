def a_n(n):
    """计算数列项"""
    numerator = 9 ** n
    denominator = ((-2) ** (n + 1)) * n
    return numerator / denominator

def plot_simple_sequence(max_n=15):
    """简单文本输出数列值"""
    print("数列 a_n = 9^n / [(-2)^(n+1) * n]")
    print("=" * 60)
    print(f"{'n':>3} | {'a_n':>20} | {'符号':>6} | {'|a_n|':>15}")
    print("-" * 60)
    
    for n in range(1, max_n + 1):
        value = a_n(n)
        sign = "+" if value > 0 else "-" if value < 0 else "0"
        print(f"{n:3} | {value:20.6f} | {sign:>6} | {abs(value):15.6f}")
    
    print("=" * 60)
    
    # 分析趋势
    print("\n趋势分析：")
    print("1. 符号交替：n为奇数时正，n为偶数时负")
    print("2. 绝对值快速增长，相邻项比值趋近于4.5")
    print("3. 数列发散到无穷大（交替发散）")

# 运行简化版本
if __name__ == "__main__":
    plot_simple_sequence(max_n=12)