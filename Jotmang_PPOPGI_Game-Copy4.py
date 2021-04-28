#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Copy4 :: 코드 정리. 쓸데없는 코드 삭제, 보기 좋게 정렬

import tkinter as tk    
from tkinter.font import Font        
import random
import time
import numpy as np


# In[3]:


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('GaCha')              # 창 제목 설정
        self.geometry("500x400+200+500")   # 창 크기 (너비x높이+x좌표+y좌표)
        self.resizable(False, False)   # 창 크기 조절 여부   
        self._frame = StartPage(self)
        self._frame.pack()        
        
class StartPage(tk.Frame): 
    
############## 10회 뽑기 ##############      
    def Start_gacha_10(self):  # 10연 뽑기 무료증정
        
        if self.count_total >= 999999999:  # 뽑을 수 있는 최고치를 넘으면 못뽑는다.
            self.inform2.config(text = "너무 많이 뽑으셨습니다.") 
            self.start_gacha.config(state = 'disabled')
            self.start_gacha_10.config(state = 'disabled')
            self.keep_going_btn.config(state='disabled')
            self.unlimited_going_btn.config(state='disabled')
            self.mooyaho_going_btn.config(state='disabled')
            return
        
        keep_going = self.keep_going.get()  # 0 이면 당첨됐을 때 버튼 꺼지고, 1 이면 계속 켜져있음.
        unlimited_going = self.unlimited_going.get()  # 1이면 이 함수를 당첨될때까지 반복함.
        mooyaho_going = self.mooyaho_going.get()  # '무한 뽑기' 가 1이면 끌때까지 무한반복함.
            
        lucky_percent = self.float_percent / 100  # 100%면 1로 만들어줌. 0.01%면 0.0001 ㅋㅋ
        p = [1-lucky_percent, lucky_percent]  # 안뽑힐 확률과 뽑힐 확률 표본. 
        lucky_number = np.random.choice(2, 10, p=p)  # 10번 뽑아서 1이 뜨면 뽑힌거.

        result_list = []  # 이 리스트에 0이면 꽝을, 1이면 당첨 을 차곡차곡 넣는다.
        for element in lucky_number:
            if element == 0:
                result_list.append("꽝")
            elif element == 1:
                result_list.append(" 당첨 ")
                unlimited_going = 0   # 뽑혔으면 '뽑힐때까지 뽑기' 라디오버튼을 해제함.
                if keep_going == 1:  # '뽑으면 버튼 비활성화 시키기'가 켜져있을 경우 당첨됐을 때 버튼 비활성화
                    self.start_gacha.config(state = 'disabled')
                    self.start_gacha_10.config(state = 'disabled') 

        how_many_get = np.count_nonzero(lucky_number == 1)  # 10개 중 몇 개나 당첨됐는지 저장.

        self.count_total += 10 # 누적 뽑은 횟수 10 추가
        self.count_get += how_many_get  # 누적 획득 갯수 뽑힌만큼 추가 

        try:
            self.get_percent = round((self.count_get / self.count_total) * 100, 5)   # 뽑은 확률 초기화
        except:
            self.get_percent = 0.0

        self.count_total_show.config(text = "뽑은 횟수 : " + str(self.count_total) + "회")
        self.count_get_show.config(text = "획득 갯수 : " + str(self.count_get) + "개")
        self.get_percent_show.config(text = "얻은 확률 : " + str(self.get_percent) + "%")

        if how_many_get == 10:      # 중앙정렬이 없어서 대충 노가다로 만듬.
            self.result_show_10.place(x=25, y=250)
        elif how_many_get == 9:    
            self.result_show_10.place(x=39, y=250)
        elif how_many_get == 8:    
            self.result_show_10.place(x=53, y=250)
        elif how_many_get == 7:    
            self.result_show_10.place(x=67, y=250)
        elif how_many_get == 6:    
            self.result_show_10.place(x=81, y=250)
        elif how_many_get == 5:    
            self.result_show_10.place(x=95, y=250)
        elif how_many_get == 4:    
            self.result_show_10.place(x=109, y=250)
        elif how_many_get == 3:    
            self.result_show_10.place(x=123, y=250)
        elif how_many_get == 2:    
            self.result_show_10.place(x=138, y=250)
        elif how_many_get == 1:    
            self.result_show_10.place(x=151, y=250)
        elif how_many_get == 0:    
            self.result_show_10.place(x=165, y=250)        

        self.result_show_10.config(text=result_list)  # 당첨 현황 알려줌.

        if how_many_get >= 1:  # 1개 이상이면 당첨이니까.
            self.result_show.config(text = str(how_many_get) + "개 획득", fg='red', font=['Helvetica', 20, 'bold'])
            self.result_show.place(x=185, y=210)
        else:
            self.result_show.config(text = "꽝", font='TkDefaultFont', fg='black')
            self.result_show.place(x=240, y=210)
            
        # 연속뽑기가 진행중일 때는 버튼을 한 번 더 누를 수 없게끔 비활성화    
        # keep_going 이 0인 경우에만 실행하는 이유는 keep_going은 위에 코드에서 바뀔 수 있기 때문.
        if unlimited_going == 1 and keep_going == 0 or mooyaho_going == 1 and keep_going == 0:  
            self.start_gacha.config(state = 'disabled')
            self.start_gacha_10.config(state = 'disabled') 
        elif unlimited_going == 0 and keep_going == 0 or mooyaho_going == 0 and keep_going == 0:
            self.start_gacha.config(state = 'active')
            self.start_gacha_10.config(state = 'active') 
        
        self.tic = self.var.get()  # 스케일바에서 얻어지는 값    
        
        if self.tic == 1:
            self.tic = 10
        elif self.tic == 2:
            self.tic = 100
        elif self.tic == 3:
            self.tic = 1000
        
        if unlimited_going == 1 and mooyaho_going == 0:
            self.unlimited_working = self.after(self.tic, self.Start_gacha_10)  # 뽑힐때까지 뽑기가 켜져있으면 무한반복. 
        elif unlimited_going == 0 and mooyaho_going == 1:
            self.unlimited_working = self.after(self.tic, self.Start_gacha_10)  # '무한 뽑기'가 켜져있으면 무한반복. 
        
