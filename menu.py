# 1. 生成公钥和秘钥
# 2. 加密信息（输入公钥，进行加密）（密文输出到文件）
# 3. 解密（输入秘钥，进行解密）（输入输出均重定向到文件）
import test


print("---------------------------------------")
print("This is a simple RSA Public-key system.")
print("g: 生成密钥，并且公钥和秘钥存放到文件中")
print("e: 加密信息，密文存放到文件中")
print("d: 解密信息，明文显示在显示屏上")
print("q：退出系统")
print("---------------------------------------")

choice = input('please enter your choice.\n')
while (choice != 'q'):
    if (choice == "g"):
        key = test.generate()
        # 存放公钥 在./id_rsa.pub
        file_pub_key = open(".\id_rsa.pub", "w")
        file_pub_key.write("%d\n%d" % (key[0], key[1]))
        file_pub_key.close()
        # 存放密钥 在./id_rsa
        file_pri_key = open(".\id_rsa", "w")
        file_pri_key.write("%d\n%d" % (key[2], key[1]))
        file_pri_key.close()

        print("your public key is: %d\n" % key[0])
        print("your common key is: %d\n" % key[1])
        print("your private key is: %d\n" % key[2])

    elif (choice == "e"):
        print("please put your public key in file:'./id_rsa.pub'\n")
        # 读入公钥（两行，第一行是e， 第二行是n）
        file_key = open("./id_rsa.pub", 'r')
        pub_key = int(file_key.readline())
        com_key = int(file_key.readline())
        file_key.close()
        # 读入明文
        ori_content = input("please enter the content you want to encrypt\n")
        # 明文转换为数字信息
        num_content = list()
        for i in ori_content:
            num_content.append(ord(i))
        # 数字信息加密，加密后的内容以列表形式存放在after_content中
        after_content = test.encrypt(pub_key, com_key, num_content)
        # 密文存放到文件中，并输出到屏幕
        file_ciphertext = open("./ciphertext", "w")
        for i in after_content:
            file_ciphertext.write("%d " % i)
        file_ciphertext.close()
        print(after_content)

    elif (choice == "d"):
        print("please put your private key in file:'./id_rsa'\n")
        # 读入密钥（两行，第一行是d， 第二行是n）
        file_key = open("./id_rsa", 'r') 
        pri_key = int(file_key.readline())
        com_key = int(file_key.readline())
        file_key.close()
        # 读入密文
        file_ciphertext = open("./ciphertext", "r")
        num_content = map(int, file_ciphertext.readline().split())
        file_ciphertext.close()
        # 数字信息解密，加密后的内容以数字列表形式存放在num_content中
        num_content = test.decode(pri_key, com_key, num_content)
        # 数字转换为明文
        ori_content = list()
        for i in num_content:
            ori_content.append(chr(i))
        # 明文输出到屏幕
        print(ori_content)

    choice = input('please enter your choice.\n')