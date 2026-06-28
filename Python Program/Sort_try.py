import random

# def sort_func(seq):
#     lens = len(seq) # 3 1 5 4 8 7 6 9 10 2
#     for i in range(lens - 1):
#         swapped = False
#         for j in range(lens - 1 - i):
#             if seq[j] > seq[j + 1]:
#                 seq[j], seq[j + 1] = seq[j + 1], seq[j]
#                 swapped = True
#         if not swapped:
#             break
    
#     return seq

def sort_func(seq):
    lens = len(seq)  # 1. 取得數列的總長度
    
    # 2. 外層迴圈：控制「總共需要執行幾輪」比對
    # 每次外層迴圈結束，當前未排序部分的最大值就會像氣泡一樣「浮」到最右邊
    for i in range(lens - 1):
        
        # 3. 旗標（Flag）：用來記錄這一輪有沒有發生任何「交換」
        swapped = False
        
        # 4. 內層迴圈：實際進行「兩兩比較」的地方
        # 為什麼要 - i？因為每一輪結束後，右邊都會多一個已經排好序的最大值，不需要再比它了
        for j in range(lens - 1 - i):
            
            # 5. 如果前面的數字大於後面的數字，就進行交換
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                swapped = True  # 標記「有發生交換」
                
        # 6. 優化關鍵：如果某一輪跑完，發現完全沒有發生任何交換（swapped 依然是 False）
        # 代表整個數列已經提前排好序了，不需要再繼續做白工，直接跳出外層迴圈
        if not swapped:
            break
    
    return seq  # 7. 回傳排序完成的數列

def main():
    oringinal_seq = []
    while len(oringinal_seq) < 10:
        x = random.randint(1, 10)
        if x in oringinal_seq:
            continue
        else:
            oringinal_seq.append(x)

    sorted = sort_func(oringinal_seq)
    print(sorted)

if __name__ == '__main__':
    main()