############## 1회 뽑기 ##############           
    def Start_gacha(self):  # 1회 뽑기 무료증정
        
        if self.count_total >= 999999999:  # 뽑을 수 있는 최고치를 넘으면 못뽑는다.
            self.inform2.config(text = "너무 많이 뽑으셨습니다.") 
            self.start_gacha.config(state = 'disabled')
            self.start_gacha_10.config(state = 'disabled')
            self.keep_going_btn.config(state='disabled')
            self.unlimited_going_btn.config(state='disabled')
            self.mooyaho_going_btn.config(state='disabled')
            return
        
        keep_going = self.keep_going.get()  # 0 이면 당첨됐을 때 버튼 꺼지고, 1 이면 계속 켜져있음.
        unlimited_going = self.unlimited_going.get()  # 1이면 이 함수를 당첨될때까지 반복함.
        mooyaho_going = self.mooyaho_going.get()  # '무한 뽑기' 가 1이면 끌때까지 무한반복함.
        
        self.count_total += 1 # 누적 뽑은 횟수 1 추가
        
        lucky_percent = self.float_percent / 100  # 100%면 1로 만들어줌. 0.01%면 0.0001 ㅋㅋ
        p = [1-lucky_percent, lucky_percent]  # 안뽑힐 확률과 뽑힐 확률 표본. 
        
        lucky_number = np.random.choice(2, 1, p=p)  # 1번 뽑아서 1이 뜨면 뽑힌거.
        
        if lucky_number[0] == 1:
            self.result_show.config(text = "1개 획득", fg='red', font=['Helvetica', 20, 'bold'])
            self.result_show.place(x=185, y=210)
            self.count_get += 1  # 누적 획득 갯수 1개 추가 
            unlimited_going = 0 # 뽑혔으면 '뽑힐때까지 뽑기' 라디오버튼을 해제함.
            
            self.result_show_10.config(text="{ 당첨 }")
            self.result_show_10.place(x=225, y=250)
            
            if keep_going == 1:  # 0 이면 당첨됐을 때 버튼 꺼지고, 1 이면 계속 켜져있음.
                self.start_gacha.config(state = 'disabled')
                self.start_gacha_10.config(state = 'disabled')  
        else: 
            self.result_show.config(text = "꽝", font='TkDefaultFont', fg='black')
            self.result_show.place(x=240, y=210)
            self.result_show_10.config(text="꽝")
            self.result_show_10.place(x=240, y=250)
            
        try:
            self.get_percent = round((self.count_get / self.count_total) * 100, 5)   # 뽑은 확률 초기화
        except:
            self.get_percent = 0.0
        
        self.count_total_show.config(text = "뽑은 횟수 : " + str(self.count_total) + "회")
        self.count_get_show.config(text = "획득 갯수 : " + str(self.count_get) + "개")
        self.get_percent_show.config(text = "얻은 확률 : " + str(self.get_percent) + "%")
        
        # 연속뽑기가 진행중일 때는 버튼을 한 번 더 누를 수 없게끔 비활성화    
        # keep_going 이 0인 경우에만 실행하는 이유는 keep_going은 위에 코드에서 바뀔 수 있기 때문.
        if unlimited_going == 1 and keep_going == 0 or mooyaho_going == 1 and keep_going == 0:  
            self.start_gacha.config(state = 'disabled')
            self.start_gacha_10.config(state = 'disabled') 
        elif unlimited_going == 0 and keep_going == 0 or mooyaho_going == 0 and keep_going == 0:
            self.start_gacha.config(state = 'active')
            self.start_gacha_10.config(state = 'active') 
        
        self.tic = self.var.get()  # 스케일바에서 얻어지는 값    
        
        if self.tic == 1:
            self.tic = 10
        elif self.tic == 2:
            self.tic = 100
        elif self.tic == 3:
            self.tic = 1000
        
        if unlimited_going == 1 and mooyaho_going == 0:
            self.unlimited_working = self.after(self.tic, self.Start_gacha)  # 뽑힐때까지 뽑기가 켜져있으면 무한반복. 
        elif unlimited_going == 0 and mooyaho_going == 1:
            self.unlimited_working = self.after(self.tic, self.Start_gacha)  # '무한 뽑기'가 켜져있으면 무한반복.  
        
