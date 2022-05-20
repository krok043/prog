m_total = 0

for i in range(0, 2):
    p = float(input('Ingresa producto: '))
    if p >= 300:
        des = p * 0.20
    elif p >= 200 and p < 300:
        des = p * 0.15
    elif p >= 100 and p < 200:
        des = p * 0.07
    else:
        des = 0
    total = p - des
    m_total = m_total + total

print(m_total)