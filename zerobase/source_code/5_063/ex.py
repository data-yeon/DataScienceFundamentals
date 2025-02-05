import  mem

m_name = input('이름 입력: ')
m_mail = input('메일 주소 입력: ')
m_pw = input('비밀번호 입력: ')
m_addr = input('주소 입력: ')
m_phone = input('연락처 입력: ')

try:
    mem.checkInputData(m_name, m_mail, m_pw, m_addr, m_phone)
    newMember = mem.RegisteMember(m_name, m_mail, m_pw, m_addr, m_phone)
    newMember.printMemberInfo()

except mem.EmptyDataException as e:
    print(e)



