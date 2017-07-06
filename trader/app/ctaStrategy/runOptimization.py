# encoding: UTF-8

"""
展示如何执行参数优化。
"""

from __future__ import division


from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, MINUTE_DB_NAME, OptimizationSetting
from ctaBase import *

if __name__ == '__main__':
    from vnpy.trader.app.ctaStrategy.strategy.strategyAtrRsi import AtrRsiStrategy
    #from vnpy.trader.app.ctaStrategy.strategy.strategyLivermore import LivermoreStrategy
    #from vnpy.trader.app.ctaStrategy.strategy.LivermoreStrategy2 import LivermoreStrategy2
    #from vnpy.trader.app.ctaStrategy.strategy.LivermoreHourStrategy import LivermoreHourStrategy
    from vnpy.trader.app.ctaStrategy.strategy.LivermoreThirtyStrategy import LivermoreThirtyStrategy
    # 创建回测引擎
    engine = BacktestingEngine()
    
    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)

    # 设置回测用的数据起始日期
    #engine.setStartDate('20140101')
    engine.setStartDate('20110101')
    
    # 设置产品相关参数
    engine.setSlippage(0.2)     # 股指1跳
    engine.setRate(0.3/10000)   # 万0.3
    engine.setSize(300)         # 股指合约大小 
    engine.setPriceTick(0.2)    # 股指最小价格变动
    
    # 设置使用的历史数据库
    #engine.setDatabase(MINUTE_DB_NAME, 'rb888')
    #engine.setDatabase(HOUR_DB_NAME, 'rb888')
    engine.setDatabase(THIRTY_MINUTE_DB_NAME, 'rb888')
    
    # 跑优化
    # setting = OptimizationSetting()                 # 新建一个优化任务设置对象
    # setting.setOptimizeTarget('capital')            # 设置优化排序的目标是策略净盈利
    # setting.addParameter('atrLength', 12, 20, 2)    # 增加第一个优化参数atrLength，起始12，结束20，步进2
    # setting.addParameter('atrMa', 20, 30, 5)        # 增加第二个优化参数atrMa，起始20，结束30，步进5
    # setting.addParameter('rsiLength', 5)            # 增加一个固定数值的参数
    
    setting = OptimizationSetting() 
    setting.setOptimizeTarget('capital')              # 设置优化排序的目标是策略净盈利
    setting.addParameter('param1',  10  , 200 , 5)      # 增加第一个优化参数atrLength，起始12，结束20，步进2
    setting.addParameter('param2',  10 , 120,  5)          
    
    #setting = OptimizationSetting()

    # 性能测试环境：I7-3770，主频3.4G, 8核心，内存16G，Windows 7 专业版
    # 测试时还跑着一堆其他的程序，性能仅供参考
    import time    
    start = time.time()
    
    # 运行单进程优化函数，自动输出结果，耗时：359秒
    #engine.runOptimization(AtrRsiStrategy, setting)            
    #engine.runOptimization(LivermoreStrategy2, setting)
    #engine.runOptimization(LivermoreHourStrategy, setting)
    engine.runOptimization(LivermoreThirtyStrategy, setting)
    
    # 多进程优化，耗时：89秒
    #engine.runParallelOptimization(AtrRsiStrategy, setting)
    #engine.runParallelOptimization(LivermoreStrategy, setting)
    #engine.runParallelOptimization(LivermoreStrategy2, setting)
    
    print u'耗时：%s' %(time.time()-start)