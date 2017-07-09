# encoding: UTF-8

"""
展示如何执行参数优化。
"""

from __future__ import division


from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, MINUTE_DB_NAME, OptimizationSetting
from ctaBase import *

if __name__ == '__main__':

    from strategy.strategyLivermore5 import *

    # 创建回测引擎
    engine = BacktestingEngine()
    
    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)

    # 设置回测用的数据起始日期
    #engine.setStartDate('20140101')
    engine.setStartDate('20110101')
    
    '''
    # 设置产品相关参数
    engine.setSlippage(0.2)     # 股指1跳
    engine.setRate(0.3/10000)   # 万0.3
    engine.setSize(300)         # 股指合约大小 
    engine.setPriceTick(0.2)    # 股指最小价格变动
    '''

    engine.setSlippage(1.0)      
    engine.setRate(1.29/10000)    # 万0.3

    engine.setSize(10)          # 股指合约大小  , 一跳
    engine.setPriceTick(1.0)    # 股指最小价格变动


    # 设置使用的历史数据库
    #engine.setDatabase(MINUTE_DB_NAME, 'rb888')
    #engine.setDatabase(HOUR_DB_NAME, 'rb888')
    engine.setDatabase(MINUTE_DB_NAME, 'rb888')
    
    # 跑优化
    # setting = OptimizationSetting()                 # 新建一个优化任务设置对象
    # setting.setOptimizeTarget('capital')            # 设置优化排序的目标是策略净盈利
    # setting.addParameter('atrLength', 12, 20, 2)    # 增加第一个优化参数atrLength，起始12，结束20，步进2
    # setting.addParameter('atrMa', 20, 30, 5)        # 增加第二个优化参数atrMa，起始20，结束30，步进5
    # setting.addParameter('rsiLength', 5)            # 增加一个固定数值的参数
    
    setting = OptimizationSetting() 
    setting.setOptimizeTarget('capital')              # 设置优化排序的目标是策略净盈利
    setting.addParameter('param1',  30 )              # 
    setting.addParameter('param2',  10 )
    setting.addParameter('minute_use',  30 )
    setting.addParameter('kai_down',  40 , 40 , 4)
    setting.addParameter('wg_size', 5 , 30 , 5)   
    
    #setting = OptimizationSetting()

    # 性能测试环境：I7-3770，主频3.4G, 8核心，内存16G，Windows 7 专业版
    # 测试时还跑着一堆其他的程序，性能仅供参考
    import time    
    start = time.time()
    
    # 运行单进程优化函数，自动输出结果，耗时：359秒
    #engine.runOptimization(AtrRsiStrategy, setting)            
    #engine.runOptimization(LivermoreStrategy2, setting)
    #engine.runOptimization(LivermoreHourStrategy, setting)
    #engine.runOptimization(LivermoreThirtyStrategy, setting)
    engine.runOptimization(Livermore_5_Strategy, setting)

    # 多进程优化，耗时：89秒
    #engine.runParallelOptimization(AtrRsiStrategy, setting)
    #engine.runParallelOptimization(LivermoreStrategy, setting)
    #engine.runParallelOptimization(LivermoreStrategy2, setting)
    
    print u'耗时：%s' %(time.time()-start)