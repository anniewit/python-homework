from expyriment import design, control, stimuli,io
from expyriment.misc import constants
import random,time

control.defaults.window_mode = True # True corresponds to windowed
control.defaults.window_size = [1024,768] # 800x600 resolution
design.defaults.experiment_background_colour = (200,200,200)

# create experiment object
exp = design.Experiment(name="Dot Reaction Experiment")
# initialize experiment object and make it active experiment
# this will show a startup screen, it will also initialize exp.screen, exp.mouse, exp.keyboard, exp.event and exp.clock
control.initialize(exp)

exp.keyboard.set_quit_key(113)

# create block after initializing the experiment
block_one = design.Block(name="Our only block")
tmp_trial = design.Trial()

# set up fixation cross
cross = stimuli.FixCross(colour=(0,0,0))
cross.preload()
cross = stimuli.FixCross()
cross.preload()

# set up stimulus positions
pos = {1: (4.5, 128, 64), 2: (2.5, 200, 200),
    3: (5, -256, -192), 4: (1, 256, -350),
    5: (5, -200, 200), 6: (2.25, -128, 350),
    7: (2.5, 200, -200), 8: (1, -128, -64),
    9: (4, -450, 0), 10: (2, 450, 0)}

runs = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(runs)
offsets =[]

for i in range(0,len(pos)):
    current = runs[i]
    stim = stimuli.Circle(radius=25,colour=(0,0,0),position=[pos[current][1],pos[current][2]])
    #offsets.append(pos[current][1])
    stim.preload()
    tmp_trial.add_stimulus(stim)
    tmp_trial.add_stimulus(cross)
    block_one.add_trial(tmp_trial)
    tmp_trial = tmp_trial.copy()
    tmp_trial.clear_stimuli()

exp.add_block(block_one)
control.start()
round = 0
for b in exp.blocks:
    for t in b.trials:
        offset = pos[runs[round]][0]
        time.sleep(offset)
        t.stimuli[0].present(clear=True, update=False)
        t.stimuli[1].present(clear=False, update=True)
        round += 1

        # [misc.constants.K_LEFT, misc.constants.K_RIGHT] doesnt work, even though imported
        key, reaction_time = exp.keyboard.wait()
        print(reaction_time)

# this will show an "ending experiment" screen and save data
control.end()
