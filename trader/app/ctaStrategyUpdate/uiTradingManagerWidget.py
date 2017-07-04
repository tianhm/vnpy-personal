# encoding: UTF-8

'''
CTA模块相关的 持仓管理模块

需要实现的功能如下:

1、获得交易的信号
2、对交易信号产生的下单进行撮合
3、对下单的方向进行管理, 如平进仓等问题。
4、对哪个账户下多少进行管理。


--- 其中最重要的是， 分离掉信号逻辑与交易逻辑部分
'''


from vnpy.event import Event
from vnpy.trader.vtEvent import *
from vnpy.trader.uiBasicWidget import QtGui, QtCore, QtWidgets, BasicCell

from vnpy.trader.app.ctaStrategyUpdate.language import text

import json

from vnpy.event import Event
from vnpy.trader.vtEvent import *
from vnpy.trader.vtConstant import *
from vnpy.trader.vtObject import VtTickData, VtBarData
from vnpy.trader.vtGateway import VtSubscribeReq, VtOrderReq, VtCancelOrderReq, VtLogData
from vnpy.trader.vtFunction import todayDate

from vnpy.event import Event
from vnpy.trader.vtEvent import *
from vnpy.trader.uiBasicWidget import QtGui, QtCore, QtWidgets, BasicCell

from vnpy.trader.app.ctaStrategyUpdate.language import text



class tradingManager():

	#----------------------------------------------------------------------
    def __init__(self, ctaEngine, eventEngine, parent=None):
        """Constructor"""
        super(CtaEngineManager, self).__init__(parent)
        
        self.ctaEngine = ctaEngine
        self.eventEngine = eventEngine
        
        self.strategyLoaded = False
        
        self.initUi()
        self.registerEvent()
        
        # 记录日志
        self.ctaEngine.writeCtaLog(text.CTA_ENGINE_STARTED)        

    # 初始化UI
    def initUI():
    	print "Init UI"

    def registerEvent(self):
        """注册事件监听"""
        self.signal.connect(self.updateCtaLog)
        self.eventEngine.register(EVENT_CTA_LOG, self.signal.emit)

def loadSetting(filename = 'CTA_setting.json'):
	with open(filename) as f:
		l = json.load(f)
        
        print l
        print l[0]["params"]
        for setting in l:
        	print setting
        #	loadStrategy(setting)



if __name__ == '__main__':
	#loadSetting(filename = "CTA_setting.json")
	#engine = ctaEngine(None , None)
    #tm = tradingManager(None , None) 

     # 创建事件引擎
    # ee = EventEngine2()
    
    # # 创建主引擎
    # me = MainEngine(ee)

    #engine = CtaEngine(me, ee)

    print "1"