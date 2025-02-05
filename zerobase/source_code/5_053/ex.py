import member as mb

mems = mb.MemberRepository()

for i in range(3):
    mId = input('아이디 입력: ')
    mPw = input('비밀번호 입력: ')
    mem = mb.Member(mId, mPw)
    mems.addMember(mem)

mems.printMembers()


mems.loginMember('abc@gmail.com', '1234')
mems.loginMember('def@gmail.com', '5678')
mems.loginMember('ghi@gmail.com', '9012')

mems.removeMember('abc@gmail.com', '1234')

mems.printMembers()