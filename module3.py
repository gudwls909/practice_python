def show_info(name):
    print('이름:', name)
    
#show_info('홍길동') # 이렇게 해버리면 import될때 자동으로 실행되어버린다

if __name__ == '__main__': # 이렇게 해야 python module3.py같이 밖에서 직접 실행할때만 실행되고 import될때는 실행되지않는다
    show_info('홍길동')