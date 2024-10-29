import random
import time
import matplotlib.pyplot as plt

names = ['Andy', 'Dazza', 'Jon', 'Andrew', 'Ted', 'Tim', 'Trina', 'Elisa', 'Shannon', 'Anita']
selection_count = {name: 0 for name in names}  # Dictionary to keep track of selections

# Initialize the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()

while True:
    # Countdown from 3 to 1
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)  # Sleep for 1 second during the countdown

    # Random selection and output
    selection = random.choice(names)
    selection_count[selection] += 1  # Increment the selection count
    print("Bottom's up! Bottom's up!")
    print(f'{selection} is fucking drinking.')

    # ASCII art of a shot glass
    shot_glass = r"""
        .~~~~.
        i====i_
        |cccc|_)
        |cccc|   
        `-==-'
        """
    print(shot_glass)

    # Update the plot
    ax.clear()  # Clear the previous plot
    ax.bar(selection_count.keys(), selection_count.values(), color='skyblue')

    # Update the timer display
    ax.set_title('Drink Selection Results')
    ax.set_xlabel('Names')
    ax.set_ylabel('Number of Selections')
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=45)

    plt.pause(1)  # Pause to update the plot

    # Wait for 1 minute before the next selection
    time.sleep(60)  # Sleep for 60 seconds

# Final plot display
plt.ioff()  # Turn off interactive mode
plt.show()  # Show the final plot
