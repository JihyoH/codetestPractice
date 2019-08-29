# 1번 문제_1
def map(arr1,arr2):
    aa=[]

    for i in range(0,len(arr1)):
        route = bin(arr1[i]|arr2[i])[2:]
        route=route.replace("1","#")
        route=route.replace("0"," ")
        aa.append(route)

    return aa

arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]

arr3=[46, 33, 33 ,22, 31, 50]
arr4=[27 ,56, 19, 14, 14, 10]

answer1_1 = map(arr1,arr2)
answer1_2 = map(arr3,arr4)
# print(answer1_1)
# print(answer1_2)

# 2번 문제.
import re

def dartResult(result):
    rex = re.compile("[0-9]{1,2}[SDT]\*?\#?")
    result1=rex.findall(result)
    finalscore=0
    storage = 0
    for rr in result1:
        re1 = re.compile("[0-9]{1,2}")
        re2 = re.compile("[SDT]")
        re3 = re.compile("\*")
        re4 = re.compile("\#")
        res1 = re1.findall(rr)
        res2 = re2.findall(rr)
        res3 = re3.findall(rr)
        res4 = re4.findall(rr)

        score = int(res1[0]) # 점수

        # 필드
        if res2[0] == "S":
            score=score**1
        elif res2[0] == "D":
            score = score ** 2
        elif res2[0]=="T":
            score=score**3

        # 보너스
        if res3 != []:
            if result.index(rr) >0:
                score = (storage+score)*2 - storage
            else:
                score=score*2

        # 옵션
        elif res4 != []:
            score=score*(-1)

        finalscore+=score
        storage=score
    return finalscore

score1 = dartResult("1S2D*3T")
score2 = dartResult("1D2S#10S")
score3 = dartResult("1D2S0T")
score4 = dartResult("1S*2T*3S")
score5 = dartResult("1D#2S*3S")
score6 = dartResult("1T2D3D#")
score7 = dartResult("1D2S3T*")
# print(score1)
# print(score2)
# print(score3)
# print(score4)
# print(score5)
# print(score6)
# print(score7)
# score = dartResult("1D2S3T*#") # *,# 둘 다 있는 경우
# print(score)

# 3번 문제
def calc_cache(cacheSize,cities):
    cache = []
    cha = 0
    for city in cities: # 사용자 검색 가정
        city=city.lower()
        if city not in cache: # 캐시에 담겨 있는지 확인(안담긴 경우) - cache miss
            try:
                if len(cache) < cacheSize: # 캐시 공간이 남았는지 확인하고(남은 경우)
                    cache.append(city)
                else: # 공간이 안남았으면
                    cache.remove(cache[0])
                    cache.append(city)
                cha += 5  # 캐시 계산은 한번에
            except:
                cha += 5
        else: # 담긴 경우 - cache hit
            index = cache.index(city) # 인덱스 알아내서 변경
            cache.remove(cache[index])
            cache.append(city)
            cha+=1
    return cha

