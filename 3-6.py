guest = ['张三','李四','王五']
print(guest)
print(guest.pop(1)+'由于事物繁忙无法赴约,所以名单修改为:')
guest.insert(1,'陆六')
print(guest)
print(guest[0]+'来喝酒。')
print(guest[1]+'来喝酒。')
print(guest[2]+'来喝酒。')
print('发现了更大的餐桌，修改名单为:')
guest.insert(0,'田七')
guest.insert(2,'徐八')
guest.append('刘九')
print(guest)
print('重新发送邀请……')
print(guest[0]+'来喝酒。')
print(guest[1]+'来喝酒。')
print(guest[2]+'来喝酒。')
print(guest[3]+'来喝酒。')
print(guest[4]+'来喝酒。')
print(guest[5]+'来喝酒。')
