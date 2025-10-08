import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

conditions = ctrl.Antecedent(np.arange(0, 5, 0.25), 'conditions')
visibility = ctrl.Antecedent(np.arange(0, 101, 1), 'visibility')
speed = ctrl.Consequent(np.arange(0, 60, 1), 'speed')

# Custom membership functions
conditions['slight'] = fuzz.zmf(conditions.universe, 1, 1.25)
conditions['intermediate'] = fuzz.trapmf(conditions.universe, [1, 1.25, 2.5, 3])
conditions['rough'] = fuzz.smf(conditions.universe, 2.5, 3)

visibility['bad'] = fuzz.zmf(visibility.universe, 25, 60)
visibility['ok'] = fuzz.trapmf(visibility.universe, [40, 60, 70, 80])
visibility['good'] = fuzz.smf(visibility.universe, 70, 80)

speed['low'] = fuzz.zmf(speed.universe, 15, 20)
speed['medium'] = fuzz.trapmf(speed.universe, [15, 30, 40, 50])
speed['high'] = fuzz.smf(speed.universe, 45, 50)

# Should you wish to view any of the membership functions
# conditions.view(speed['low'])

# rule1 = ctrl.Rule(visibility['bad'] | conditions['rough'], speed['low'])
# rule2 = ctrl.Rule(visibility['ok'], speed['medium'])
# rule3 = ctrl.Rule(visibility['good'] & conditions['slight'], speed['high'])

# speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
# speed_sim = ctrl.ControlSystemSimulation(speed_ctrl)

# speed_sim.input['conditions'] = 1.1
# speed_sim.input['visibility'] = 55

# speed_sim.compute()

# print(speed_sim.output['speed'])

# If you want to view the centroid
# speed.view(sim=speed_sim)

time = ctrl.Antecedent(np.arange(0, 5, 0.25), 'time')
complexity = ctrl.Antecedent(np.arange(0, 1, 1), 'complexity')
studyHours = ctrl.Consequent(np.arange(0, 20, 1), 'studyHours')

time['short'] = fuzz.zmf(time.universe, 1, 2)
time['medium'] = fuzz.trapmf(time.universe, [2, 3.25, 4, 4])
time['long'] = fuzz.smf(time.universe, 4, 7)

complexity['low'] = fuzz.zmf(complexity.universe, 0.1, 0.3)
complexity['medium'] = fuzz.trapmf(complexity.universe, [0.25, 0.5, 0.65, 0.7])
complexity['high'] = fuzz.smf(complexity.universe, 0.6, 1)

studyHours['short'] = fuzz.zmf(studyHours.universe, 0, 1)
studyHours['medium'] = fuzz.trapmf(studyHours.universe, [1, 1.25, 2.5, 3])
studyHours['long'] = fuzz.smf(studyHours.universe, 2.5, 5)

rule1 = ctrl.Rule(time['short'] | complexity['high'], studyHours['long'])
rule2 = ctrl.Rule(complexity['medium'], studyHours['medium'])
rule3 = ctrl.Rule(time['long'] & complexity['low'], studyHours['short'])

studyHours_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
studyHours_sim = ctrl.ControlSystemSimulation(studyHours_ctrl)

studyHours_sim.input['time'] = 1.5
studyHours_sim.input['complexity'] = 0.2

studyHours_sim.compute()

print(studyHours_sim.output['studyHours'])