cacheSize1=3
cities1=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cha1= calc_cache(cacheSize1,cities1)
cacheSize2=3
cities2=["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cha2 = calc_cache(cacheSize2,cities2)
cacheSize3=2
cities3=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cha3 = calc_cache(cacheSize3,cities3)
cacheSize4=5
cities4=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cha4 = calc_cache(cacheSize4,cities4)
cacheSize5=2
cities5=["Jeju", "Pangyo", "NewYork", "newyork"]
cha5 = calc_cache(cacheSize5,cities5)
cacheSize6=0
cities6=["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cha6= calc_cache(cacheSize6,cities6)
# print(cha1)
# print(cha2)
# print(cha3)
# print(cha4)
# print(cha5)
# print(cha6)

# 4번 문제
# 운행 간격 가지고 범위를 나누어야 함.
# 탑승 가능 시간의 범위에 포함되는 인원이 초과되면 그 사람을 다음 회차로 밀어내기
# 마지막에 한 명 더 탑승할 수 있으면 도착시간을 마지막 차량 출발 시간으로
# 그렇지 않은 경우 마지막 탑승차량의 탑승자 목록을 비교해서 마지막 한 사람 혹은 최대 전체보다 앞서 도착할 시간 구하기
def boardingTime(n,t,m,timetable): # n: 운행 횟수, t: 운행 간격, m: 1회 최대 탑승 가능 인원
    timetableS = sorted(timetable)
    startT = "09:00"
    onetimeM=0

    # 운행 간격 나누기
    bustime = [startT]
    while(n!=1):
        minute = int(startT[3:]) + t
        if minute < 60:
            startT = startT[:2] + ":" + ("%02d" % minute)
        else:
            hour = int(startT[:2]) + minute // 60
            minute = minute %60
            startT = ("%02d" %hour) + ":" + ("%02d" % minute)
        bustime.append(startT)
        n-=1

    boardingList=[]
    checkList=0
    # 한 명씩 태워보기(태우면서 잘라내야...)
    for bs in bustime:
        if checkList>0:
            timetableS = timetableS[checkList:]
            boardingList=[]
        for tt in timetableS:
            if tt <= bs:
                boardingList.append(tt)
                checkList+=1
                # 한 회차에 탈 수 있는 정원을 이 사람들이 넘나?
                if len(boardingList) < m:
                    startT=bs
                elif len(boardingList) >= m: #  and checkList==len(boardingList)
                    minute = int(tt[3:])-1
                    hour = 0
                    if minute <0:
                        hour = -1
                        minute = 60 +minute
                    startT="%02d"%(int(tt[:2])+hour)+":"+"%02d"%minute
    return startT

timetable=["08:00", "08:01", "08:02", "08:03"]
t1 = boardingTime(1,1,5,timetable)
timetable=["09:10", "09:09", "08:00"]
t2 = boardingTime(2,10,2,timetable)
timetable=["09:00", "09:00", "09:00", "09:00"]
t3 = boardingTime(2,1,2,timetable)
timetable=["00:01", "00:01", "00:01", "00:01", "00:01"]
t4 = boardingTime(1,1,5,timetable)
timetable=["23:59"]
t5 = boardingTime(1,1,1,timetable)
timetable=["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
t6 = boardingTime(10,60,45,timetable)
timetable=["08:59", "09:00", "09:00", "09:00"]
t7 = boardingTime(2,1,2,timetable)

# print(t1)
# print(t2)
# print(t3)
# print(t4)
# print(t5)
# print(t6)
# print(t7)

# 5번 문제
import re

def makelist(str1):
    rex = re.compile("([a-z]{2})")
    list1 = []
    cnt=0
    while cnt != len(str1)-1:
        a = str1[cnt:cnt+2]
        if rex.match(a) != None:
            list1.append(a)
        cnt+=1
    return list1

def jaccard(str1,str2):

    str1 = str1.lower()
    str2 = str2.lower()

    list1 = sorted(makelist(str1))
    list2 = sorted(makelist(str2))

    if list1 == [] and list2 == [] or list1==list2: # 공집합인 경우, 혹은 두 집합이 동일한 경우 처리
        return 65536

    # 교집합과 합집합 구하기(다중집합 아님)
    intersection=[]
    union=sorted(list(set(list1+list2)))

    for li1 in list1:
        for li2 in list2:
            if li1 == li2 and li1 not in intersection:
                intersection.append(li1)

    # 중복검사
    set1 = set(list1)
    set2 = set(list2)

    dictionary1 = {}
    if len(list1) != len(set1):
        for s1 in set1:
            key = s1
            value = list1.count(s1)
            dictionary1[key] = value

    dictionary2 = {}
    if len(list2) != len(set2):
        for s2 in set2:
            key = s2
            value = list2.count(s2)
            dictionary2[key] = value

    for key1, value1 in dictionary1.items():
        for key2, value2 in dictionary2.items():
            if key1==key2 and union.count(key) == 1:
                if value1 <= value2:
                    for i in range(value1-1):
                        intersection.append(key1)
                    for i in range(value2-1):
                        union.append(key1)
                else:
                    for i in range(value2-1):
                        intersection.append(key1)
                    for i in range(value1-1):
                        union.append(key1)

    allList = list(set(list1+list2))
    for al in allList:
        if al not in union:
            union.append(al)

    result = "%d"%(len(intersection)/(len(union))*65536)
    return result

ans1 = jaccard("FRANCE+","french")
ans2 = jaccard("handshake","shake hands")
ans3 = jaccard("aa1+aa2","AAAA12")
ans4 = jaccard("E=M*C^2","e=m*c^2")
# print(ans1)
# print(ans2)
# print(ans3)
# print(ans4)

# 6번 문제
# 일단 네모네모(한 행 내에서는 그냥 2개 이상 이어지면 되고 위아래로 맞아야함.) 찾기. 한바퀴 스캔. - 한 줄 내에서 같은 글자 연속 나오는 것 확인. 위 아래 줄과 비교.
# 네모네모 영역 " "으로 대체
# " " 부분은 윗윗줄에서 가져오기. 가져가진 부분은 ""으로 바꾸기
# 반복
# 없으면 그대로 종료.

def firstfriends(list):
    location=[] # 좌표값 담아줌
    for i in range(len(list)-1):
        for j in range(len(list[0])-2):
            if list[i][j] == list[i][j+1] and list[i+1][j] == list[i+1][j+1] and list[i][j] == list[i+1][j] and list[i][j] != " ":
                if [i,j] not in location:
                    location.append([i,j])
                if [i,j+1] not in location:
                    location.append([i,j+1])
                if [i+1,j] not in location:
                    location.append([i+1,j])
                if [i+1,j+1] not in location:
                    location.append([i+1,j+1])

    location = sorted(location)
    if location==[]:
        return [[], list]

    rownum = location[0][0]
    cnt=0
    changelist=[]
    for loca in location:
        if loca[0] == rownum:
            cnt+=1
        else:
            index = list[loca[0]][loca[1]:cnt] # loca[0]번째에 있는 원소의 loca[1]번째부터
            if index not in changelist:
                changelist.append([loca[0]-cnt+1,index])
            rownum=loca[0]
            cnt=1

    newlist=[]
    cnt=0
    for fl in list:
        for ch in changelist:
            if ch[1] in fl:
                if cnt >=2:#list.index(fl)
                    #index = list.index(fl)
                    origin = list[cnt - 2]
                    print(origin)
                    nl = fl.replace(ch[1], origin[ch[0]:len(ch[1])])
                    origin = origin.replace(origin[ch[0]:len(ch[1])], " "*len(ch[1]))
                    print("++++++++++++++++",list,fl,newlist,origin,cnt,cnt-2)
                    newlist[cnt - 2] = origin
                    newlist.append(nl)
                else:
                    fl = fl.replace(ch[1], " "*len(ch))
                    newlist.append(fl)
            else:
                newlist.append(fl)
            print(newlist)
            input("*")
        cnt+=1
    return [changelist,newlist]

def kakaofriends(firstlist):
    lists = firstfriends(firstlist)

    firstlist = lists[1]

    while lists[0] != []:
        lists = firstfriends(firstlist)
        firstlist = lists[1]

    cnt=0
    for i in firstlist:
        cnt+=i.count(" ")

    return cnt

def friends(lists):
    newlist = []
    for li in lists:
        empty=[]
        for i in range(len(li)):
            empty.append(li[i])
        newlist.append(empty)

    location = []
    for i in range(len(lists)-1):
        for j in range(len(lists[i])-1):
            if lists[i][j] == lists[i][j+1]:
                if lists[i][j] != "*" and lists[i][j] == lists[i+1][j] and lists[i][j] == lists[i+1][j+1]:
                    if [i,j] not in location:
                        location.append([i,j])
                    if [i,j+1] not in location:
                        location.append([i,j+1])
                    if [i+1,j] not in location:
                        location.append([i+1,j])
                    if [i+1,j+1] not in location:
                        location.append([i+1,j+1])
    # print("location:",location)

    for loca in location:
        target = newlist[loca[0]][loca[1]]
        newlist[loca[0]][loca[1]] = target.replace(target,"*")
    # print("newlist:", newlist)

    for loca in location:
        for i in range(loca[0]):
            target = newlist[i][loca[1]] # *로 바뀐 것보다 한 줄 위에 있는 알파벳
            current = newlist[loca[0]][loca[1]] # *로 바뀐 현재
            newlist[loca[0]][loca[1]] = current.replace(current,target)
            newlist[i][loca[1]] = target.replace(target, current)
    # print("newlist2:", newlist)

    cnt=0
    for nl in newlist:
        for n in nl:
            if n=="*":
                cnt+=1
    return [newlist, cnt]

def repeatFriends(newlist):
    result = friends(newlist)

    while True:
        cnt1 = result[1]
        result = friends(result[0])
        cnt2 = result[1]
        if cnt1 == cnt2:
            break
    return result[1]


list1=["CCBDE", "AAADE", "AAABF", "CCBBF"]
result1 = repeatFriends(list1)
list2=["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
result2 = repeatFriends(list2)
# print(result1)
# print(result2)

# 7번
import re
from datetime import datetime, timedelta
def solutions(inputval):
    rex = re.compile("[^ ]+")
    rex2 = re.compile("[^ \:\-]+")
    print(inputval)

    timedata = []
    for iv in inputval:
        datas = rex2.findall(iv)
        year = int(datas[0])
        month = int(datas[1])
        day = int(datas[2])
        hour = int(datas[3])
        minute = int(datas[4])
        sec = int(float(datas[5]))
        sec2 = int(round(float(datas[6][:-1])))
        starttime = datetime(year,month,day,hour,minute,sec)-timedelta(seconds=sec2)-timedelta(seconds=1)
        endtime = datetime(year,month,day,hour,minute,sec)
        timedata.append([starttime,endtime])
        # while starttime != endtime:
        #     starttime=starttime+timedelta(seconds=1)
        #     if starttime not in servertime:
        #         servertime.append(starttime)

    startT = timedata[0][0]
    stopT = timedata[-1][-1]

    # 서버 돌아간 전체 시간을 초단위로 계산
    cnt = 0
    cntserver = []
    while startT < stopT:
        for td in timedata:
            if startT <= td[0] < startT+timedelta(seconds=1):
                cnt += 1
                print('1. ',td, startT + timedelta(seconds=1), cnt)
            elif startT < td[1] <= startT+timedelta(seconds=1):
                cnt += 1
                print('2. ',td, startT + timedelta(seconds=1), cnt)
            elif td[0] < startT and td[1] > startT+timedelta(seconds=1):
                cnt += 1
                print('3. ',td, startT+timedelta(seconds=1), cnt)
            else:
                print('4. ', td, startT + timedelta(seconds=1), cnt)
        cntserver.append(cnt)
        startT += timedelta(seconds=1)
        cnt = 0

    cntserver = sorted(cntserver)
    return cntserver[-1]



inputval1 = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
inputval2 = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
inputval3 = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
count1 = solutions(inputval1)
count2 = solutions(inputval2)
count3 = solutions(inputval3)
print(count1)
print(count2)
print(count3)
