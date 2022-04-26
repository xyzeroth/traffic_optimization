# -*- coding: utf-8 -*-

class DBG_OPTIONS :
    ## Options which are related maintaining states
    MaintainServerThreadState = True    # maintain a state of thread

    ## Options which are related to print message
    PrintCtrlDaemon = True          # print messages which are related to operations of CtrlDaemon
    PrintExecDaemon = True          # print messages which are related to operations of CtrlDaemon
    PrintFindOptimalModel = True    # print messages which are related to find optimal model
    PrintGeneratedCommand = True    # print messages which are related to generate command
    PrintImprovementRate = True     # print messages which are related to improvement rate
    PrintServingThread = True       # print messages which are related to serving thread

    PrintSaRelatedInfo = False      # print SA related info
    PrintStep = False               # print progress msgs every step : inferred actions

    PrintMsg = True                 # print messages

    ## Other Options
    RunWithWaitForDebug = False      # wait for debug
    UseConfig = True    # use config dic instead of args
    WithNewCode = True  # run with new code


def waitForDebug(msg):
    if DBG_OPTIONS.RunWithWaitForDebug:
        return input("wait... {}\n\t\tenter if you want to keep going".format(msg))
    else:
        print(msg)
        return 0