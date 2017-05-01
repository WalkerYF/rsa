## 1. 文件说明
1. id_rsa, id_rsa.pub:存放密钥（私钥和公钥）
2. prime_number_store：质数库
3. prime_number: 三行，每行放一个质数，用来生成密钥对
4. ciphertext: 存放加密后的密文
5. test.py：方法库
6. menu.py：主程序

## 2. 使用方法
1. 在质数库中随便选三个数放入prime_number文件中
    注意每行放一个，放三行
    用于生成密钥
2. 运行menu.py
```
python menu.py
```
3. 根据提示进行操作
```
---------------------------------------
This is a simple RSA Public-key system.
g: 生成密钥，并且公钥和秘钥存放到文件中
e: 加密信息，密文存放到文件中
d: 解密信息，明文显示在显示屏上
q：退出系统
---------------------------------------
```