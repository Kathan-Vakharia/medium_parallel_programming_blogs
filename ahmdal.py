import matplotlib.pyplot as plt
import numpy as np

# Real-world scenario: 20 workers take 36 months to complete a project
# This means total work = 20 workers × 36 months = 720 worker-months
baseline_workers = 20
baseline_time = 36
total_work = baseline_workers * baseline_time  # 720 worker-months

print(
    f"Project Scenario: {baseline_workers} workers take {baseline_time} months")
print(f"Total work required: {total_work} worker-months")
print("-" * 50)

# Different scenarios: What % of work MUST be done in sequence?
scenarios = [
    (0.1, "Highly Parallel Work (10% sequential)", "green"),
    (0.3, "Moderately Parallel (30% sequential)", "blue"),
    (0.5, "Mixed Work (50% sequential)", "orange"),
    (0.9, "Mostly Sequential (90% sequential)", "red")
]

# Test different team sizes
team_sizes = np.arange(5, 101, 5)  # From 5 to 100 workers

# Create the plot with beginner-friendly styling
plt.figure(figsize=(12, 8))
plt.style.use('default')  # Clean, simple style

for sequential_fraction, label, color in scenarios:
    completion_times = []

    for workers in team_sizes:
        # Time for work that MUST be done sequentially (can't be parallelized)
        sequential_time = (sequential_fraction * total_work) / baseline_workers

        # Time for work that CAN be done in parallel
        parallel_work = total_work * (1 - sequential_fraction)
        parallel_time = parallel_work / workers

        # Total project time = sequential time + parallel time
        total_time = sequential_time + parallel_time
        completion_times.append(total_time)

    # Plot with thick lines and clear markers
    plt.plot(team_sizes, completion_times,
             linewidth=3, marker='o', markersize=6,
             label=label, color=color, alpha=0.8)

# Add reference line for original scenario
original_time = [baseline_time] * len(team_sizes)
plt.plot(team_sizes, original_time,
         '--', linewidth=2, color='gray', alpha=0.7,
         label=f'Original: {baseline_workers} workers, {baseline_time} months')

# Make the chart beginner-friendly
plt.title('Why Adding More Workers Doesn\'t Always Speed Up Projects\n(Amdahl\'s Law in Action)',
          fontsize=16, fontweight='bold', pad=20)

plt.xlabel('Number of Workers on the Project', fontsize=14, fontweight='bold')
plt.ylabel('Total Project Time (Months)', fontsize=14, fontweight='bold')

# Improve legend and grid
plt.legend(fontsize=11, loc='upper right', framealpha=0.9)

# Add helpful annotations - positioned to avoid legend overlap
plt.annotate('* Key Insight: When most work is sequential,\nadding workers helps very little!',
             xy=(25, 15), fontsize=12,
             bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8))
plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)

# Set axis limits and ticks for better readability
plt.xlim(0, 100)
plt.ylim(0, max(baseline_time + 10, 60))
plt.xticks(np.arange(0, 101, 10), fontsize=11)
plt.yticks(fontsize=11)

# Add some explanatory text
plt.figtext(0.12, 0.02,
            "> Each line shows how project time changes with team size for different types of work.\n" +
            "> Red line (90% sequential): Adding workers barely helps - most work can't be parallelized.\n" +
            "> Green line (10% sequential): Adding workers helps a lot - most work can be split up.",
            fontsize=10, style='italic')

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)  # Make room for explanation text

# Print some key insights for beginners
print("\n🎯 KEY TAKEAWAYS:")
print(
    f"• With 10% sequential work: 100 workers finish in ~{(0.1 * total_work / baseline_workers + 0.9 * total_work / 100):.1f} months")
print(
    f"• With 90% sequential work: 100 workers finish in ~{(0.9 * total_work / baseline_workers + 0.2 * total_work / 100):.1f} months")
print("• The 'sequential bottleneck' limits how much adding workers can help!")

plt.show()
