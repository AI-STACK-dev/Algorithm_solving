import sys; input = sys.stdin.readline;
while True:
    D, RH, RV = map(float, input().split())
    if D == 0:
        break
    H_DPI = RH * (337 ** 0.5) / (16 * D)
    V_DPI = RV * (337 ** 0.5) / (9 * D)
    print(f"Horizontal DPI: {H_DPI :.2f}")
    print(f"Vertical DPI: {V_DPI :.2f}")