############## 확률 치고 엔터 눌렀을 때 ##############      
    def Put_percent(self):
        # 문자가 들어오면 오류로 인식함.
        try:
            self.count_total = 0  # 누적 뽑은 횟수 초기화
            self.count_get = 0   # 누적 획득 횟수 초기화
            try:
                self.get_percent = round((self.count_get / self.count_total) * 100, 5)   # 뽑은 확률 초기화
            except:
                self.get_percent = 0.0
                
            self.count_total_show.config(text = "뽑은 횟수 : " + str(self.count_total) + "회")
            self.count_get_show.config(text = "획득 갯수 : " + str(self.count_get) + "개")
            self.get_percent_show.config(text = "얻은 확률 : " + str(self.get_percent) + "%")
            self.inform2.config(text = "") 
            
            # 최대치에 다다르면 모든 버튼이 비활성화 되는데, 확률을 다시 입력하면 전부 다시 활성화 되게끔 만들기.
            self.start_gacha.config(state = 'active')  
            self.start_gacha_10.config(state = 'active')
            self.keep_going_btn.config(state='active')
            self.unlimited_going_btn.config(state='normal')
            self.mooyaho_going_btn.config(state='normal')
        
            self.percent = tk.Entry.get(self.percent_enter)  # Entry에서 값 받아오는 부분.
            self.float_percent = float(self.percent)
            
            if self.float_percent < 0.00009:
                self.percent_show.config(text = "그건너무확률이낮음 ㅅㄱㅋㅋ")
            elif self.float_percent > 100:
                self.percent_show.config(text = "100%보다 높으면 뭐함")
            else:
                self.percent_show.config(text = '입력한 확률 : ' + str(round(self.float_percent, 5)) + "%")
                self.start_gacha.config(state = 'active')
                self.start_gacha_10.config(state = 'active')
        except:
            self.percent_show.config(text = "그건 숫자가 아닌듯 ㅋㅋ")
            
