print("欢迎来到猜数字游戏，本游戏由gwj编写")
print("-------------------------------------------------------------")
import random       
numb = random.randint(1,100)   
caice = 0    
while True:
    
        num_input = input("请输入一个1-100之间的，整数，整数，整数:")
        caice += 1
    
        if not num_input.isdigit():
            print("让你输入整数知道不，否则本程序无法正常运行.")
            print("****************************************")
        elif int(num_input) < 0 or int(num_input) >= 100:
            print("输入的数必须在1-100之间，你是不是不想玩了.")
        else:
            if numb == int(num_input):
                print("wdnmd，你很牛逼，只用了%d次, 你就成功了." % caice)
                break
            elif numb > int(num_input):
                print("太小了，继续猜，菜逼.")
            elif numb < int(num_input):
                print("太大了，不行啊，菜鸡")
            else:
                print("遭遇到异常，程序即将崩溃")
print("-------------------------------------------------------------") 
print("感谢您的游玩，欢迎下次继续，嘿嘿嘿")               
