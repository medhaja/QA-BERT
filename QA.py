import utils
import os
import sys
import time


context = '''The Kargil War, also known as the Kargil conflict, was an armed conflict fought between India and Pakistan from May to July 1999 in the Kargil district of Jammu and Kashmir and elsewhere along the Line of Control (LoC). In India, the conflict is also referred to as Operation Vijay, which was the name of the Indian military operation to clear out the Kargil sector. The Indian Air Force's role in acting jointly with Indian Army ground troops during the war was aimed at flushing out regular and irregular troops of the Pakistan Army from vacated Indian positions along the LoC.This particular operation was given the codename Operation Safed Sagar'''

question = 'what is Operation Vijay'
#  time it takes to run the model
start = time.time()
print(utils.QA_prediction(question, context))
end = time.time() 