import smartTv as st

my4KTv = st.Tv4k('65', 'silver', '4K')
my4KTv.setSmartTv('on')
my4KTv.turnOn()
my4KTv.printTvInfo()
my4KTv.turnOff()


friend4KTv = st.Tv4k('55', 'white', '4K')
friend4KTv.setSmartTv('off')
friend4KTv.turnOn()
friend4KTv.printTvInfo()
friend4KTv.turnOff()



my8KTv = st.Tv8k('75', 'black', '8K')
my8KTv.setSmartTv('on')
my8KTv.setAiTv('on')
my8KTv.turnOn()
my8KTv.printTvInfo()
my8KTv.turnOff()


friend8KTv = st.Tv8k('86', 'red', '8K')
friend8KTv.setSmartTv('on')
friend8KTv.setAiTv('off')
friend8KTv.turnOn()
friend8KTv.printTvInfo()
friend8KTv.turnOff()
