"""
Database: Hotel
Table:

Customer(cust_id int primary key,
        fname varchar,
        lastname varchar,
        mobile varchar,
        idproof varchar
        )

reservation(resvid int primary key,
        roomid int  (1,2,3,45,),
        custid
        forgeign key (cust_id),
        checkin date,
        checkout date
        )
room (roomid, room_no)

room_no, no of customers,

SELECT t2.room_no, count(t1.custid) from
reservation t1
right JOIN room t2
ON t1.roomid = t2.roomid
group by t1.custid


"""

str1 = "NAYAN"
str2 = "ABCDE"
print(str1[1:-2])
print(str1 == str1[::-1])
print(str2 == str2[::-1])


def recursive(str1, start=0, end=-1):
    if len(str1) == 1:
        return True

    if str1[start] == str1[end]:
        recursive(str1, start + 1, end - 1)
    else:
        return False


print(recursive(str1))

array = [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]

arr = [[0, 1, 0, 1, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0]]




























