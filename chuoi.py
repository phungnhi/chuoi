def min_in_tempcount(temp_count, a,i): # ki tu co so lan xuat hien it nhat và ASCII nho hon
    id = 0
    for j in range (len(temp_count)):
        if (temp_count[id] > temp_count[j] or (temp_count[id] == temp_count[j] and ord(a[i][id]) > ord (a[i][j]))):
            id = j
    return a[i][id].upper()
def demsokituitnhat(a, i): # tinh so luong xuat hien cua cac ki tu va tim min
    count = 0
    for j1 in (a[i]):
        for j2 in (a[i]):
            if(j1==j2):
                count = count + 1
        temp_count.append(count)
        count = 0
    ketqua = min_in_tempcount(temp_count, a, i)
    print (ketqua)
a = []
temp_count = [] #mang luu so luong xuat hien của các ki tu
n = int(input())
for i in range(n):
    temp = input()
    a. append(temp.lower())
for i in range(len(a)):
    demsokituitnhat(a, i)
    temp_count = []
