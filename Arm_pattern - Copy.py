#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on October 28, 2022, at 10:51
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from pylsl import StreamInfo, StreamOutlet

info = StreamInfo('MyMarkerStream', 'Events', 1, 0, 'string', 'id43536');
outlet = StreamOutlet(info)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Arm_pattern'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Education\\Skoltech\\CNBR\\Остеоинтеграция\\Experiments\\Arm_pattern.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='Экспермент заключается в сборе ЭМГ данных для создание системы \nуправления бионического протеза.  \nНа экране будут отображаться название движений:\n1.Сгибание/разгибание локтя\n2.Сгибание/разгибание запястья\n3.Пронация/супинация кисти\n4.Сжатие/Разжатие в кулак\n5.Сжатие/Разжатие точный схват\n6.Сжатие/Разжатие указательный жест\n7.Перемещение большого пальца из \nбокового положения в центральное и наоборот\n8. Отсутствие движения\nВыполняйте движения: из положения по умолчанию в сокращенное \nи по сигналу в обратном направлении.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=2.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Move"
MoveClock = core.Clock()
Movement = visual.TextStim(win=win, name='Movement',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Forward = visual.TextStim(win=win, name='Forward',
    text='Cжатие',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Backward = visual.TextStim(win=win, name='Backward',
    text='Разжатие',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Neut = visual.TextStim(win=win, name='Neut',
    text='Нейтральное положение\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionComponents = [Instructions, key_resp]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions.started', Instructions.tStartRefresh)
thisExp.addData('Instructions.stopped', Instructions.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Move"-------
    continueRoutine = True
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    MoveComponents = [Movement, Forward, Backward, Neut]
    for thisComponent in MoveComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MoveClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Move"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = MoveClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MoveClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Movement* updates
        if Movement.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Movement.frameNStart = frameN  # exact frame index
            Movement.tStart = t  # local t and not account for scr refresh
            Movement.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Movement, 'tStartRefresh')  # time at next scr refresh
            Movement.setAutoDraw(True)
        if Movement.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Movement.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Movement.tStop = t  # not accounting for scr refresh
                Movement.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Movement, 'tStopRefresh')  # time at next scr refresh
                Movement.setAutoDraw(False)
        if Movement.status == STARTED:  # only update if drawing
            Movement.setText(movement, log=False)
        
        # *Forward* updates
        if Forward.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            Forward.frameNStart = frameN  # exact frame index
            Forward.tStart = t  # local t and not account for scr refresh
            Forward.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Forward, 'tStartRefresh')  # time at next scr refresh
            Forward.setAutoDraw(True)
            outlet.push_sample(f'{stimuli_id}')
        if Forward.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Forward.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Forward.tStop = t  # not accounting for scr refresh
                Forward.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Forward, 'tStopRefresh')  # time at next scr refresh
                Forward.setAutoDraw(False)
        
        # *Neut* updates
        if movement == "Вращение запястьем":
            if Neut.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                Neut.frameNStart = frameN  # exact frame index
                Neut.tStart = t  # local t and not account for scr refresh
                Neut.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Neut, 'tStartRefresh')  # time at next scr refresh
                Neut.setAutoDraw(True)
                outlet.push_sample(f'{stimuli_id}')
            if Neut.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Neut.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Neut.tStop = t  # not accounting for scr refresh
                    Neut.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Neut, 'tStopRefresh')  # time at next scr refresh
                    Neut.setAutoDraw(False)
        
        # *Backward* updates
        if Backward.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            Backward.frameNStart = frameN  # exact frame index
            Backward.tStart = t  # local t and not account for scr refresh
            Backward.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Backward, 'tStartRefresh')  # time at next scr refresh
            Backward.setAutoDraw(True)
            outlet.push_sample(f'{stimuli_id}')
        if Backward.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Backward.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Backward.tStop = t  # not accounting for scr refresh
                Backward.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Backward, 'tStopRefresh')  # time at next scr refresh
                Backward.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MoveComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Move"-------
    for thisComponent in MoveComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Movement.started', Movement.tStartRefresh)
    trials.addData('Movement.stopped', Movement.tStopRefresh)
    trials.addData('Forward.started', Forward.tStartRefresh)
    trials.addData('Forward.stopped', Forward.tStopRefresh)
    trials.addData('Backward.started', Backward.tStartRefresh)
    trials.addData('Backward.stopped', Backward.tStopRefresh)
    trials.addData('Neut.started', Neut.tStartRefresh)
    trials.addData('Neut.stopped', Neut.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
