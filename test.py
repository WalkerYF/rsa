# 快速幂模
def quick_power(b, e, p):
    ans = 1
    while(e > 1):
        if (e % 2 != 0):
            ans = (ans * b) % p
        b = (b * b) % p
        e = e // 2
    return (ans * b) % p


# 快速幂， 不模
def quick_power2(b, e):
    ans = 1
    while(e > 1):
        if (e % 2 != 0):
            ans = ans * b
        b = b * b
        e = e // 2
    return ans * b


# ax === 1 (mod p)
# 1 = ax + py
# 扩展欧几里得算法，默认认为两数互质
def extended_euler(a, p):
    if (p == 1):
        return (0, 1)
    (x1, y1) = extended_euler(p, a % p)
    x = y1
    y = x1 - a // p * y1
    return (x, y)


# 用扩展欧几里得算法求乘法逆元
# 中间有一个循环确保求出大于零的逆元
def Modular_Inverse(a, p):
    (x, y) = extended_euler(a, p)
    while (x < 0):
        x = x + p
    return x


# ax === 1 (mod p)
# 由费马小定理a^(p-1)≡ 1(mod p)(p为素数)
# 稍作变形 aa^(p-2)≡ 1(mod p)
# a^(p-2)即是a的逆元
def Modular_Inverse2(a, p):
    return quick_power2(a, p-2)


# 产生密钥对
# 从文件中直接拿三个质数
# （e,n）为公钥
# （d,n）为私钥
def generate():
    file_primeNumber = open('./prime_number', 'r')
    prime_number = []
    for i in range(0, 3):
        number = int(file_primeNumber.readline())
        prime_number.append(number)
    print(prime_number)
    q = prime_number[0]
    p = prime_number[1]
    # 得到两个质数 p, q
    n = q * p
    # k 是 欧拉函数值
    k = (q-1) * (p-1)
    # 得到e e与k互质(e从质数库里拿)
    e = prime_number[2]
    # 求d, d是e在模k下的逆元
    d = Modular_Inverse(e, k)
    print(e, d, k)
    return (e, n, d)
    # return (2987, 3937, 143)
    # return (17, 3233, 2753)


# 加密
# input：公钥和存放逐个数字的列表
# return：逐个数字加密后的列表
def encrypt(pub_key, com_key, num_content):
    after_content = []
    for i in num_content:
        result = quick_power(i, pub_key, com_key)
        after_content.append(result)
    return after_content


# 解密
# input：私钥， 存放数字的列表
# return：存放解密后数字的列表
def decode(pri_key, com_key, num_content):
    after_content = []
    for i in num_content:
        result = quick_power(i, pri_key, com_key)
        after_content.append(result)
    return after_content

