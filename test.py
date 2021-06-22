from tkinter import *
from tkinter import ttk,messagebox
def convert():
    global n,m,l
    n= q.get()
    m= b.get()
    l= float(x.get())
    with open('currency.txt') as f:
        a = f.readlines()
    cur = []
    inv = []
    conv = []
    for i in a:
        word = i.split()
        cur.append(word[0])
        conv.append(word[3])
    cur.append("INDIAN")

    def getindex(cur, a):
        if a == 'INDIAN':
            return 0
        obj = list(enumerate(cur))
        for item in obj:
            if item[1] == a:
                return item[0]

    def convert(a, b, aindex, bindex, lst, x):
        p = float(lst[aindex])
        q = float(lst[bindex])
        if a != 'INDIAN' and b != 'INDIAN':
            ans = ((x * p) / q)
            return ans
        elif a == 'INDIAN':
            return x / q
        else:
            return x * p
    #print(fromc,toc,val)
    if n == m:
        st.set(f"{l} {n} is equal to {l} {m}")
        return
    g = getindex(cur, n)
    h = getindex(cur, m)
    result = convert(n, m, g, h, conv, l)
    st.set(f"{l} {n} is equal to {result} {m}")

root= Tk()
root.title("CURRENCY CONVERTER| Somosree Ghosh")
root.geometry("900x600+10+10")
root.maxsize(width=900,height=600)
frm= Frame(root,bd=20,relief=GROOVE,background="blue")
frm.place(x=5,y=5,width=890,height=490)
Label(frm, text="WELCOME TO CURRENCY CONVERTER!!", bg= "red", fg="white",font= "times 19 bold",bd=10,relief=RIDGE).place(x=150,y=10)
f=Frame(root,bd=20, relief= RAISED, background="light green").place(x=100,y=110,width=700,height=350)
Label(f, text= "FROM WHAT CURRENCY DO YOU WISH TO CONVERT?",font= "comicsansms 15 bold italic").place(x= 150,y=150)
Label(f,text= "Select currency:",font="times 11 bold",bg='black',fg='white').place(x=200,y=200)
q= StringVar()
fromcurr=ttk.Combobox(f,width=30,textvariable=q)
fromcurr['values']=('US','INDIAN','Argentine', 'Australian', 'Bahraini', 'Botswana', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Canadian', 'Chilean', 'ChineseYuan', 'Colombian', 'Croatian', 'Czech', 'Danish', 'Emirati', 'Euro', 'HongKong', 'Hungarian', 'Icelandic', 'Indonesian', 'Iranian', 'Israeli', 'Japanese', 'Kazakhstani', 'Kuwaiti', 'Libyan', 'Malaysian', 'Mauritian', 'Mexican', 'Nepalese', 'NewZealand', 'Norwegian', 'Omani', 'Pakistani', 'Philippine', 'Polish', 'Qatari', 'RomanianNew', 'Russian', 'SaudiArabian', 'Singapore', 'SouthAfrican', 'SouthKorean', 'SriLankan', 'Swedish', 'Swiss', 'TaiwanNew', 'Thai', 'Trinidadian', 'Turkish')
fromcurr.place(x=380,y=200)
fromcurr.current(0)
Label(f, text= "TO WHAT CURRENCY DO YOU WISH TO CONVERT?",font= "comicsansms 15 bold italic").place(x= 150,y=250)
Label(f,text= "Select currency:",font="times 11 bold",bg='black',fg='white').place(x=200,y=300)
b= StringVar()
tocurr=ttk.Combobox(f,width=30,textvariable=b)
tocurr['values']=('US','INDIAN','Argentine', 'Australian', 'Bahraini', 'Botswana', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Canadian', 'Chilean', 'ChineseYuan', 'Colombian', 'Croatian', 'Czech', 'Danish', 'Emirati', 'Euro', 'HongKong', 'Hungarian', 'Icelandic', 'Indonesian', 'Iranian', 'Israeli', 'Japanese', 'Kazakhstani', 'Kuwaiti', 'Libyan', 'Malaysian', 'Mauritian', 'Mexican', 'Nepalese', 'NewZealand', 'Norwegian', 'Omani', 'Pakistani', 'Philippine', 'Polish', 'Qatari', 'RomanianNew', 'Russian', 'SaudiArabian', 'Singapore', 'SouthAfrican', 'SouthKorean', 'SriLankan', 'Swedish', 'Swiss', 'TaiwanNew', 'Thai', 'Trinidadian', 'Turkish')
tocurr.place(x=380,y=300)
tocurr.current(1)
Label(f, text= "HOW MUCH DO YOU WISH TO CONVERT?",font= "comicsansms 15 bold italic").place(x= 150,y=350)
x= StringVar()
ent=Entry(f,bd=5,relief= SUNKEN, font= "Ariel 10 bold",textvariable=x).place(x= 600,y=350)
end= Frame(root,background='yellow',bd=10,relief=RIDGE).place(x=5,y=495,width=890,height=100)
Button(text= "Convert",font="Times 11 bold",bd=5,relief= RAISED,bg='black',fg='white',command=convert).place(x=330,y=390)
st= StringVar()
st.set("")
label=Label(f, textvariable= st,font= "Monotype 20 bold italic",bg="yellow").place(x= 150,y=520)
root.mainloop()