############## '무한 뽑기' 라디오 버튼을 눌렀을 때 ##############             
    def Disable_buttons(self):
        mooyaho_going = self.mooyaho_going.get() 
        
        # '무한 뽑기' 버튼이 눌리면 '뽑으면 버튼 비활성화' 와 '뽑힐때까지 뽑기' 의 체크가 해제되고 비활성화됨.
        if mooyaho_going == 1:  
            self.keep_going_btn.deselect()  
            self.keep_going_btn.config(state='disabled')
            self.unlimited_going_btn.deselect()
            self.unlimited_going_btn.config(state='disabled')
        elif mooyaho_going == 0:
            self.keep_going_btn.config(state='normal')
            self.unlimited_going_btn.config(state='normal')

############## 시작 ##############        
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, width = 500, height = 400)
        
        self.keep_going = tk.IntVar()
        self.unlimited_going = tk.IntVar()
        self.mooyaho_going = tk.IntVar()
        self.var=tk.IntVar()
        
        self.count_total = 0  # 누적갯수 저장
        self.count_total_show = tk.Label(self, text = "뽑은 횟수 : " + str(self.count_total) + "회", font=['Helvetica', 10, 'bold'])
        self.count_total_show.place(x=35, y=320)
        
        self.count_get = 0  # 뽑힌 횟수 저장
        self.count_get_show = tk.Label(self, text = "획득 갯수 : " + str(self.count_get) + "개", font=['Helvetica', 10, 'bold'])
        self.count_get_show.place(x=185, y=320)
        
        try:
            self.get_percent = round((self.count_get / self.count_total) * 100, 5)
        except:
            self.get_percent = 0.0
        self.get_percent_show = tk.Label(self, text = "얻은 확률 : " + str(self.get_percent) + "%", font=['Helvetica', 10, 'bold'])
        self.get_percent_show.place(x=340, y=320)
        
        self.percent = tk.Label(self, text = "확률 퍼센트로 써요 : ", anchor = 'e') # 라벨 생성
        self.percent.place(x=30, y=25)
        
        self.percent_show = tk.Label(self, text = "", anchor = 'e') # 라벨 생성
        self.percent_show.place(x=30, y=45)
        
        self.result_show = tk.Label(self, text = "") # 1회뽑기 라벨 생성
        self.result_show.place(x=235, y=210)
        
        self.result_show_10 = tk.Label(self, text = "") # 10회뽑기 라벨 생성
        self.result_show_10.place(x=25, y=250)
        
        self.inform1 = tk.Label(self, text = "(참고로 5째자리에서 반올림 됨.)", anchor = 'e') # 라벨 생성
        self.inform1.place(x=300, y=25)
        
        self.inform2 = tk.Label(self, text = "", fg='red') # 라벨 생성
        self.inform2.place(x=35, y=345)
        
        
        self.percent_enter = tk.Entry(self)  # Entry 생성
        self.percent_enter.bind("<Return>", lambda event:self.Put_percent())
        self.percent_enter.place(x=150, y=25) 
        
        
        self.start_gacha = tk.Button(self, text = '1회 뽑기', anchor = 'center', takefocus = True
                                  ,command = self.Start_gacha, state='disabled', font=['Helvetica', 18, 'bold'])
        self.start_gacha.place(x=30, y=75, width=210, height=90)
        
        self.start_gacha_10 = tk.Button(self, text = '10회 뽑기', anchor = 'center', takefocus = True
                                  ,command = self.Start_gacha_10, state='disabled', font=['Helvetica', 18, 'bold'])
        self.start_gacha_10.place(x=260, y=75, width=210, height=90)
        
        
        self.keep_going_btn=tk.Checkbutton(self, text='뽑으면 버튼 비활성화 시키기', variable=self.keep_going)
        self.keep_going_btn.place(x=5, y=370)
        
        self.unlimited_going_btn=tk.Checkbutton(self, text='뽑힐때까지 뽑기', variable=self.unlimited_going) 
        self.unlimited_going_btn.place(x=195, y=370)
        
        self.mooyaho_going_btn=tk.Checkbutton(self, text='무한 뽑기', variable=self.mooyaho_going, command=self.Disable_buttons) 
        self.mooyaho_going_btn.place(x=315, y=370)
        
        
        self.tic_scale=tk.Scale(self, variable=self.var, orient="horizontal", showvalue=False, label="속도조절",
                                length=60, sliderlength=30, from_=1, to=3)  # 출력 반복 간격 설정 스케일
        self.tic_scale.place(x=405 , y=353)
        
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


# In[ ]:




