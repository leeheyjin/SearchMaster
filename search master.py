import tkinter as tk
import webbrowser

base=tk.Tk()
base.title('Search Master')
string=tk.StringVar()

def search():
    for i in check_value:
        if check_value[i].get()==True:
            webbrowser.open(url[i]+string.get())

input_area=tk.Frame(base, relief=tk.RAISED, bd=2)

entry=tk.Entry(input_area, textvariable=string).pack(side=tk.LEFT)
search_button=tk.Button(input_area, text='검색', command=search).pack(side=tk.LEFT)

input_area.pack(padx=70, pady=5)

website={0:'구글',
         1:'네이버',
         2:'Bing',
         3:'나무위키',
         4:'유튜브',
         5:'넷플릭스',
         6:'페이스북',
         7:'인스타그램'}

url={0:'https://www.google.com/search?q=',
     1:'http://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=',
     2:'https://www.bing.com/search?q=',
     3:'https://namu.wiki/w/',
     4:'https://www.youtube.com/results?search_query=',
     5:'https://media.netflix.com/ko/search?term=',
     6:'https://www.facebook.com/search/top?q=',
     7:'https://www.instagram.com/'}

check_value={}

for i in range(len(website)):
    check_value[i]=tk.BooleanVar()
    tk.Checkbutton(base, variable=check_value[i], text=website[i]).pack(anchor=tk.W)

base.mainloop()

