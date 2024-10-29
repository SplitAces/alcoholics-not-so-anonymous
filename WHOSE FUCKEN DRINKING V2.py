import random
import time
import matplotlib.pyplot as plt

names = ['Andy', 'Dazza', 'Jon', 'Andrew', 'Ted', 'Tim', 'Trina', 'Elisa', 'Shannon', 'Anita']
selection_count = {name: 0 for name in names}  # Dictionary to keep track of selections

# Initialize the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()

while True:
    # Wait for 60 seconds while updating the countdown
    for remaining in range(60, 0, -1):
        # Clear the plot
        ax.clear()
        
        # Check if it's time to select a name (only once every minute)
        if remaining == 1:
            # Random selection and output
            selection = random.choice(names)
            selection_count[selection] += 1  # Increment the selection count
            
            # Print results to console
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

        # Update the bar chart
        ax.bar(selection_count.keys(), selection_count.values(), color='skyblue')
        
        # Update the timer display
        ax.set_title('Drink Selection Results')
        ax.set_xlabel('Names')
        ax.set_ylabel('Number of Selections')
        ax.set_xticks(range(len(names)))
        ax.set_xticklabels(names, rotation=45)
        
        # Display the countdown timer
        ax.text(0.5, 1.05, f'Time remaining: {remaining}s', ha='center', va='center', fontsize=14, fontweight='bold', transform=ax.transAxes)
        
        plt.pause(1)  # Pause to update the plot

    # Wait for a short period before the next selection to allow for final display
    time.sleep(1)

# Final plot display (This code won't be reached in an infinite loop)
plt.ioff()  # Turn off interactive mode
plt.show()  # Show the final plot
