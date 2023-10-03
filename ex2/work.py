from math import ceil

def calc_account(m):
    # 実装は入れていません、自分で入れてください
    base = 610 # 初乗り運賃

    if m <= 0: # 0m以下なら None を返す
        return None
    
    elif 0 <= m <= 1700: # 0以上1700以下なら 初乗り運賃 を返す
        return base
    
    else: #1701以上なら 初乗り運賃 + 超過分を足して 返す
        ex = (1 + (m - 1701) // 315) * 80 # どれだけ超過金の計算
        return base + ex


if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


