import random
import time
import statistics
import matplotlib.pyplot as plt

def linear_search(myList, key):

    for i, k in enumerate(myList):

        if k == key:

            return i
    return -1 #returns -1 if key is not found in the list

def generate_list_unique(n, low=0, high=None):

    if high is None or high - low < n:

        high = low + n * 10

    result = []
    
    while len(result) < n:

        k = random.randint(0, high)

        if linear_search(result, k) == -1:

            result.append(k)

    return result

#sweet now we have set up everything to start our experiment

#calculates the mean time taken to search for a key in the list
def time_taken(myList, key, repeats = 5):

    times = []

    for _ in range(repeats): #iterate the number of repeats

        start = time.perf_counter() #start the timer

        linear_search(myList, key) #call the linear search function
        times.append(time.perf_counter() - start) #append the time taken into the times list

    return statistics.mean(times) #returns the mean of the times taken


def run_experiments(sizes):

    results = {'n': [], 'best': [], 'worst': [], 'avg': []} #dictionary to store the results

    for n in sizes:


        myList = generate_list_unique(n)

        results['n'].append(n) #appends the size of the list to the results
        
        results['best'].append(time_taken(myList, myList[0])) #best case key at beginning

        results['worst'].append(time_taken(myList, None)) #worst case key not in list

        #for avg case we tests keys at random positions and absent
        trials = 20

        keys = [random.choice(myList) for _ in range(trials // 2)] + [None] * (trials // 2) #selects the random keys + the fact that a key can also not be included i nthe list

        avg_time = statistics.mean([time_taken(myList, k, repeats = 1) for k in keys])

        results['avg'].append(avg_time) #appends the average time taken to the results

    return results


#lets plot our results

data = run_experiments([1000, 5000, 10000, 20000, 50000])

plt.plot(data['n'], data['best'], label='Best Case (O(1))')
plt.plot(data['n'], data['avg'], label='Average Case (O(n))')
plt.plot(data['n'], data['worst'], label='Worst Case (O(n))')

plt.xlabel('List Size n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Linear Search: Time vs Input Size')
plt.show()
